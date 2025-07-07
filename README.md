# Ethereum Protocol Specifications Template

A modern Python template for Ethereum protocol specifications with best practices and tooling.

## 🚀 Using This Template

This is a template repository. To use it for your own Ethereum specification project:

### Option 1: Use GitHub's Template Feature (Recommended)

1. Click the "Use this template" button on GitHub
2. Create a new repository with your desired name
3. Clone your new repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME
   cd YOUR_REPO_NAME
   ```

### Option 2: Clone Directly

1. **Clone the template:**
   ```bash
   git clone https://github.com/fselmo/ethereum-protocol-specs my-ethereum-spec
   cd my-ethereum-spec
   
   # Remove the existing git history
   rm -rf .git
   git init
   ```

### Setup Your Project

1. **Run the setup script:**
   ```bash
   # Use uv to run the setup script in an isolated environment
   uv run --no-project python scripts/setup.py
   ```
   
   The script will prompt you for:
   - Project name
   - Package name (for Python imports)
   - GitHub organization/username
   - Author name and email
   - Copyright year

2. **Clean up and sync:**
   ```bash
   # Remove the setup script
   rm scripts/setup.py
   
   # Update dependencies
   uv sync --all-extras
   
   # Verify everything works
   uv run pytest
   ```

3. **Start developing your specifications!**

## Features

- **Modern Python tooling**: Uses `uv` for fast, reliable dependency management
- **Type safety**: Pydantic models for data validation and mypy for static typing
- **Testing**: pytest with coverage reporting and parallel execution
- **Code quality**: Ruff for fast linting and auto-formatting
- **Documentation**: MkDocs with Material theme for beautiful docs
- **Developer friendly**: Simple commands, clear structure

## Quick Start

### Prerequisites

- Python 3.12 or later
- [uv](https://github.com/astral-sh/uv) package manager

### Setup

```bash
# Clone this repository
git clone <repository-url> {PROJECT_NAME}
cd {PROJECT_NAME}

# Install dependencies
uv sync --all-extras

# Install pre-commit hooks (optional but recommended)
uvx pre-commit install

# Run tests to verify setup
uv run pytest
```

### Project Structure

```
├── src/
│   ├── specs/              # Main protocol specifications
│   ├── subspecs/           # Sub-specifications (EIPs, features)
│   └── example/            # Example implementations (reference only)
├── tests/
│   ├── specs/              # Tests for main specs
│   ├── subspecs/           # Tests for subspecs
│   └── example/            # Example tests (reference only)
├── docs/                   # Documentation source
└── pyproject.toml         # Project configuration
```

The `example` directories contain reference implementations showing how to use Pydantic models and write tests. These would not be included in an actual specification repository.

## Development Workflow

### Running Tests

```bash
# Run all tests (runs with coverage by default)
uv run pytest

# Run specific test file
uv run pytest tests/specs/test_types.py

# Run tests in parallel
uv run pytest -n auto
```

### Code Quality

```bash
# Check code style and errors
uv run ruff check src tests

# Auto-fix issues
uv run ruff check --fix src tests

# Format code
uv run ruff format src tests

# Type checking
uv run mypy src tests
```

### Using Tox

```bash
# Run all environments (tests, linting, type checking, docs)
uvx --with=tox-uv tox

# Run specific environment
uvx --with=tox-uv tox -e lint

# List available environments
uvx --with=tox-uv tox -av
```

### Pre-commit Hooks

The project includes pre-commit hooks that automatically check your code before commits:

```bash
# Install pre-commit hooks (one-time setup)
uvx pre-commit install

# Run hooks manually on all files
uvx pre-commit run --all-files

# Skip hooks for a single commit
git commit --no-verify
```

Hooks include:
- Trailing whitespace removal
- End-of-file fixing
- YAML/TOML validation
- Ruff linting and formatting
- MyPy type checking

### Documentation

```bash
# Serve docs locally (with auto-reload)
uv run mkdocs serve

# Build docs
uv run mkdocs build
```

## Writing Specifications

### Example: Creating a New Type

```python
# src/specs/new_types.py
from pydantic import BaseModel, Field

class NewTransaction(BaseModel):
    """A new transaction type for the protocol."""
    
    version: int = Field(..., ge=1)
    data: bytes = Field(...)
    signature: bytes = Field(..., min_length=65, max_length=65)
```

### Example: Adding Validation

```python
# src/specs/new_validation.py
from .new_types import NewTransaction

def validate_new_transaction(tx: NewTransaction) -> bool:
    """Validate the new transaction type."""
    # Add validation logic
    return len(tx.data) > 0 and tx.version >= 1
```

### Example: Writing Tests

```python
# tests/specs/test_new_types.py
import pytest
from pydantic import ValidationError
from specs.new_types import NewTransaction

# Parametrized test - test multiple inputs
@pytest.mark.parametrize("version", [1, 2, 3])
def test_transaction_versions(version):
    """Test different transaction versions."""
    tx = NewTransaction(version=version, data=b"test", signature=b"0" * 65)
    assert tx.version == version

# Exception testing
def test_invalid_transaction():
    """Test that invalid data raises ValidationError."""
    with pytest.raises(ValidationError) as exc_info:
        NewTransaction(version=0, data=b"", signature=b"short")
    
    assert "version" in str(exc_info.value)  # Check error details
```

## Tips for Non-Python Developers

- **Pydantic models**: Think of these as strongly-typed data structures that validate inputs automatically
- **Type hints**: Python's way of declaring types (like TypeScript for JavaScript)
- **pytest**: Testing framework - just name test files `test_*.py` and functions `test_*`
- **uv**: Fast Python package manager - like npm/yarn but for Python

## Common Commands Reference

| Task | Command |
|------|---------|
| Install deps | `uv sync` |
| Run tests | `uv run pytest` |
| Format code | `uv run ruff format src tests` |
| Check types | `uv run mypy src tests` |
| Serve docs | `uv run mkdocs serve` |
| Run all checks | `uvx --with=tox-uv tox` |

## Contributing

1. Make your changes
2. Run `uv run ruff format src tests` to format code
3. Run `uvx --with=tox-uv tox` to ensure all checks pass
4. Submit a pull request

## License

MIT License - see LICENSE file for details.