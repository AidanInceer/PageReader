"""CLI argument parser for Vox.

This module handles command-line argument parsing, extracted from main.py
to support both GUI-first and CLI modes.
"""

import argparse
from typing import Final

# CLI commands that trigger CLI mode instead of GUI
CLI_COMMANDS: Final[set[str]] = {
    "read",
    "transcribe",
    "list",
    "list-sessions",
    "resume",
    "delete-session",
    "config",
}


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser for Vox CLI.

    Returns:
        Configured ArgumentParser with all subcommands.
    """
    parser = argparse.ArgumentParser(
        prog="vox",
        description="Vox - Bidirectional audio-text conversion for Windows 11",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--cli",
        action="store_true",
        help="Run in CLI mode instead of launching GUI",
    )

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 3.0.0",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Read command
    read_parser = subparsers.add_parser("read", help="Read web content aloud")
    read_parser.add_argument("--url", help="URL to read")
    read_parser.add_argument("--tab", action="store_true", help="Read from active browser tab")
    read_parser.add_argument("--file", dest="filepath", help="Read from local file")
    read_parser.add_argument("--voice", help="Voice model to use")
    read_parser.add_argument("--speed", type=float, default=1.0, help="Playback speed (0.5-2.0)")

    # Transcribe command
    transcribe_parser = subparsers.add_parser("transcribe", help="Transcribe audio to text")
    transcribe_parser.add_argument("--duration", type=int, help="Max recording duration in seconds")
    transcribe_parser.add_argument("--output", help="Save transcription to file")
    transcribe_parser.add_argument("--silence-stop", action="store_true", help="Auto-stop on silence")

    # List command
    list_parser = subparsers.add_parser("list", help="List available browser tabs")
    list_parser.add_argument("--browser", help="Filter by browser (chrome, edge, firefox)")
    list_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # List sessions command
    sessions_parser = subparsers.add_parser("list-sessions", help="List saved TTS sessions")
    sessions_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Resume command
    resume_parser = subparsers.add_parser("resume", help="Resume a saved TTS session")
    resume_parser.add_argument("session_id", help="Session ID to resume")

    # Delete session command
    delete_parser = subparsers.add_parser("delete-session", help="Delete a saved TTS session")
    delete_parser.add_argument("session_id", help="Session ID to delete")

    # Config command
    config_parser = subparsers.add_parser("config", help="View or modify configuration")
    config_parser.add_argument("--show", action="store_true", help="Show current config")
    config_parser.add_argument("--set", dest="set_value", help="Set config value (KEY=VALUE)")
    config_parser.add_argument("--reset", action="store_true", help="Reset to defaults")

    # GUI command (explicit)
    subparsers.add_parser("gui", help="Launch the GUI (default when no args)")

    return parser


def parse_args(args: list[str] | None = None) -> argparse.Namespace:
    """Parse command line arguments.

    Args:
        args: List of arguments to parse. If None, uses sys.argv.

    Returns:
        Parsed arguments namespace.
    """
    parser = create_parser()
    return parser.parse_args(args)
