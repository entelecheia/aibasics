import os

from hyfi import HyFI

from ._version import __version__

# Read the package path from the current directory
__package_path__ = os.path.dirname(__file__)

# Initialize the global HyFI object
HyFI.initialize_global_hyfi(
    package_path=__package_path__,
    version=__version__,
    plugins=[],
)

# Initialize the logger
HyFI.setLogger()


def get_version() -> str:
    """Get the package version."""
    return __version__


__all__ = ["HyFI", "get_version"]
