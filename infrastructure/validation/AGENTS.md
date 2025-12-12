# Validation Module

## Purpose

The validation module provides PDF text extraction functionality needed by the literature summarization system. This is a minimal subset focused on PDF processing.

## Components

### PDF Text Extraction (`pdf_validator.py`)

Extracts text content from PDF files:
- **Text extraction**: Extracts all text from PDF files
- **Warning suppression**: Suppresses harmless pypdf warnings
- **Error handling**: Comprehensive error handling for PDF issues

## Usage Examples

### Extracting Text from PDF

```python
from infrastructure.validation.pdf_validator import extract_text_from_pdf
from pathlib import Path

pdf_path = Path("data/pdfs/paper.pdf")
text = extract_text_from_pdf(pdf_path)
```

## Error Handling

```python
from infrastructure.validation.pdf_validator import (
    extract_text_from_pdf,
    PDFValidationError
)

try:
    text = extract_text_from_pdf(pdf_path)
except PDFValidationError as e:
    print(f"PDF extraction failed: {e}")
```

## Dependencies

- **pypdf**: PDF parsing library

## See Also

- [`README.md`](README.md) - Quick reference
- [`pdf_validator.py`](pdf_validator.py) - Implementation

