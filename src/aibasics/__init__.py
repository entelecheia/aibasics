"""Initialize the AI Basics package."""

import os

from ._version import __version__

# Read the package path from the current directory
__package_path__ = os.path.dirname(__file__)


def get_version() -> str:
    """Get the package version."""
    return __version__


__all__ = ["get_version", "open_homepage"]
