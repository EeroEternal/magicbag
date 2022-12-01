"""Test versioneer."""
from magicbag._version import get_versions


def test_version():
    """Test version."""
    versions = get_versions()
    # print(f"versions:{versions}")
