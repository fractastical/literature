# Infrastructure Layer Module

Complete documentation for the infrastructure layer.

## Overview

The infrastructure layer provides reusable, standalone modules for literature search, PDF management, reference tracking, and AI-powered summarization. It is designed to be completely independent and self-contained.

## Module Structure

```
infrastructure/
├── core/          # Foundation utilities
├── llm/           # Local LLM integration
├── literature/    # Literature search and management
└── validation/    # Validation utilities
```

## Core Module

Foundation utilities used across all infrastructure modules.

**Key Components:**
- Logging system
- Exception hierarchy
- Configuration management
- Progress tracking
- Checkpoint management
- Retry logic
- Performance monitoring

**See:** [Core Module Documentation](../infrastructure/core/AGENTS.md)

## LLM Module

Local LLM integration for research assistance.

**Key Components:**
- LLMClient for Ollama interaction
- Configuration management
- Context management
- Template system
- Output validation
- Review generation

**See:** [LLM Module Documentation](../infrastructure/llm/AGENTS.md)

## Literature Module

Literature search and management functionality.

**Key Components:**
- LiteratureSearch main interface
- Source adapters (arXiv, Semantic Scholar, etc.)
- PDF handling
- Library management
- Summarization system
- Meta-analysis tools

**See:** [Literature Module Documentation](../infrastructure/literature/AGENTS.md)

## Usage

### Importing Modules

```python
# Core utilities
from infrastructure.core import get_logger, TemplateError

# LLM integration
from infrastructure.llm import LLMClient, LLMConfig

# Literature search
from infrastructure.literature import (
    LiteratureSearch,
    LiteratureConfig
)
```

## Configuration

All modules support environment variable configuration. See [Configuration Guide](guides/configuration.md) for details.

## See Also

- **[Getting Started](../getting-started.md)** - Quick start guide
- **[Architecture Overview](../architecture.md)** - System architecture
- **[API Reference](../reference/api-reference.md)** - Complete API documentation

