"""Example validation function for specifications."""

from .types import Block


def validate_block_gas(block: Block) -> bool:
    """Validate that block gas usage doesn't exceed limit.

    Args:
        block: Block to validate.

    Returns:
        bool: True if gas usage is valid.
    """
    return block.gas_used <= block.gas_limit
