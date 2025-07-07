"""Tests for validation function."""

from src.example.types import Block
from src.example.validation import validate_block_gas


def test_validate_block_gas():
    """Test block gas validation."""
    # Valid block - gas used within limit
    valid_block = Block(
        number=1,
        parent_hash=b"\x00" * 32,
        gas_used=1_000_000,
        gas_limit=15_000_000,
    )
    assert validate_block_gas(valid_block) is True

    # Invalid block - gas used exceeds limit
    invalid_block = Block(
        number=1,
        parent_hash=b"\x00" * 32,
        gas_used=15_000_001,
        gas_limit=15_000_000,
    )
    assert validate_block_gas(invalid_block) is False
