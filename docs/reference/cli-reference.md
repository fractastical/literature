# CLI Reference

Complete command-line interface reference.

## Literature CLI

### Search Command

```bash
python3 -m infrastructure.literature.core.cli search "query" [options]
```

**Options:**
- `--limit N` - Limit results per source
- `--sources SOURCES` - Comma-separated source list
- `--download` - Download PDFs automatically

**Examples:**
```bash
# Basic search
python3 -m infrastructure.literature.core.cli search "machine learning"

# Search with options
python3 -m infrastructure.literature.core.cli search "transformers" \
    --limit 20 \
    --sources arxiv,semanticscholar \
    --download
```

### Library Commands

#### List

```bash
python3 -m infrastructure.literature.core.cli library list [--limit N]
```

#### Stats

```bash
python3 -m infrastructure.literature.core.cli library stats
```

#### Export

```bash
python3 -m infrastructure.literature.core.cli library export [--output FILE]
```

#### Validate

```bash
python3 -m infrastructure.literature.core.cli library validate
```

#### Cleanup

```bash
python3 -m infrastructure.literature.core.cli library cleanup [--no-pdf]
```

## LLM CLI

### Query Command

```bash
python3 -m infrastructure.llm.cli query "prompt" [options]
```

**Options:**
- `--short` - Short response mode
- `--long` - Long response mode
- `--stream` - Stream output
- `--model MODEL` - Override model
- `--temperature FLOAT` - Temperature
- `--max-tokens INT` - Max tokens
- `--seed INT` - Random seed

**Examples:**
```bash
# Basic query
python3 -m infrastructure.llm.cli query "What is machine learning?"

# Short response
python3 -m infrastructure.llm.cli query --short "Define AI"

# With options
python3 -m infrastructure.llm.cli query \
    --temperature 0.0 \
    --seed 42 \
    "Test query"
```

### Check Command

```bash
python3 -m infrastructure.llm.cli check
```

### Models Command

```bash
python3 -m infrastructure.llm.cli models
```

### Template Command

```bash
# List templates
python3 -m infrastructure.llm.cli template --list

# Apply template
python3 -m infrastructure.llm.cli template TEMPLATE_NAME --input "text"
```

## Orchestrator Script

### Literature Search Script

```bash
python3 scripts/07_literature_search.py [options]
```

**Modes:**
- `--search` - Search for papers
- `--search-only` - Search without downloading
- `--download-only` - Download PDFs only
- `--extract-text` - Extract text from PDFs
- `--summarize` - Generate summaries
- `--meta-analysis` - Run meta-analysis
- `--cleanup` - Clean up library
- `--llm-operation OPERATION` - Advanced LLM operations

**Options:**
- `--keywords KEYWORDS` - Comma-separated keywords
- `--limit N` - Limit per keyword
- `--sources SOURCES` - Source list

**Examples:**
```bash
# Search
python3 scripts/07_literature_search.py --search --keywords "machine learning"

# Summarize
python3 scripts/07_literature_search.py --summarize

# Meta-analysis
python3 scripts/07_literature_search.py --meta-analysis --keywords "optimization"
```

## See Also

- **[API Reference](api-reference.md)** - Python API documentation
- **[Configuration Guide](../guides/configuration.md)** - Configuration options

