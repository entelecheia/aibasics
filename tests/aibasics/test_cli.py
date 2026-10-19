"""
test cli module
"""

import subprocess

from aibasics import get_version


def test_cli() -> None:
    """The installed entry point prints the version."""
    proc = subprocess.run(["aibasics"], capture_output=True, text=True, check=False)
    assert proc.returncode == 0
    assert proc.stdout.strip() == f"aibasics {get_version()}"
