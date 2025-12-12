# Searching Papers Guide

Complete guide to searching for academic papers using the Literature Search system.

## Quick Start

### Command Line

```bash
# Interactive search
python3 scripts/07_literature_search.py --search

# Search with keywords
python3 scripts/07_literature_search.py --search --keywords "machine learning,deep learning"
```

### Python API

```python
from infrastructure.literature import LiteratureSearch

searcher = LiteratureSearch()
papers = searcher.search("machine learning", limit=10)
```

## Search Sources

The system supports multiple academic databases:

- **arXiv** - Preprints in physics, mathematics, computer science
- **Semantic Scholar** - AI-powered research tool
- **PubMed** - Biomedical literature
- **CrossRef** - DOI resolution and metadata
- **OpenAlex** - Open scholarly metadata
- **DBLP** - Computer science bibliography
- **bioRxiv/medRxiv** - Biology and medicine preprints
- **Europe PMC** - European biomedical literature

### Configuring Sources

```bash
# Set sources via environment variable
export LITERATURE_SOURCES="arxiv,semanticscholar,pubmed"
```

```python
# Set sources programmatically
from infrastructure.literature import LiteratureConfig, LiteratureSearch

config = LiteratureConfig(sources=["arxiv", "semanticscholar"])
searcher = LiteratureSearch(config)
```

## Search Options

### Limit Results

```python
# Limit per source
papers = searcher.search("query", limit=25)

# Limit via environment
export LITERATURE_DEFAULT_LIMIT=25
```

### Source Selection

```python
# Use specific sources
papers = searcher.search(
    "query",
    sources=["arxiv", "semanticscholar"]
)
```

### Statistics

```python
# Get search statistics
papers, stats = searcher.search(
    "query",
    return_stats=True
)

print(f"Total results: {stats.total_results}")
print(f"Sources used: {stats.sources_used}")
```

## Processing Results

### Add to Library

```python
for paper in papers:
    citation_key = searcher.add_to_library(paper)
    print(f"Added: {citation_key}")
```

### Download PDFs

```python
for paper in papers:
    if paper.pdf_url:
        result = searcher.download_paper(paper)
        if result:
            print(f"Downloaded: {result}")
```

### Complete Workflow

```python
papers = searcher.search("active inference", limit=10)

for paper in papers:
    # Add to library
    citation_key = searcher.add_to_library(paper)
    
    # Download PDF
    if paper.pdf_url:
        pdf_path = searcher.download_paper(paper)
        print(f"Downloaded: {pdf_path}")
```

## Deduplication

The system automatically deduplicates results:
- Exact DOI matching (highest priority)
- Fuzzy title similarity matching
- Relevance ranking to keep best results

## Health Checking

Check source availability before searching:

```python
health_status = searcher.get_source_health_status()
for source, status in health_status.items():
    print(f"{source}: {'healthy' if status['healthy'] else 'unhealthy'}")
```

## Best Practices

1. **Use specific keywords** - More specific queries yield better results
2. **Combine sources** - Use multiple sources for comprehensive coverage
3. **Check source health** - Verify sources are available before large searches
4. **Limit results** - Use appropriate limits to avoid overwhelming results
5. **Review before adding** - Check results before adding to library

## Troubleshooting

### No Results

- Check source health status
- Verify internet connection
- Try different keywords
- Check source-specific requirements (API keys, etc.)

### Slow Searches

- Reduce limit per source
- Use fewer sources
- Check network connectivity
- Verify source rate limits

## See Also

- **[API Reference](../reference/api-reference.md)** - Complete API documentation
- **[Literature Module Documentation](../infrastructure/literature/AGENTS.md)** - Module documentation

