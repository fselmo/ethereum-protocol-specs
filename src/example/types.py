"""Example types using Pydantic for Ethereum data structures."""

from pydantic import BaseModel, Field


class Address(BaseModel):
    """Ethereum address (20 bytes)."""

    value: bytes = Field(..., min_length=20, max_length=20)


class Transaction(BaseModel):
    """Simple transaction model."""

    nonce: int = Field(..., ge=0)
    gas_price: int = Field(..., ge=0)
    gas_limit: int = Field(..., ge=0)
    to: Address | None = None
    value: int = Field(..., ge=0)
    data: bytes = Field(default=b"")


class Block(BaseModel):
    """Simple block model."""

    number: int = Field(..., ge=0)
    parent_hash: bytes = Field(..., min_length=32, max_length=32)
    transactions: list[Transaction] = Field(default_factory=list)
    gas_used: int = Field(..., ge=0)
    gas_limit: int = Field(..., ge=0)
