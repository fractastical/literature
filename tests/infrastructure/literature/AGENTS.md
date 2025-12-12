# Literature Tests Module

## Purpose

Comprehensive test suite for literature search and management functionality, including integration tests with real APIs.

## Test Files

### Core Tests
- `test_core.py` - LiteratureSearch core functionality
- `test_config.py` - Configuration tests
- `test_integration.py` - Integration tests
- `test_literature_integration_real.py` - Real API integration tests

### Source Tests
- `test_api.py` - API adapter tests
- `test_unpaywall.py` - Unpaywall integration tests

### PDF Tests
- `test_pdf_handler_simple.py` - Basic PDF handler tests
- `test_pdf_handler_comprehensive.py` - Comprehensive PDF tests
- `test_pdf_handler_fallbacks.py` - PDF fallback strategy tests

### Library Tests
- `test_library_index.py` - Library indexing tests
- `test_clear_operations.py` - Library cleanup tests

### Summarization Tests
- `test_summarizer.py` - Summarization engine tests
- `test_summarization_streaming.py` - Streaming summarization tests
- `test_chunker.py` - Text chunking tests
- `test_prompt_builder.py` - Prompt builder tests

### Workflow Tests
- `test_workflow.py` - Workflow orchestration tests
- `test_workflow_skip_existing.py` - Skip existing functionality tests
- `test_progress.py` - Progress tracking tests

### Analysis Tests
- `test_analysis.py` - Paper analysis tests
- `test_meta_analysis.py` - Meta-analysis tests

### CLI Tests
- `test_literature_cli.py` - CLI interface tests
- `test_literature_cli_simple.py` - Simple CLI tests

### LLM Operations Tests
- `test_llm_operations.py` - LLM operations tests
- `test_llm_operations_real.py` - Real LLM integration tests
- `test_paper_selector.py` - Paper selection tests

### Other Tests
- `test_html_parsing.py` - HTML parser tests
- `test_reporting.py` - Reporting tests
- `test_logging.py` - Logging tests
- `test_structured_logging.py` - Structured logging tests
- `test_pure_logic.py` - Pure logic tests

## Running Tests

```bash
# All literature tests
pytest tests/infrastructure/literature/

# Specific category
pytest tests/infrastructure/literature/test_core.py
pytest tests/infrastructure/literature/test_summarizer.py

# Integration tests
pytest tests/infrastructure/literature/test_literature_integration_real.py
```

## Test Coverage

Comprehensive coverage of:
- Core search functionality
- Source adapters
- PDF handling and fallbacks
- Library management
- Summarization system
- Workflow orchestration
- Meta-analysis
- CLI interface
- LLM operations

## See Also

- [`README.md`](README.md) - Quick reference
- [`../../infrastructure/literature/AGENTS.md`](../../infrastructure/literature/AGENTS.md) - Literature module documentation

