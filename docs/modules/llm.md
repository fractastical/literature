# LLM Module

Local LLM integration for research assistance.

## Overview

The LLM module provides a unified interface for interacting with local large language models (via Ollama) to assist with research tasks. It offers flexible response modes, comprehensive validation, and conversation context management.

## Key Components

### LLMClient (`core/client.py`)

Main interface for querying LLMs:
- Multiple response modes (short, long, structured, raw)
- Streaming support
- Context management
- Template support

### Configuration (`core/config.py`)

Configuration management:
- LLMConfig for global settings
- GenerationOptions for per-query control
- Environment variable support

### Templates (`templates/`)

Pre-built prompt templates:
- Research templates
- Manuscript review templates
- Template registry

### Validation (`validation/`)

Output validation:
- JSON validation
- Format compliance
- Repetition detection
- Structure validation

## Usage Examples

### Basic Usage

```python
from infrastructure.llm import LLMClient

client = LLMClient()
response = client.query("What is machine learning?")
```

### Response Modes

```python
# Short response
answer = client.query_short("Define AI")

# Long response
explanation = client.query_long("Explain neural networks in detail")

# Structured response
result = client.query_structured(
    "Analyze...",
    schema={"type": "object", "properties": {...}}
)
```

### Templates

```python
from infrastructure.llm.templates import PaperSummarization

template = PaperSummarization()
prompt = template.render(text=paper_text)
```

## Configuration

See [Configuration Guide](../guides/configuration.md) for environment variables and settings.

## See Also

- **[LLM Module Documentation](../infrastructure/llm/AGENTS.md)** - Complete documentation
- **[API Reference](../reference/api-reference.md)** - API documentation

