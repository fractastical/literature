# PDF Module - Complete Documentation

## Purpose

The PDF module handles all aspects of PDF downloading, text extraction, and URL resolution with comprehensive fallback strategies.

## Components

### PDFHandler (handler.py)

Main interface for PDF downloading and management.

**Key Methods:**
- `download_paper()` - Download PDF for a search result
- `download_pdf()` - Download PDF from URL with citation key naming

**Features:**
- Automatic retry with exponential backoff
- User-Agent rotation (limited to 2 attempts)
- Multiple fallback strategies (configurable limits)
- Citation key-based file naming
- Configurable retry limits to prevent excessive attempts

### PDFDownloader (downloader.py)

Low-level PDF download implementation.

**Features:**
- Content type validation
- HTML response detection
- Recursive HTML parsing (limited depth)
- Error categorization
- Optimized retry logic with configurable limits
- Early exit for clearly unavailable URLs (404)
- Smart detection of when to stop retrying

### PDF Extractor (extractor.py)

Text extraction and HTML parsing utilities.

**Functions:**
- `extract_pdf_urls_from_html()` - Extract PDF URLs from HTML content
- `extract_citations()` - Extract citations from PDF (placeholder)

### PDF Fallbacks (fallbacks.py)

Fallback strategies for PDF URL resolution.

**Strategies:**
- URL transformation (PMC, arXiv, bioRxiv patterns)
- Unpaywall lookup
- DOI-based URL generation
- Publisher-specific patterns

## Usage Examples

### Basic Download

```python
from infrastructure.literature.pdf import PDFHandler
from infrastructure.literature.core import LiteratureConfig

config = LiteratureConfig()
handler = PDFHandler(config)

pdf_path = handler.download_paper(search_result)
```

### Fallback Strategies

The handler automatically tries multiple strategies:
1. Primary URL from search result
2. Transformed URLs (PMC variants, etc.)
3. Unpaywall lookup
4. arXiv title search
5. bioRxiv/medRxiv DOI lookup

## Error Handling

PDF downloads categorize failures:
- `access_denied` - HTTP 403 Forbidden (tries multiple User-Agents and referers)
- `not_found` - HTTP 404 Not Found (early exit, no retries)
- `html_response` - HTML received instead of PDF (tries transformed URLs)
- `timeout` - Request timeout
- `network_error` - Connection errors

Error messages include helpful context and troubleshooting suggestions.

## Configuration

### Retry Limits

To prevent excessive retry attempts, configure:

```python
config = LiteratureConfig(
    max_url_attempts_per_pdf=8,  # Maximum total URL attempts per PDF (default: 8)
    max_fallback_strategies=3,   # Maximum fallback strategy attempts (default: 3)
)
```

Or via environment variables:
```bash
export LITERATURE_MAX_URL_ATTEMPTS_PER_PDF=8
export LITERATURE_MAX_FALLBACK_STRATEGIES=3
```

### Retry Behavior

The downloader uses optimized retry logic:
- **Standard download**: 1 attempt
- **Transformed URLs**: Up to 2 variants (for HTML responses)
- **User-Agent rotation**: Up to 2 different User-Agents
- **Minimal headers**: 1 attempt
- **HEAD request**: Skipped for persistent 403 errors
- **Referer spoofing**: 1 attempt (Google referer)
- **Academic referers**: 1 attempt (Scholar/Semantic Scholar)
- **Standard retries**: Up to `download_retry_attempts` (default: 2)

Total attempts are limited by `max_url_attempts_per_pdf` (default: 8).

## Troubleshooting

### PDF Download Failures

**Common Issues:**

1. **403 Forbidden errors**
   - The server may be blocking automated requests
   - Try accessing the URL manually in a browser
   - Check if the PDF requires authentication
   - The downloader automatically tries multiple User-Agents and referers

2. **HTML received instead of PDF**
   - The URL points to a web page, not a direct PDF link
   - The downloader automatically tries transformed URLs
   - Some publishers require clicking a download button (not supported)

3. **404 Not Found**
   - The PDF URL does not exist or has been moved
   - The downloader exits early for 404 errors (no retries)
   - Check the source URL or try alternative sources

4. **Excessive retry attempts**
   - Configure `max_url_attempts_per_pdf` to limit total attempts
   - Default is 8 attempts per PDF
   - Reduce if downloads are taking too long

### Missing PDF Libraries

If you see "No PDF parsing library available":
- Install one of: `pdfplumber`, `pypdf`, or `PyPDF2`
- `pypdf>=5.0` should be installed automatically with the project
- If missing, try: `pip install -e .` or `pip install pypdf`
- For best quality, install: `pip install pdfplumber`

## See Also

- [`README.md`](README.md) - Quick reference
- [`../AGENTS.md`](../AGENTS.md) - Literature module overview


