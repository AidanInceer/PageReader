"""CLI module for Vox command-line interface.

This module contains the argument parser and command implementations
extracted from main.py for better separation of concerns.
"""

from src.cli.parser import create_parser, parse_args

__all__ = ["create_parser", "parse_args"]
