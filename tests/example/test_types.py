"""Tests for basic types demonstrating common pytest patterns."""

import pytest
from pydantic import ValidationError

from src.example.types import Address, Block, Transaction


# 1. Parametrized test - run same test with different inputs
@pytest.mark.parametrize(
    "value,expected_valid",
    [
        (b"\x00" * 20, True),  # Valid 20-byte address
        (b"\x00" * 19, False),  # Too short
        (b"\x00" * 21, False),  # Too long
        (b"", False),  # Empty
    ],
)
def test_address_validation(value: bytes, expected_valid: bool):
    """Test address validation with various inputs."""
    if expected_valid:
        address = Address(value=value)
        assert len(address.value) == 20
    else:
        with pytest.raises(ValidationError):
            Address(value=value)


# 2. Regular test with simple assertions
def test_transaction_creation():
    """Test basic transaction creation."""
    tx = Transaction(
        nonce=0,
        gas_price=20_000_000_000,
        gas_limit=21_000,
        value=1_000_000_000_000_000_000,  # 1 ETH in wei
    )

    assert tx.nonce == 0
    assert tx.gas_price == 20_000_000_000
    assert tx.data == b""  # Default empty data
    assert tx.to is None  # Contract creation when to is None


# 3. Exception testing with pytest.raises
def test_transaction_validation_errors():
    """Test that invalid transactions raise appropriate errors."""
    # Test negative values are rejected
    with pytest.raises(ValidationError) as exc_info:
        Transaction(nonce=-1, gas_price=1, gas_limit=21_000, value=0)
    
    # Can also check the error details
    assert "greater than or equal to 0" in str(exc_info.value)
    
    # Test multiple validation errors
    with pytest.raises(ValidationError) as exc_info:
        Transaction(nonce=-1, gas_price=-100, gas_limit=-1, value=-50)
    
    errors = exc_info.value.errors()
    assert len(errors) == 4  # All fields have validation errors


# 4. Using fixtures (defined in conftest.py or here)
@pytest.fixture
def sample_block():
    """Fixture providing a sample block for tests."""
    return Block(
        number=100,
        parent_hash=b"\x11" * 32,
        gas_used=5_000_000,
        gas_limit=15_000_000,
    )


def test_block_with_fixture(sample_block):
    """Test using a fixture."""
    assert sample_block.number == 100
    assert len(sample_block.parent_hash) == 32
    assert sample_block.gas_used < sample_block.gas_limit


# 5. Slow test with marker (run with: pytest -m "not slow")
@pytest.mark.slow
def test_large_block_creation():
    """Test creating a block with many transactions (marked as slow)."""
    transactions = [
        Transaction(nonce=i, gas_price=1, gas_limit=21_000, value=i * 100)
        for i in range(1000)
    ]
    
    block = Block(
        number=1,
        parent_hash=b"\x00" * 32,
        transactions=transactions,
        gas_used=21_000_000,
        gas_limit=30_000_000,
    )
    
    assert len(block.transactions) == 1000
