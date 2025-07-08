"""Pytest configuration and shared fixtures."""

import pytest


@pytest.fixture
def example_fixture():
    """Example fixture for tests."""
    return {"test": "data"}
