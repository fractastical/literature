# Workflow Operations Module

## Purpose

The operations module contains operation-specific implementations split from the orchestrator for better modularity and testability. Each operation module handles a specific workflow task.

## Module Structure

```
operations/
├── search.py          # Search operations
├── download.py        # PDF download operations
├── cleanup.py         # Library cleanup operations
├── meta_analysis.py   # Meta-analysis pipeline
├── llm_operations.py  # Advanced LLM operations
└── utils.py           # Common utilities
```

## Components

### Search Operations (`search.py`)

Search and bibliography management operations.

**Functions:**
- `run_search_only()` - Execute search only (add to bibliography, no PDF download)
- `run_search()` - Execute full search workflow (search + download)
- `get_keywords_input()` - Interactive prompt for search keywords
- `get_limit_input()` - Interactive prompt for search limit
- `get_clear_options_input()` - Interactive prompt for clear options

**Usage:**
```python
from infrastructure.literature.workflow.operations import run_search_only

# Search only (adds to bibliography)
run_search_only(keywords=["machine learning"], limit=10)
```

### Download Operations (`download.py`)

PDF download operations for existing bibliography entries.

**Functions:**
- `run_download_only()` - Download PDFs for existing bibliography entries
- `find_papers_needing_pdf()` - Find library entries that need PDF downloads
- `library_entry_to_search_result()` - Convert LibraryEntry to SearchResult
- `failed_download_to_search_result()` - Convert failed download entry to SearchResult
- `get_pdf_path_for_entry()` - Get expected PDF path for library entry

**Failed Downloads Tracking:**
- All download failures are automatically saved to `data/failed_downloads.json`
- By default, previously failed downloads are **automatically skipped** to avoid wasting time
- Use `retry_failed=True` to retry previously failed downloads
- The `find_papers_needing_pdf()` function filters out failed downloads unless `retry_failed=True`
- Failures are saved for both regular downloads and retry attempts
- "no_pdf_url" failures are warnings and not tracked

**Usage:**
```python
from infrastructure.literature.workflow.operations import run_download_only

# Download PDFs for existing entries (skips previously failed downloads)
run_download_only()

# Retry previously failed downloads
run_download_only(retry_failed=True)
```

### Cleanup Operations (`cleanup.py`)

Library cleanup and orphaned file management.

**Functions:**
- `run_cleanup()` - Clean up library (remove papers without PDFs, delete orphaned files)
- `find_orphaned_files()` - Find orphaned files not in bibliography
- `find_orphaned_pdfs()` - Find orphaned PDFs for meta-analysis
- `delete_orphaned_files()` - Delete orphaned files with error handling

**Usage:**
```python
from infrastructure.literature.workflow.operations import run_cleanup

# Clean up library
run_cleanup(remove_no_pdf=True, delete_orphaned=True)
```

### Meta-Analysis Operations (`meta_analysis.py`)

Meta-analysis pipeline execution.

**Functions:**
- `run_meta_analysis()` - Execute literature search workflow with meta-analysis
  - Runs search → download → extract → meta-analysis pipeline
  - Performs PCA analysis, keyword analysis, author analysis, and visualizations

**Failed Downloads Tracking:**
- All download failures during the meta-analysis pipeline are automatically saved
- Previously failed downloads are **automatically skipped** by default
- Use `retry_failed=True` to retry previously failed downloads
- Failures are saved for both regular downloads and retry attempts
- The download step uses `find_papers_needing_pdf()` which filters out failed downloads unless `retry_failed=True`

**Usage:**
```python
from infrastructure.literature.workflow.operations import run_meta_analysis

# Run meta-analysis pipeline (skips previously failed downloads)
run_meta_analysis(keywords=["active inference"], limit=25)

# Retry previously failed downloads
run_meta_analysis(keywords=["active inference"], limit=25, retry_failed=True)
```

### LLM Operations (`llm_operations.py`)

Advanced LLM operations for multi-paper synthesis.

**Functions:**
- `run_llm_operation()` - Execute advanced LLM operation on selected papers
  - Supports: review, communication, compare, gaps, network operations
  - Uses paper selection config for filtering

**Usage:**
```python
from infrastructure.literature.workflow.operations import run_llm_operation

# Generate literature review
run_llm_operation(operation_type="review", paper_config_path="paper_selection.yaml")
```

### Utilities (`utils.py`)

Common utilities for workflow operations.

**Functions:**
- `get_source_descriptions()` - Get descriptions for all available sources
- `display_sources_with_status()` - Display sources with health status
- `get_source_selection_input()` - Interactive prompt to select sources
- `display_file_locations()` - Display file location summary

**Constants:**
- `SOURCE_DESCRIPTIONS` - Dictionary mapping source names to descriptions

## Module Organization

This module follows the **thin orchestrator pattern**:
- **Operations modules**: Contain all business logic
- **Orchestrator**: Thin coordinator that imports and re-exports functions
- **Clear separation**: Logic vs. orchestration

## Integration

All functions are re-exported from `infrastructure.literature.workflow.operations` for convenience:

```python
from infrastructure.literature.workflow.operations import (
    run_search_only,
    run_download_only,
    run_cleanup,
    run_meta_analysis,
    run_llm_operation,
)
```

## See Also

- [`README.md`](README.md) - Quick reference
- [`../AGENTS.md`](../AGENTS.md) - Workflow module documentation
- [`../../AGENTS.md`](../../AGENTS.md) - Literature module overview

