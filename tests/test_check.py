"""Test prefix check."""

import pytest

from magicbag import prefix_check


@pytest.mark.parametrize(
    "content, prefix",
    [
        ("int(10)", ("int", "decimal")),
        ("decimal(10,5)", ("int", "decimal")),
    ],
)
def test_check_match(content, prefix):
    """Test prefix check.
        Args:
            content (str): source string
            prefix (tuple): prefix tuple list
        Returns:
            bool: True if string start with, otherwise False
    """
    result = prefix_check(content, prefix)
    assert result[0] is True
    assert result[1] in prefix


@pytest.mark.parametrize(
    "content, prefix",
    [
        ("string", ("int", "decimal")),
        ("float", ("int", "decimal")),
    ],
)
def test_check_not(content, prefix):
    """Test prefix check not match.
        Args:
            content (str): source string
            prefix (tuple): prefix tuple list
        Returns:
            bool: True if string start with, otherwise False
    """
    result = prefix_check(content, prefix)
    assert result[0] is False
    assert result[1] is None
