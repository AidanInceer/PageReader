# Implementation Plan: App Modernization & Polish

**Branch**: `005-app-modernization` | **Date**: January 21, 2026 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/005-app-modernization/spec.md`

---

## Summary

Transform Vox from a CLI-centric application to a polished, user-focused Windows desktop app with:

1. Single executable distribution (no Python required)
2. Modern light-mode UI using ttkbootstrap "litera" theme
3. Refactored codebase following SOLID principles (<300 lines/file, <30 lines/function)
4. User-focused README with visual media
5. Engineering architecture documentation

---

## Technical Context

**Language/Version**: Python 3.13  
**Primary Dependencies**:

- ttkbootstrap (UI theming)
- piper-tts (text-to-speech)
- faster-whisper (speech-to-text)
- PyInstaller (executable bundling)
- pynput (global hotkeys)
- pyperclip (clipboard operations)

**Storage**: SQLite database (via src/persistence/database.py)  
**Testing**: pytest with >80% coverage requirement  
**Target Platform**: Windows 11 (desktop application)  
**Project Type**: Desktop GUI application with optional CLI  
**Performance Goals**: <5 second startup, <200MB executable size  
**Constraints**: Must bundle Piper TTS models and Whisper models

**Current Code Metrics (files exceeding 300 lines):**
| File | Lines | Refactoring Needed |
|------|-------|-------------------|
| src/main.py | 899 | Extract CLI commands to separate modules |
| src/ui/main_window.py | 662 | Split into tab-specific components |
| src/session/manager.py | 409 | Extract session CRUD operations |
| src/stt/ui.py | 393 | Extract dialog components |
| src/ui/indicator.py | 359 | Simplify state management |
| src/voice_input/controller.py | 347 | Extract recording/transcription logic |
| src/persistence/database.py | 321 | Split into repository classes |
| src/tts/controller.py | 304 | Extract playback coordination |

---

## Constitution Check

_GATE: Must pass before Phase 0 research. Re-check after Phase 1 design._

| Principle              | Status    | Notes                                     |
| ---------------------- | --------- | ----------------------------------------- |
| Test-First Development | ✅ PASS   | Will write tests before refactoring       |
| Clear API Contracts    | ✅ PASS   | Refactoring will improve contracts        |
| Semantic Versioning    | ✅ PASS   | This is a MINOR release (non-breaking)    |
| Simplicity & Clarity   | ✅ PASS   | Reducing file sizes improves clarity      |
| 80% Test Coverage      | ⚠️ CHECK  | Must maintain coverage during refactoring |
| SOLID Principles       | ✅ TARGET | Primary goal of this feature              |
| DRY                    | ✅ TARGET | Will consolidate duplicate patterns       |
| KISS                   | ✅ TARGET | Simplifying UI and code structure         |
| Import Organization    | ✅ PASS   | Will enforce via ruff                     |

**Gate Status**: ✅ PASSED - No violations requiring justification

---

## Project Structure

### Documentation (this feature)

```text
specs/005-app-modernization/
├── plan.md              # This file
├── research.md          # Phase 0: Technical research
├── data-model.md        # Phase 1: Data models (minimal changes)
├── quickstart.md        # Phase 1: Developer quickstart
├── contracts/           # Phase 1: API contracts
│   └── ui-components.md # UI component interfaces
└── tasks.md             # Phase 2: Implementation tasks
```

### Source Code (refactored structure)

```text
src/
├── __init__.py
├── config.py                    # App configuration
├── main.py                      # Entry point (GUI-first, CLI optional)
│
├── ui/                          # UI Layer (refactored)
│   ├── __init__.py
│   ├── app.py                   # Main application class
│   ├── styles.py                # Theme configuration (light mode)
│   ├── main_window.py           # Main window (slim coordinator)
│   ├── components/              # NEW: Reusable UI components
│   │   ├── __init__.py
│   │   ├── status_tab.py        # Status tab component
│   │   ├── settings_tab.py      # Settings tab component
│   │   ├── history_tab.py       # History tab component
│   │   └── status_bar.py        # Status bar component
│   └── indicator.py             # Recording indicator overlay
│
├── cli/                         # NEW: CLI layer (extracted from main.py)
│   ├── __init__.py
│   ├── commands.py              # CLI command implementations
│   └── parser.py                # Argument parsing
│
├── voice_input/                 # Voice input orchestration
│   ├── __init__.py
│   ├── controller.py            # Slim coordinator
│   ├── recording.py             # NEW: Recording logic
│   └── transcription.py         # NEW: Transcription logic
│
├── tts/                         # Text-to-speech
│   ├── __init__.py
│   ├── controller.py            # Playback coordination
│   ├── synthesizer.py           # Piper synthesis
│   ├── playback.py              # Audio playback
│   ├── chunking.py              # Text chunking
│   └── piper_provider.py        # Piper model management
│
├── stt/                         # Speech-to-text
│   ├── __init__.py
│   ├── engine.py                # Whisper engine
│   ├── recorder.py              # Audio recording
│   ├── transcriber.py           # Transcription processing
│   ├── audio_utils.py           # Audio utilities
│   └── ui.py                    # STT-specific dialogs
│
├── persistence/                 # Data layer
│   ├── __init__.py
│   ├── database.py              # Database connection
│   ├── models.py                # Data models
│   └── repositories/            # NEW: Repository pattern
│       ├── __init__.py
│       ├── settings_repo.py     # Settings repository
│       └── history_repo.py      # History repository
│
├── browser/                     # Browser integration
├── extraction/                  # Content extraction
├── session/                     # Session management
├── hotkey/                      # Hotkey management
├── clipboard/                   # Clipboard operations
└── utils/                       # Shared utilities

tests/
├── unit/
│   ├── ui/
│   │   └── components/          # NEW: Component tests
│   ├── cli/                     # NEW: CLI tests
│   └── ...
├── integration/
└── contract/
```

**Structure Decision**: Refactoring existing single-project structure by:

1. Extracting UI components from monolithic main_window.py
2. Extracting CLI commands from main.py
3. Adding repository pattern for persistence
4. Splitting voice_input controller logic

---

## Complexity Tracking

No constitution violations requiring justification. All changes simplify the codebase.

---

## Phase Summary

| Phase   | Deliverable                              | Status      |
| ------- | ---------------------------------------- | ----------- |
| Phase 0 | research.md                              | ✅ Complete |
| Phase 1 | data-model.md, contracts/, quickstart.md | ✅ Complete |
| Phase 2 | tasks.md (via /speckit.tasks)            | ⏳ Pending  |
