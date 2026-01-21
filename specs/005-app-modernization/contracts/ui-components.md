# UI Component Contracts

**Feature**: 005-app-modernization  
**Date**: January 21, 2026

---

## Overview

This document defines the interfaces for the refactored UI components. Each component is extracted from `main_window.py` and follows the Single Responsibility Principle.

---

## Component Hierarchy

```
VoxApp (main.py)
└── VoxMainWindow (ui/main_window.py)
    ├── StatusTab (ui/components/status_tab.py)
    ├── SettingsTab (ui/components/settings_tab.py)
    ├── HistoryTab (ui/components/history_tab.py)
    ├── StatusBar (ui/components/status_bar.py)
    └── RecordingIndicator (ui/indicator.py)
```

---

## Interface: TabComponent (Base)

All tab components inherit from this abstract interface.

```python
from abc import ABC, abstractmethod
from typing import Callable, Optional
import ttkbootstrap as ttk

class TabComponent(ABC):
    """Base interface for notebook tab components."""

    @abstractmethod
    def __init__(
        self,
        parent: ttk.Frame,
        on_action: Optional[Callable[[str, dict], None]] = None
    ) -> None:
        """
        Initialize the tab component.

        Args:
            parent: Parent frame (notebook tab container)
            on_action: Callback for user actions (action_name, action_data)
        """
        pass

    @abstractmethod
    def build(self) -> ttk.Frame:
        """
        Build and return the tab's frame.

        Returns:
            Configured ttk.Frame ready to add to notebook
        """
        pass

    @abstractmethod
    def refresh(self) -> None:
        """Refresh the tab's content (e.g., reload data)."""
        pass

    @property
    @abstractmethod
    def title(self) -> str:
        """Tab title displayed in notebook."""
        pass
```

---

## Interface: StatusTab

Displays current application state and primary actions.

```python
class StatusTab(TabComponent):
    """
    Main status display showing:
    - Current state (Idle/Recording/Transcribing)
    - Active hotkey display
    - Manual record button
    - Quick instructions
    """

    def update_state(self, state: AppState) -> None:
        """
        Update displayed state.

        Args:
            state: New application state
        """
        pass

    def update_hotkey_display(self, hotkey: str) -> None:
        """
        Update the displayed hotkey combination.

        Args:
            hotkey: Hotkey string (e.g., "<ctrl>+<alt>+space")
        """
        pass

# Actions emitted via on_action:
# - ("record_toggle", {})  # User clicked record button
```

---

## Interface: SettingsTab

Configuration panel for user preferences.

```python
class SettingsTab(TabComponent):
    """
    Settings configuration:
    - Hotkey configuration with capture mode
    - Clipboard restore toggle
    - Minimize to tray toggle
    - Theme selection (future)
    """

    def start_hotkey_capture(self) -> None:
        """Enter hotkey capture mode."""
        pass

    def stop_hotkey_capture(self) -> None:
        """Exit hotkey capture mode."""
        pass

    def get_settings(self) -> dict:
        """
        Get current settings values.

        Returns:
            Dict with keys: hotkey, restore_clipboard, minimize_to_tray
        """
        pass

# Actions emitted via on_action:
# - ("save_settings", {"hotkey": str, "restore_clipboard": bool, ...})
# - ("capture_hotkey", {})
```

---

## Interface: HistoryTab

Transcription history display and management.

```python
class HistoryTab(TabComponent):
    """
    History management:
    - Scrollable list of past transcriptions
    - Copy to clipboard action per item
    - Delete individual items
    - Clear all history
    """

    def load_history(self, records: list[TranscriptionRecord]) -> None:
        """
        Load transcription records into display.

        Args:
            records: List of TranscriptionRecord objects
        """
        pass

    def clear_display(self) -> None:
        """Clear all displayed history items."""
        pass

# Actions emitted via on_action:
# - ("copy_transcription", {"id": int, "text": str})
# - ("delete_transcription", {"id": int})
# - ("clear_history", {})
# - ("refresh_history", {})
```

---

## Interface: StatusBar

Bottom status bar with state and version info.

```python
class StatusBar:
    """
    Status bar component:
    - Left: Current status message
    - Right: Version number
    """

    def __init__(self, parent: ttk.Frame) -> None:
        """Initialize status bar."""
        pass

    def build(self) -> ttk.Frame:
        """Build and return the status bar frame."""
        pass

    def set_message(self, message: str, style: str = "secondary") -> None:
        """
        Update status message.

        Args:
            message: Status text
            style: ttkbootstrap style (success, danger, warning, etc.)
        """
        pass

    def show_error(self, message: str, duration_ms: int = 5000) -> None:
        """
        Show temporary error message.

        Args:
            message: Error text
            duration_ms: Time before reverting to normal
        """
        pass
```

---

## Interface: RecordingIndicator

Floating overlay for recording feedback.

```python
class RecordingIndicator:
    """
    Translucent floating indicator:
    - Shows above taskbar
    - State-dependent colors and text
    - Thread-safe for background updates
    """

    def show(self, state: IndicatorState = "recording") -> None:
        """
        Show indicator with given state.
        Thread-safe: can be called from any thread.

        Args:
            state: "recording" | "processing" | "success" | "error"
        """
        pass

    def hide(self) -> None:
        """Hide the indicator. Thread-safe."""
        pass

    def update_state(self, state: IndicatorState) -> None:
        """Update state without hiding. Thread-safe."""
        pass

    def set_main_root(self, root: tk.Tk) -> None:
        """Set main window root for thread-safe scheduling."""
        pass

    def destroy(self) -> None:
        """Cleanup resources on application exit."""
        pass
```

---

## Interface: VoxMainWindow (Refactored)

Slim coordinator that composes tab components.

```python
class VoxMainWindow:
    """
    Main window coordinator:
    - Creates and manages tab components
    - Routes actions to controller
    - Handles window lifecycle
    """

    def __init__(
        self,
        controller: VoiceInputController,
        database: VoxDatabase,
        on_close_callback: Optional[Callable[[], None]] = None
    ) -> None:
        """Initialize main window with dependencies."""
        pass

    def run(self) -> None:
        """Start the main event loop."""
        pass

    def on_close(self) -> None:
        """Handle window close (minimize to tray or exit)."""
        pass

    def show(self) -> None:
        """Show the window (restore from tray)."""
        pass

    def refresh_history(self) -> None:
        """Reload history from database."""
        pass

    # Internal action routing
    def _handle_tab_action(self, action: str, data: dict) -> None:
        """Route tab actions to appropriate handlers."""
        pass
```

---

## Thread Safety Contract

All UI updates from background threads **MUST** use the main thread scheduler:

```python
# ❌ WRONG - Will crash
def background_callback():
    label.configure(text="Updated")

# ✅ CORRECT - Thread-safe
def background_callback():
    root.after(0, lambda: label.configure(text="Updated"))
```

Components that receive background updates:

- `RecordingIndicator` - Has internal thread-safe scheduling
- `StatusTab` - Must receive updates via `root.after()`
- `StatusBar` - Must receive updates via `root.after()`

---

## Dependency Injection

All components receive dependencies via constructor:

```python
# ✅ CORRECT - Dependencies injected
class HistoryTab(TabComponent):
    def __init__(self, parent, on_action, database: VoxDatabase):
        self._database = database

# ❌ WRONG - Global import
class HistoryTab(TabComponent):
    def __init__(self, parent, on_action):
        from src.persistence.database import get_database
        self._database = get_database()
```

This enables testing with mocks and follows Dependency Inversion Principle.
