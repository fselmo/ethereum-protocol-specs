# Working with Ethereum Specifications

This document provides context for AI assistants working on this Ethereum specifications repository.

## Repository Overview

This is a Python repository for writing Ethereum protocol specifications using modern tooling and best practices. The specifications use Pydantic models for type safety and automatic validation.

## Key Directories

- `src/specs/` - Main protocol specifications (core types, validation rules, state transitions)
- `src/subspecs/` - Sub-specifications like EIPs that extend or modify the main specs
- `src/example/` - Reference implementations showing how to use Pydantic models and write tests (not packaged)
- `tests/` - Test suite mirroring the src structure
- `docs/` - MkDocs documentation source

## Development Workflow

### Running Tests
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/specs/test_types.py

# Run with coverage
uv run pytest --cov

# Run any python via uv
uv run python
```

### Code Quality Checks
```bash
# Format code
uv run ruff format src tests

# Check linting
uv run ruff check src tests

# Type checking
uv run mypy src tests

# Run all checks via tox
uvx --with=tox-uv tox
```

### Common Tasks

1. **Adding a new type**: Create it in using appropriate Pydantic models or BaseModel
2. **Adding to specs**: Located in `src/specs`
2. **Adding to subspecs**: Located in `src/subspecs/`
4. **Writing tests**: Mirror the source structure in `tests/`

## Important Patterns

### Pydantic Models
```python
from pydantic import BaseModel, Field

class Transaction(BaseModel):
    nonce: int = Field(...)

    # ... extend model 
```

### Test Patterns
- Use `pytest.mark.parametrize` for testing multiple inputs
- Use `pytest.raises(ValidationError)` for testing validation errors
- Create fixtures in `conftest.py` or test files
- Use `@pytest.mark.slow` for long-running tests

## Code Style

- Line length: 99 characters (ruff configured)
- Use type hints everywhere
- Follow Google docstring style
- No docstrings needed for `__init__` methods
- Imports are automatically sorted by ruff

## Testing Philosophy

- Tests should be simple and clear
- Test file names must start with `test_`
- Test function names must start with `test_`
- Use descriptive test names that explain what's being tested

## Common Commands Reference

| Task | Command |
|------|---------|
| Install dependencies | `uv sync --all-extras` |
| Run tests | `uv run pytest` |
| Format code | `uv run ruff format src tests` |
| Lint code | `uv run ruff check src tests` |
| Type check | `uv run mypy src tests` |
| Run all checks | `uvx --with=tox-uv tox` |
| Build docs | `uv run mkdocs build` |
| Serve docs | `uv run mkdocs serve` |

## Working with Git

- Pre-commit hooks are installed via `uvx pre-commit install`
- To skip hooks once: `git commit --no-verify`
- PR template asks for: what was wrong, how it was fixed, and a cute animal picture

## Important Notes

1. This repository uses Python 3.12+ features
2. All models should use Pydantic for automatic validation
3. The `example/` directory is for reference only and not included in builds
4. Keep things simple - many users are not Python experts

## Debugging Tips

- If imports fail, check that you're using relative imports correctly
- If mypy fails, ensure all directories have `py.typed` files
- If tests fail to discover, ensure test files/functions start with `test_`
- Coverage reports are generated in `htmlcov/` directory