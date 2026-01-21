# CLI Contracts

**Feature**: 005-app-modernization  
**Date**: January 21, 2026

---

## Overview

CLI commands extracted from `main.py` into `src/cli/` module. The CLI remains available but is secondary to the GUI.

---

## Entry Point Behavior

```python
# src/main.py

def main():
    """
    Entry point behavior:
    1. No args → Launch GUI
    2. 'gui' arg → Launch GUI (explicit)
    3. CLI command → Run CLI
    """
    if len(sys.argv) == 1:
        # No arguments: launch GUI
        return launch_gui()

    command = sys.argv[1]
    if command == "gui":
        return launch_gui()
    elif command in CLI_COMMANDS:
        return run_cli()
    else:
        # Unknown command: show help
        print_help()
        return 1
```

---

## CLI Commands

### read

Read web content aloud using TTS.

```
vox read [OPTIONS]

Options:
  --url URL          URL to read
  --tab              Read from active browser tab
  --file PATH        Read from local file
  --voice VOICE      Voice model to use
  --speed SPEED      Playback speed (0.5-2.0)

Examples:
  vox read --url https://example.com
  vox read --tab
  vox read --file article.txt
```

### transcribe

Transcribe audio to text using STT.

```
vox transcribe [OPTIONS]

Options:
  --duration SECS    Max recording duration
  --output PATH      Save transcription to file
  --silence-stop     Auto-stop on silence

Examples:
  vox transcribe
  vox transcribe --duration 60 --output notes.txt
```

### list

List available browser tabs.

```
vox list [OPTIONS]

Options:
  --browser NAME     Filter by browser (chrome, edge, firefox)
  --json             Output as JSON

Examples:
  vox list
  vox list --browser chrome --json
```

### list-sessions

List saved TTS sessions.

```
vox list-sessions [OPTIONS]

Options:
  --json             Output as JSON

Examples:
  vox list-sessions
```

### resume

Resume a saved TTS session.

```
vox resume SESSION_ID

Arguments:
  SESSION_ID         Session ID to resume

Examples:
  vox resume abc123
```

### delete-session

Delete a saved TTS session.

```
vox delete-session SESSION_ID

Arguments:
  SESSION_ID         Session ID to delete

Examples:
  vox delete-session abc123
```

### config

View or modify configuration.

```
vox config [OPTIONS]

Options:
  --show             Show current config
  --set KEY=VALUE    Set config value
  --reset            Reset to defaults

Examples:
  vox config --show
  vox config --set hotkey="<ctrl>+<shift>+v"
```

### gui

Launch the GUI (explicit).

```
vox gui

Examples:
  vox gui
```

---

## Module Structure

```
src/cli/
├── __init__.py
├── parser.py       # Argument parsing (argparse setup)
└── commands.py     # Command implementations
```

### parser.py

```python
def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    pass

def parse_args(args: list[str] = None) -> argparse.Namespace:
    """Parse command line arguments."""
    pass

CLI_COMMANDS = {
    "read", "transcribe", "list", "list-sessions",
    "resume", "delete-session", "config", "gui"
}
```

### commands.py

```python
def command_read(args: argparse.Namespace) -> int:
    """Execute 'read' command. Returns exit code."""
    pass

def command_transcribe(args: argparse.Namespace) -> int:
    """Execute 'transcribe' command. Returns exit code."""
    pass

def command_list(args: argparse.Namespace) -> int:
    """Execute 'list' command. Returns exit code."""
    pass

def command_list_sessions(args: argparse.Namespace) -> int:
    """Execute 'list-sessions' command. Returns exit code."""
    pass

def command_resume(args: argparse.Namespace) -> int:
    """Execute 'resume' command. Returns exit code."""
    pass

def command_delete_session(args: argparse.Namespace) -> int:
    """Execute 'delete-session' command. Returns exit code."""
    pass

def command_config(args: argparse.Namespace) -> int:
    """Execute 'config' command. Returns exit code."""
    pass

def run_cli() -> int:
    """Main CLI entry point. Returns exit code."""
    pass
```

---

## Exit Codes

| Code | Meaning              |
| ---- | -------------------- |
| 0    | Success              |
| 1    | General error        |
| 2    | Invalid arguments    |
| 3    | Resource not found   |
| 4    | Permission denied    |
| 130  | Interrupted (Ctrl+C) |

---

## Output Formats

### Human-readable (default)

```
[*] Reading from https://example.com
[OK] Text extracted (1,234 words)
[*] Starting playback...
```

### JSON (--json flag)

```json
{
  "status": "success",
  "data": {
    "url": "https://example.com",
    "word_count": 1234
  }
}
```

---

## Error Handling

All commands follow this pattern:

```python
def command_example(args: argparse.Namespace) -> int:
    try:
        # Command logic
        return 0
    except UserError as e:
        print_error(str(e))
        return 1
    except KeyboardInterrupt:
        print_warning("Interrupted by user")
        return 130
    except Exception as e:
        logger.exception("Unexpected error")
        print_error(f"Unexpected error: {e}")
        return 1
```
