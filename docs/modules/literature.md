# Literature Module

Literature search and management functionality.

## Overview

The literature module provides comprehensive tools for searching scientific papers, downloading PDFs, managing references, and generating AI-powered summaries.

## Key Components

### Core (`core/`)

Main interface for literature operations:
- LiteratureSearch class
- Configuration management
- CLI interface

### Sources (`sources/`)

API adapters for academic databases:
- arXiv
- Semantic Scholar
- PubMed
- CrossRef
- OpenAlex
- DBLP
- bioRxiv/medRxiv
- Europe PMC
- Unpaywall (open access)

### PDF (`pdf/`)

PDF handling:
- Downloading with retry logic
- Text extraction
- Fallback strategies
- HTML parsing

### Library (`library/`)

Library management:
- JSON-based indexing
- BibTeX generation
- Statistics and reporting
- Cleanup operations

### Summarization (`summarization/`)

AI-powered summarization:
- Multi-stage generation
- Quality validation
- Context extraction
- Progress tracking

### Meta-Analysis (`meta_analysis/`)

Analysis tools:
- Temporal trends
- Keyword evolution
- PCA analysis
- Visualizations

## Usage Examples

### Search

```python
from infrastructure.literature import LiteratureSearch

searcher = LiteratureSearch()
papers = searcher.search("machine learning", limit=10)
```

### Add to Library

```python
for paper in papers:
    citation_key = searcher.add_to_library(paper)
    searcher.download_paper(paper)
```

### Summarization

```python
from infrastructure.literature.summarization import SummarizationEngine
from infrastructure.llm import LLMClient

llm_client = LLMClient()
engine = SummarizationEngine(llm_client)

result = engine.summarize_paper(
    result=search_result,
    pdf_path=Path("data/pdfs/paper.pdf")
)
```

## See Also

- **[Literature Module Documentation](../infrastructure/literature/AGENTS.md)** - Complete documentation
- **[Searching Papers Guide](../guides/search-papers.md)** - Search guide
- **[Summarizing Papers Guide](../guides/summarize-papers.md)** - Summarization guide

