"""Miscellaneous helper functions."""
from pathlib import Path
from platform import system
from subprocess import Popen


def browse_file_directory(filepath: Path):
    """Browse a file parent directory in OS file explorer."""
    # pylint: disable=no-name-in-module,import-outside-toplevel
    if system() == "Windows":
        from os import startfile

        startfile(filepath.parent)
    elif system() == "Darwin":
        Popen(["open", filepath.parent])
    else:
        Popen(["xdg-open", filepath.parent])
