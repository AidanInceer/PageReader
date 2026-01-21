# Quickstart: App Modernization Development

**Feature**: 005-app-modernization  
**Date**: January 21, 2026

---

## Prerequisites

- Python 3.13+
- Windows 11
- Git

---

## Setup (5 minutes)

```powershell
# 1. Clone and checkout feature branch
git clone https://github.com/AidanInceer/vox.git
cd vox
git checkout 005-app-modernization

# 2. Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -e ".[dev]"

# 4. Verify installation
vox gui  # Should open the application
pytest tests/ -v --tb=short  # Should pass
```

---

## Key Files for This Feature

| File                    | Purpose                 | Action                     |
| ----------------------- | ----------------------- | -------------------------- |
| `src/ui/styles.py`      | Theme configuration     | Update to light theme      |
| `src/ui/main_window.py` | Main window (662 lines) | Split into components      |
| `src/main.py`           | Entry point (899 lines) | Extract CLI, add GUI-first |
| `src/ui/components/`    | NEW directory           | Create tab components      |
| `src/cli/`              | NEW directory           | Extract CLI commands       |
| `README.md`             | Project README          | Rewrite user-focused       |
| `docs/ARCHITECTURE.md`  | NEW file                | Engineering summary        |

---

## Development Workflow

### 1. Run Tests First

```powershell
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=term-missing

# Run specific test file
pytest tests/unit/test_ui_components.py -v
```

### 2. Code Quality Checks

```powershell
# Linting
ruff check src/

# Auto-fix linting issues
ruff check src/ --fix

# Type checking (optional)
mypy src/
```

### 3. Test UI Changes

```powershell
# Launch GUI in development
python -m src.main gui

# Or directly
vox gui
```

### 4. Build Executable

```powershell
# Build standalone .exe
pyinstaller vox.spec

# Output: dist/vox.exe
```

---

## Common Tasks

### Change Theme to Light Mode

```python
# src/ui/styles.py
THEME_NAME: Final[str] = "litera"  # Was "darkly"

COLORS: Final[dict[str, str]] = {
    "primary": "#4582ec",
    "background": "#ffffff",
    "foreground": "#333333",
    # ... update other colors
}
```

### Extract a UI Component

```python
# src/ui/components/status_tab.py
from typing import Callable, Optional
import ttkbootstrap as ttk

class StatusTab:
    def __init__(
        self,
        parent: ttk.Frame,
        on_action: Optional[Callable[[str, dict], None]] = None
    ):
        self._parent = parent
        self._on_action = on_action
        self._frame = self._build()

    def _build(self) -> ttk.Frame:
        frame = ttk.Frame(self._parent, padding=15)
        # ... build UI
        return frame

    @property
    def frame(self) -> ttk.Frame:
        return self._frame
```

### Extract a CLI Command

```python
# src/cli/commands.py
def command_read(args):
    """Read web content aloud."""
    # Move logic from main.py command_read()
    pass
```

---

## File Size Targets

After refactoring, all files should meet these limits:

| Metric                | Target | Check Command       |
| --------------------- | ------ | ------------------- |
| Lines per file        | < 300  | `wc -l src/**/*.py` |
| Lines per function    | < 30   | Manual review       |
| Cyclomatic complexity | < 10   | `radon cc src/ -a`  |

---

## Testing New Components

```python
# tests/unit/ui/components/test_status_tab.py
import pytest
from unittest.mock import Mock, MagicMock
import ttkbootstrap as ttk

from src.ui.components.status_tab import StatusTab

@pytest.fixture
def mock_parent():
    root = ttk.Window(themename="litera")
    frame = ttk.Frame(root)
    yield frame
    root.destroy()

def test_status_tab_creation(mock_parent):
    tab = StatusTab(mock_parent)
    assert tab.frame is not None
    assert tab.title == "Status"

def test_status_tab_update_state(mock_parent):
    tab = StatusTab(mock_parent)
    tab.update_state(AppState.RECORDING)
    # Assert state label updated
```

---

## Debugging Tips

### GUI Not Launching

```powershell
# Check for import errors
python -c "from src.ui.main_window import VoxMainWindow"

# Check ttkbootstrap
python -c "import ttkbootstrap; print(ttkbootstrap.__version__)"
```

### Threading Errors

```python
# Always use after() for cross-thread UI updates
self._root.after(0, lambda: self._update_label(text))
```

### Build Errors

```powershell
# Clean build artifacts
Remove-Item -Recurse -Force build/, dist/

# Rebuild
pyinstaller vox.spec --clean
```

---

## Useful Commands

```powershell
# Count lines in large files
Get-ChildItem -Path "src" -Recurse -File -Filter "*.py" |
    Select-Object FullName, @{Name="Lines";Expression={(Get-Content $_.FullName | Measure-Object -Line).Lines}} |
    Where-Object { $_.Lines -gt 300 } |
    Sort-Object Lines -Descending

# Find functions over 30 lines (approximate)
# Use IDE or manual review

# Check test coverage
pytest tests/ --cov=src --cov-report=html
# Open htmlcov/index.html
```

---

## Resources

- [ttkbootstrap Themes](https://ttkbootstrap.readthedocs.io/en/latest/themes/)
- [PyInstaller Docs](https://pyinstaller.org/en/stable/)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Feature Spec](spec.md)
- [Research Notes](research.md)
