# Core Module

Foundation utilities for the infrastructure layer.

## Overview

The core module provides essential utilities used across all infrastructure modules, including logging, exception handling, configuration management, and progress tracking.

## Key Components

### Logging (`logging_utils.py`)

Unified Python logging system with consistent formatting:
- Environment-based configuration (LOG_LEVEL 0-3)
- Context managers for operation tracking
- Decorators for function call logging
- Integration with bash logging format

### Exceptions (`exceptions.py`)

Comprehensive exception hierarchy:
- Base exception classes
- Module-specific exceptions
- Context preservation
- Exception chaining utilities

### Configuration (`config_loader.py`)

Configuration management:
- YAML configuration file loading
- Environment variable support
- Configuration file discovery
- Translation language configuration

### Progress (`progress.py`)

Progress tracking utilities:
- Visual progress indicators
- Sub-stage progress tracking
- Progress bar utilities

### Checkpoint (`checkpoint.py`)

Pipeline checkpoint management:
- Save/restore pipeline state
- Stage result tracking

### Retry (`retry.py`)

Retry logic with exponential backoff:
- Transient failure handling
- Retryable operation wrappers

## Usage Examples

### Logging

```python
from infrastructure.core import get_logger, log_operation

logger = get_logger(__name__)
logger.info("Starting process")

with log_operation("Data processing", logger):
    process_data()
```

### Exception Handling

```python
from infrastructure.core import TemplateError, chain_exceptions

try:
    risky_operation()
except ValueError as e:
    raise chain_exceptions(
        TemplateError("Operation failed"),
        e
    )
```

### Configuration

```python
from infrastructure.core import load_config

config = load_config(Path("config.yaml"))
```

## See Also

- **[Core Module Documentation](../infrastructure/core/AGENTS.md)** - Complete documentation
- **[API Reference](../reference/api-reference.md)** - API documentation

