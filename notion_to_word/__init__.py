"""Notion to Word Converter Package

A Python package for converting Notion pages to professionally formatted Word documents.
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .converter import NotionToWordConverter

def main():
    """Main entry point for the CLI."""
    from .cli import main as cli_main
    cli_main()

__all__ = ["NotionToWordConverter", "main"]