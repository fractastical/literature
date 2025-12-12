# Tests Module

## Purpose

The tests module provides comprehensive test coverage for all infrastructure modules. Tests follow a no-mocks policy, using real data and computations.

## Test Organization

```
tests/
└── infrastructure/
    ├── core/          # Core utilities tests
    ├── llm/           # LLM integration tests
    └── literature/    # Literature search tests
```

## Test Philosophy

### No Mocks Policy

All tests use real data and real computations:
- No MagicMock, mocker.patch, or unittest.mock
- Real LLM responses when possible
- Real file operations
- Real API calls (with graceful skipping)

### Test Categories

1. **Pure Logic Tests** - Test business logic without network access
2. **Integration Tests** - Test with real services (marked with `@pytest.mark.requires_ollama`)

## Running Tests

### All Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=infrastructure --cov-report=html
```

### Module-Specific Tests

```bash
# Core tests
pytest tests/infrastructure/core/

# LLM tests
pytest tests/infrastructure/llm/

# Literature tests
pytest tests/infrastructure/literature/
```

### Integration Tests

```bash
# Skip integration tests (fast)
pytest -m "not requires_ollama"

# Only integration tests (requires Ollama)
pytest -m requires_ollama
```

## Test Coverage

### Core Module
- 15 test files
- Comprehensive coverage of all utilities
- Exception handling tests
- Configuration tests

### LLM Module
- 22 test files
- 88%+ coverage
- Pure logic and integration tests
- Template and validation tests

### Literature Module
- 32 test files
- Comprehensive coverage
- Integration tests with real APIs
- Workflow and orchestration tests

## Test Documentation

- `tests/infrastructure/llm/AGENTS.md` - LLM test documentation
- `tests/infrastructure/llm/README.md` - LLM test quick reference

## See Also

- [`README.md`](README.md) - Quick reference
- [`infrastructure/core/AGENTS.md`](../infrastructure/core/AGENTS.md) - Core module documentation
- [`infrastructure/llm/AGENTS.md`](../infrastructure/llm/AGENTS.md) - LLM module documentation
- [`infrastructure/literature/AGENTS.md`](../infrastructure/literature/AGENTS.md) - Literature module documentation

