# Ethereum Specifications

Welcome to the Ethereum Specifications documentation. This project provides a modern Python foundation for writing Ethereum protocol specifications with integrated testing support.

## Overview

This template helps developers create well-structured, testable specifications for Ethereum protocols. It includes:

- **Modern Python tooling** with `uv` for fast dependency management
- **Type safety** with Pydantic models and full mypy support
- **Comprehensive testing** with pytest and coverage reporting
- **Code quality** with Ruff for fast linting and formatting
- **Documentation** with MkDocs Material theme

## Quick Start

```bash
# Clone the repository
git clone <repository-url> {PROJECT_NAME}
cd {PROJECT_NAME}

# Install dependencies
uv sync --all-extras

# Run tests
uv run pytest

# Start documentation server
uv run mkdocs serve
```

## Features

### Type-Safe Specifications

Using Pydantic for automatic validation:

```python
from pydantic import BaseModel, Field

class Transaction(BaseModel):
    nonce: int = Field(..., ge=0)
    gas_price: int = Field(..., ge=0)
    gas_limit: int = Field(..., ge=0)
    value: int = Field(..., ge=0)
```

### Structured Testing

Tests mirror the source structure for easy navigation:

```
src/specs/types.py → tests/specs/test_types.py
src/subspecs/eip.py → tests/subspecs/test_eip.py
```

### Development Tools

Pre-configured environment with:

- **Ruff**: Fast Python linter and formatter
- **Mypy**: Static type checking with Pydantic plugin
- **Pytest**: Testing with coverage and parallel execution
- **Tox**: Test automation across environments
- **Pre-commit**: Automated code quality checks

## Project Structure

```
├── src/
│   ├── specs/              # Main specification modules
│   │   ├── types.py        # Core data types
│   │   └── validation.py   # Validation logic
│   └── subspecs/           # Sub-specifications (EIPs)
│       └── example_eip.py  # Example implementation
├── tests/                  # Test suite
│   ├── specs/              # Tests for main specs
│   └── subspecs/           # Tests for subspecs
├── docs/                   # Documentation
└── pyproject.toml         # Project configuration
```

## Next Steps

- Review the [example types](https://github.com/{GITHUB_ORG}/{PACKAGE_NAME}/blob/main/src/specs/types.py)
- Check out the [test examples](https://github.com/{GITHUB_ORG}/{PACKAGE_NAME}/tree/main/tests)
- Read the [README](https://github.com/{GITHUB_ORG}/{PACKAGE_NAME}#readme) for development workflow