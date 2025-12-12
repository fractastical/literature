# Tests Module

Comprehensive test suite for infrastructure modules.

## Quick Start

```bash
# Run all tests
pytest

# Run specific module
pytest tests/infrastructure/core/
```

## Test Organization

- **core/** - Core utilities tests
- **llm/** - LLM integration tests
- **literature/** - Literature search tests

## Test Philosophy

- No mocks policy
- Real data and computations
- Integration tests marked with `@pytest.mark.requires_ollama`

## See Also

- [`AGENTS.md`](AGENTS.md) - Complete documentation

