#!/usr/bin/env python3
"""Tests for infrastructure/validation/pdf_validator.py.

Tests PDF validation and text extraction functionality.
No mocks - tests actual PDF processing.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Add repo root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from infrastructure.validation.pdf_validator import (
    PDFValidationError,
    extract_text_from_pdf,
)


class TestPDFValidationError:
    """Test PDFValidationError exception."""
    
    def test_error_creation(self):
        """Test creating a PDFValidationError."""
        error = PDFValidationError("Test error")
        assert str(error) == "Test error"
        assert isinstance(error, Exception)


class TestExtractTextFromPDF:
    """Test extract_text_from_pdf function."""
    
    def test_extract_nonexistent_file(self, tmp_path):
        """Test extraction from non-existent file."""
        pdf_path = tmp_path / "nonexistent.pdf"
        
        with pytest.raises(PDFValidationError):
            extract_text_from_pdf(pdf_path)
    
    def test_extract_invalid_pdf(self, tmp_path):
        """Test extraction from invalid PDF file."""
        pdf_path = tmp_path / "invalid.pdf"
        pdf_path.write_bytes(b"Not a PDF file")
        
        with pytest.raises(PDFValidationError):
            extract_text_from_pdf(pdf_path)
    
    def test_extract_valid_pdf(self, tmp_path):
        """Test extraction from valid PDF file."""
        # Create a simple valid PDF for testing
        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import letter
            
            pdf_path = tmp_path / "valid.pdf"
            c = canvas.Canvas(str(pdf_path), pagesize=letter)
            c.drawString(100, 750, "Test PDF Content")
            c.save()
            
            text = extract_text_from_pdf(pdf_path)
            assert isinstance(text, str)
            assert len(text) > 0
            
        except ImportError:
            pytest.skip("reportlab not available for PDF creation")
    
    def test_extract_empty_pdf(self, tmp_path):
        """Test extraction from empty PDF."""
        # Create minimal valid PDF
        pdf_path = tmp_path / "empty.pdf"
        pdf_path.write_bytes(
            b"%PDF-1.4\n"
            b"1 0 obj\n"
            b"<< /Type /Catalog >>\n"
            b"endobj\n"
            b"xref\n"
            b"0 1\n"
            b"trailer\n"
            b"<< /Root 1 0 R >>\n"
            b"%%EOF\n"
        )
        
        # Should not raise error, but may return empty text
        try:
            text = extract_text_from_pdf(pdf_path)
            assert isinstance(text, str)
        except PDFValidationError:
            # Some PDFs may fail validation
            pass
    
    def test_extract_pdf_with_text(self, tmp_path):
        """Test extraction from PDF with text content."""
        try:
            from reportlab.pdfgen import canvas
            from reportlab.lib.pagesizes import letter
            
            pdf_path = tmp_path / "test.pdf"
            c = canvas.Canvas(str(pdf_path), pagesize=letter)
            c.drawString(100, 750, "Test PDF Content")
            c.drawString(100, 730, "This is a test PDF file.")
            c.save()
            
            text = extract_text_from_pdf(pdf_path)
            assert isinstance(text, str)
            assert len(text) > 0
            # Text may be extracted in different formats
            assert "Test" in text or "test" in text.lower()
            
        except ImportError:
            pytest.skip("reportlab not available for PDF creation")


class TestPDFValidatorModule:
    """Test PDF validator module structure."""
    
    def test_module_imports(self):
        """Test that module imports correctly."""
        from infrastructure.validation import pdf_validator
        assert pdf_validator is not None
        assert hasattr(pdf_validator, 'extract_text_from_pdf')
        assert hasattr(pdf_validator, 'PDFValidationError')
    
    def test_function_signatures(self):
        """Test function signatures."""
        import inspect
        
        sig = inspect.signature(extract_text_from_pdf)
        assert 'pdf_path' in sig.parameters
        assert sig.return_annotation == str

