"""Utilities for testing."""

from pathlib import Path
from typing import Union

from bs4 import BeautifulSoup


def read_as_html(filename: Union[Path, str]) -> BeautifulSoup:
    """Read a test file and parse it as HTML."""
    with open(filename) as file_handle:
        tree = BeautifulSoup(file_handle, "html.parser")
    return tree
