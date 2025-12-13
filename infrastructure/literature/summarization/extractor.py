"""Text extraction from PDFs for summarization pipeline.

This module handles the extraction of text from PDF files and saving
to data/extracted_text/ for use in the summarization pipeline.
"""
from __future__ import annotations

import os
import time
from pathlib import Path
from typing import Optional, Tuple

from infrastructure.core.logging_utils import get_logger
from infrastructure.literature.summarization.pdf_processor import PDFProcessor
from infrastructure.validation.pdf_validator import extract_text_from_pdf, PDFValidationError

logger = get_logger(__name__)


class TextExtractor:
    """Extracts text from PDFs and saves to extracted_text directory.
    
    Handles the first stage of the summarization pipeline:
    PDF → extracted text file → (later) summarization
    """
    
    def __init__(self):
        """Initialize text extractor."""
        self.pdf_processor = PDFProcessor()
        self.extracted_text_dir = Path("data/extracted_text")
        self.extracted_text_dir.mkdir(parents=True, exist_ok=True)
    
    def extract_and_save(
        self,
        pdf_path: Path,
        citation_key: Optional[str] = None,
        use_prioritization: bool = False,
        max_chars: Optional[int] = None
    ) -> Tuple[bool, Optional[str], int]:
        """Extract text from PDF and save to extracted_text directory.
        
        Args:
            pdf_path: Path to PDF file.
            citation_key: Citation key for the paper (defaults to PDF stem).
            use_prioritization: Whether to use prioritized extraction (default: False).
            max_chars: Maximum characters for prioritized extraction (if used).
            
        Returns:
            Tuple of (success, error_message, chars_extracted).
            - success: True if extraction and saving succeeded
            - error_message: Error message if failed, None if succeeded
            - chars_extracted: Number of characters extracted (0 if failed)
        """
        if citation_key is None:
            citation_key = pdf_path.stem
        
        extracted_text_path = self.extracted_text_dir / f"{citation_key}.txt"
        
        # Check if extracted text already exists
        if extracted_text_path.exists():
            existing_size = extracted_text_path.stat().st_size
            abs_path = extracted_text_path.resolve()
            abs_pdf_path = pdf_path.resolve()
            logger.info(
                f"[{citation_key}] Extracted text already exists: {abs_path} "
                f"({existing_size:,} bytes) from {abs_pdf_path}. Skipping extraction."
            )
            # Read existing file to get char count
            try:
                existing_text = extracted_text_path.read_text(encoding='utf-8')
                return True, None, len(existing_text)
            except Exception as e:
                logger.warning(
                    f"[{citation_key}] Failed to read existing extracted text: {e}. "
                    f"Re-extracting..."
                )
                # Continue to extraction below
        
        # Extract text from PDF
        logger.info(f"[{citation_key}] Extracting text from {pdf_path.name}...")
        extraction_start = time.time()
        
        try:
            if use_prioritization and max_chars:
                # Use prioritized extraction
                prioritized_result = self.pdf_processor.extract_prioritized_text(
                    pdf_path, max_chars
                )
                pdf_text = prioritized_result.text
                
                if prioritized_result.truncation_occurred:
                    logger.info(
                        f"[{citation_key}] Prioritized extraction: "
                        f"{prioritized_result.original_length:,} -> "
                        f"{prioritized_result.final_length:,} chars. "
                        f"Sections: {', '.join(prioritized_result.sections_included)}"
                    )
            else:
                # Use full extraction (no truncation)
                pdf_text = extract_text_from_pdf(pdf_path)
            
            extraction_time = time.time() - extraction_start
            
            if not pdf_text or len(pdf_text.strip()) < 100:
                # Gather diagnostic information
                pdf_size = pdf_path.stat().st_size if pdf_path.exists() else 0
                pdf_exists = pdf_path.exists()
                extracted_chars = len(pdf_text) if pdf_text else 0
                extracted_words = len(pdf_text.split()) if pdf_text else 0
                
                error_msg = (
                    f"Insufficient text extracted from PDF "
                    f"(less than 100 characters). "
                    f"Extracted: {extracted_chars} chars, {extracted_words} words. "
                    f"PDF: {pdf_path.name} ({pdf_size:,} bytes, exists: {pdf_exists})"
                )
                logger.warning(f"[{citation_key}] {error_msg}")
                logger.warning(f"  PDF path: {pdf_path.resolve()}")
                logger.warning(f"  This may indicate a scanned PDF, corrupted file, or extraction issue")
                return False, error_msg, 0
            
            # Save extracted text to file
            try:
                extracted_text_path.write_text(pdf_text, encoding='utf-8')
                file_size = extracted_text_path.stat().st_size
                
                chars_extracted = len(pdf_text)
                words_extracted = len(pdf_text.split())
                
                abs_extracted_path = extracted_text_path.resolve()
                abs_pdf_path = pdf_path.resolve()
                file_size = extracted_text_path.stat().st_size
                logger.info(
                    f"[{citation_key}] Extracted and saved text: "
                    f"{chars_extracted:,} chars, {words_extracted:,} words "
                    f"({extraction_time:.2f}s, {file_size:,} bytes) -> {abs_extracted_path} (from {abs_pdf_path})"
                )
                
                return True, None, chars_extracted
                
            except Exception as e:
                error_msg = f"Failed to save extracted text: {e}"
                abs_extracted_path = extracted_text_path.resolve()
                abs_pdf_path = pdf_path.resolve()
                
                # Gather diagnostic information
                text_length = len(pdf_text) if pdf_text else 0
                output_dir_exists = extracted_text_path.parent.exists()
                output_dir_writable = extracted_text_path.parent.is_dir() and os.access(extracted_text_path.parent, os.W_OK) if output_dir_exists else False
                
                logger.error(f"[{citation_key}] {error_msg}")
                logger.error(f"  PDF source: {abs_pdf_path}")
                logger.error(f"  Expected output: {abs_extracted_path}")
                logger.error(f"  Extracted text length: {text_length:,} chars")
                logger.error(f"  Output directory exists: {output_dir_exists}, writable: {output_dir_writable}")
                logger.error(f"  Error type: {type(e).__name__}")
                return False, error_msg, len(pdf_text) if pdf_text else 0
                
        except PDFValidationError as e:
            extraction_time = time.time() - extraction_start
            abs_pdf_path = pdf_path.resolve()
            abs_extracted_path = extracted_text_path.resolve()
            
            # Gather diagnostic information
            pdf_exists = pdf_path.exists()
            pdf_size = pdf_path.stat().st_size if pdf_exists else 0
            pdf_readable = pdf_path.is_file() and pdf_path.stat().st_mode & 0o444 if pdf_exists else False
            
            error_msg = f"PDF extraction failed: {e}"
            logger.error(f"[{citation_key}] {error_msg} (took {extraction_time:.2f}s)")
            logger.error(f"  PDF source: {abs_pdf_path}")
            logger.error(f"  PDF exists: {pdf_exists}, size: {pdf_size:,} bytes, readable: {pdf_readable}")
            logger.error(f"  Expected output: {abs_extracted_path}")
            logger.error(f"  Error type: {type(e).__name__}")
            return False, error_msg, 0
        except Exception as e:
            extraction_time = time.time() - extraction_start
            abs_pdf_path = pdf_path.resolve()
            abs_extracted_path = extracted_text_path.resolve()
            
            # Gather diagnostic information
            pdf_exists = pdf_path.exists()
            pdf_size = pdf_path.stat().st_size if pdf_exists else 0
            pdf_readable = pdf_path.is_file() and pdf_path.stat().st_mode & 0o444 if pdf_exists else False
            
            error_msg = f"Unexpected error during extraction: {e}"
            logger.error(f"[{citation_key}] {error_msg} (took {extraction_time:.2f}s)")
            logger.error(f"  PDF source: {abs_pdf_path}")
            logger.error(f"  PDF exists: {pdf_exists}, size: {pdf_size:,} bytes, readable: {pdf_readable}")
            logger.error(f"  Expected output: {abs_extracted_path}")
            logger.error(f"  Error type: {type(e).__name__}")
            logger.debug(f"Full traceback for {citation_key}:", exc_info=True)
            return False, error_msg, 0
    
    def load_extracted_text(self, citation_key: str) -> Optional[str]:
        """Load extracted text from file.
        
        Args:
            citation_key: Citation key for the paper.
            
        Returns:
            Extracted text if file exists, None otherwise.
        """
        extracted_text_path = self.extracted_text_dir / f"{citation_key}.txt"
        
        if not extracted_text_path.exists():
            return None
        
        try:
            text = extracted_text_path.read_text(encoding='utf-8')
            logger.debug(
                f"[{citation_key}] Loaded extracted text: {len(text):,} chars "
                f"from {extracted_text_path}"
            )
            return text
        except Exception as e:
            logger.warning(
                f"[{citation_key}] Failed to load extracted text from "
                f"{extracted_text_path}: {e}"
            )
            return None
    
    def has_extracted_text(self, citation_key: str) -> bool:
        """Check if extracted text exists for a citation key.
        
        Args:
            citation_key: Citation key for the paper.
            
        Returns:
            True if extracted text file exists, False otherwise.
        """
        extracted_text_path = self.extracted_text_dir / f"{citation_key}.txt"
        return extracted_text_path.exists()



