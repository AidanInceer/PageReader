# Tasks: App Modernization

**Feature**: 005-app-modernization  
**Generated**: January 21, 2026  
**Total Tasks**: 52

---

## Phase 1: Setup

Initial project configuration and directory structure.

> **Test-First Note**: Per constitution, write failing tests before implementing each task. Test files should be created alongside or before implementation code.

- [x] T001 Add pystray dependency to pyproject.toml in [project.dependencies]
- [x] T002 Create src/cli/ directory with **init**.py
- [x] T003 Create src/ui/components/ directory with **init**.py
- [x] T004 Create src/ui/mixins/ directory with **init**.py
- [x] T005 Verify all dependencies install with `pip install -e ".[dev]"`

---

## Phase 2: Foundational

Blocking prerequisites that must complete before user stories.

- [x] T006 Create BaseComponent mixin class in src/ui/mixins/base_component.py with validation_mixin and state_management helpers
- [x] T007 Create TabComponent protocol/interface in src/ui/components/base.py defining frame property and action callback
- [x] T008 [P] Create event constants module src/ui/events.py with UI_EVENTS dict for standardized event names

---

## Phase 3: User Story 1 - Download & Run Executable (P1)

**Goal**: Users can download and run Vox as a standalone Windows application without Python.

**Independent Test Criteria**:

- Running `vox.exe` (no args) launches GUI
- Running `vox.exe --cli read --url <url>` runs CLI command
- System tray icon appears when GUI launches
- Minimize to tray works
- Restore from tray works

### Implementation Tasks

- [x] T009 [US1] Update src/main.py to make GUI the default entry point (no args = GUI, `--cli` flag for CLI commands)
- [x] T010 [US1] Create src/ui/system_tray.py with SystemTrayManager class using pystray
- [x] T011 [US1] Implement SystemTrayManager.create_icon() method returning pystray.Icon in src/ui/system_tray.py
- [x] T012 [US1] Implement SystemTrayManager.create_menu() method with Show/Hide/Exit options in src/ui/system_tray.py
- [x] T013 [US1] Implement minimize-to-tray on window close (hide window, show tray) in src/ui/system_tray.py
- [x] T014 [US1] Implement restore-from-tray on tray click (show window, optionally hide tray) in src/ui/system_tray.py
- [x] T015 [US1] Integrate SystemTrayManager into VoxMainWindow.**init**() in src/ui/main_window.py
- [x] T016 [US1] Update vox.spec to set console=False for GUI-first windowed executable
- [x] T017 [US1] Add Vox icon asset to build/resources/vox.ico for executable and tray
- [x] T018 [US1] Update vox.spec to include icon path and all required hidden imports
- [ ] T019 [US1] Test executable build with `pyinstaller vox.spec` and verify GUI launch
- [ ] T020 [US1] Test CLI mode with `dist/vox.exe --cli read --help` works correctly
- [ ] T020a [US1] Create first-run model download dialog with progress indicator in src/ui/first_run.py
- [ ] T020b [US1] Add tray behavior toggle (minimize vs exit) to Settings tab

---

## Phase 4: User Story 2 - Light Mode UI (P1)

**Goal**: Application uses a modern, professional light theme with consistent colors.

**Independent Test Criteria**:

- App launches with white/light gray background
- All text is dark and readable
- Primary accent color is blue (#4582ec)
- Recording indicator is clearly visible on light backgrounds
- No visual glitches or unthemed elements

### Implementation Tasks

- [x] T021 [US2] Update THEME_NAME from "darkly" to "litera" in src/ui/styles.py
- [x] T021a [US2] Configure "Segoe UI Variable" font family in styles.py FONT_FAMILY constant
- [x] T022 [US2] Update COLORS dict with light-mode palette (background=#ffffff, foreground=#333333, primary=#4582ec) in src/ui/styles.py
- [x] T023 [US2] Update recording indicator colors for visibility on light backgrounds in src/ui/indicator.py
- [x] T024 [US2] Update StatusTab visual styling for light theme consistency in src/ui/main_window.py
- [x] T025 [US2] Update SettingsTab visual styling for light theme consistency in src/ui/main_window.py
- [x] T026 [US2] Update HistoryTab visual styling for light theme consistency in src/ui/main_window.py
- [x] T027 [US2] Update StatusBar colors for light theme in src/ui/main_window.py
- [x] T028 [US2] Visual QA: Launch app and verify all components render correctly in light mode

---

## Phase 5: User Story 3 - Simplified Codebase & Interface (P2)

**Goal**: Codebase follows SOLID principles with no file exceeding 300 lines.

**Independent Test Criteria**:

- All refactored files pass existing tests
- No file in src/ exceeds 300 lines
- Each extracted component works independently
- GUI launches and all features work after refactoring

### Refactoring Tasks

- [ ] T029 [US3] Extract StatusTab class from main_window.py to src/ui/components/status_tab.py (~120 lines)
- [ ] T030 [US3] Extract SettingsTab class from main_window.py to src/ui/components/settings_tab.py (~150 lines)
- [ ] T031 [US3] Extract HistoryTab class from main_window.py to src/ui/components/history_tab.py (~100 lines)
- [ ] T032 [US3] Extract StatusBar class from main_window.py to src/ui/components/status_bar.py (~50 lines)
- [ ] T033 [US3] Update main_window.py imports to use extracted components, reduce to <300 lines
- [ ] T034 [P] [US3] Extract argument parser from main.py to src/cli/parser.py (~100 lines)
- [ ] T035 [P] [US3] Extract CLI command implementations from main.py to src/cli/commands.py (~200 lines)
- [ ] T036 [US3] Update main.py to import from src/cli/, reduce to <300 lines
- [ ] T037 [US3] Extract TTS engine logic from tts/controller.py to tts/engine_manager.py if over 300 lines
- [ ] T038 [US3] Verify session/manager.py under 300 lines or split into session/state.py and session/persistence.py
- [ ] T039 [US3] Verify stt/ui.py under 300 lines or extract transcription display to stt/display.py
- [ ] T040 [US3] Run full test suite to verify refactoring preserves functionality

---

## Phase 6: User Story 4 - User-Focused README (P2)

**Goal**: README is sleek, user-focused with clear download/install instructions.

**Independent Test Criteria**:

- README has hero section with tagline
- Download button/link is prominent
- Quick start shows 3 steps or fewer
- Feature list is scannable (bullets or icons)
- No developer/contribution content above fold

### Documentation Tasks

- [ ] T041 [US4] Create README hero section with Vox tagline and brief description in README.md
- [ ] T042 [US4] Add download section with link to releases/executable in README.md
- [ ] T043 [US4] Add quick start section (download, run, use) in README.md
- [ ] T044 [US4] Add features section with bullet list of capabilities in README.md
- [ ] T045 [US4] Add keyboard shortcuts reference section in README.md
- [ ] T046 [US4] Move developer/contribution content to CONTRIBUTING.md (new file)
- [ ] T047 [US4] Add screenshot or GIF of app in action to README.md (placeholder path: imgs/screenshot.png)

---

## Phase 7: User Story 5 - Engineering Documentation (P3)

**Goal**: Engineering team has concise architecture overview.

**Independent Test Criteria**:

- ARCHITECTURE.md exists in docs/
- Contains component diagram (mermaid or ASCII)
- Documents data flow for TTS and STT pipelines
- Lists key modules with single-sentence descriptions

### Documentation Tasks

- [ ] T048 [US5] Create docs/ARCHITECTURE.md with overview section
- [ ] T049 [US5] Add component diagram showing module relationships in docs/ARCHITECTURE.md
- [ ] T050 [US5] Document TTS pipeline flow (content fetch → chunking → synthesis → playback) in docs/ARCHITECTURE.md
- [ ] T051 [US5] Document STT pipeline flow (record → transcribe → paste) in docs/ARCHITECTURE.md
- [ ] T052 [US5] Add module reference table with single-line descriptions in docs/ARCHITECTURE.md

---

## Phase 8: Polish & Cross-Cutting Concerns

Final validation and cleanup.

- [ ] T053 Run ruff check src/ and fix all linting errors
- [ ] T054 Run pytest tests/ --cov=src and verify >80% coverage maintained
- [ ] T055 Verify all files under 300 lines with line count check
- [ ] T056 Final executable build and smoke test (GUI launch, TTS, STT, tray)
- [ ] T057 Update CHANGELOG.md with modernization release notes

---

## Dependency Graph

```
Phase 1 (Setup)
    │
    ▼
Phase 2 (Foundational)
    │
    ├──────────────────────────────────────────┐
    │                                          │
    ▼                                          ▼
Phase 3 (US1: Executable)              Phase 4 (US2: Light Mode)
    │                                          │
    └──────────────┬───────────────────────────┘
                   │
                   ▼
           Phase 5 (US3: Refactoring)
                   │
    ┌──────────────┼──────────────┐
    │              │              │
    ▼              ▼              ▼
Phase 6        Phase 7        Phase 8
(US4: README)  (US5: Docs)    (Polish)
```

**Notes**:

- US1 and US2 can be done in parallel (different concerns)
- US3 (refactoring) should wait until US1 and US2 styling is finalized
- US4 and US5 can be done in parallel and at any time after US1
- Phase 8 must be last

---

## Parallel Execution Examples

### Within Phase 3 (US1):

```
T010 (system_tray.py) ─┬─► T015 (integrate into main_window)
T011 (create_icon)    ─┤
T012 (create_menu)    ─┤
T013 (minimize)       ─┘
                         │
T016 (vox.spec) ─────────┴──► T019 (build test)
T017 (icon asset) ───────────┘
```

### Within Phase 5 (US3):

```
T029 (StatusTab)    ─┬─► T033 (update main_window imports)
T030 (SettingsTab)  ─┤
T031 (HistoryTab)   ─┤
T032 (StatusBar)    ─┘

T034 (parser.py)    ─┬─► T036 (update main.py)
T035 (commands.py)  ─┘
```

---

## Implementation Strategy

### MVP Scope (Recommended First Milestone)

Complete User Story 1 (Executable) + User Story 2 (Light Mode) for a functional, distributable app:

- Tasks T001-T028
- Result: Users can download and run a light-themed GUI app

### Incremental Delivery

1. **Sprint 1**: US1 + US2 (core user experience)
2. **Sprint 2**: US3 (technical debt reduction)
3. **Sprint 3**: US4 + US5 (documentation)
4. **Sprint 4**: Polish and release

---

## File Targets Summary

| File                      | Current | Target | Action                  |
| ------------------------- | ------- | ------ | ----------------------- |
| main.py                   | 899     | <300   | Extract CLI to src/cli/ |
| main_window.py            | 662     | <300   | Extract components      |
| session/manager.py        | 409     | <300   | Split if needed         |
| stt/ui.py                 | 393     | <300   | Extract display         |
| indicator.py              | 359     | <300   | Simplify                |
| voice_input/controller.py | 347     | <300   | Extract helpers         |
| persistence/database.py   | 321     | <300   | Minor cleanup           |
| tts/controller.py         | 304     | <300   | Extract engine mgr      |

---

## Validation Checklist

After completing all tasks:

- [ ] `vox.exe` (no args) launches GUI with light theme
- [ ] `vox.exe --cli read --url <url>` reads content aloud
- [ ] System tray appears, minimize/restore works
- [ ] All files in src/ are ≤300 lines
- [ ] Test coverage remains >80%
- [ ] README is user-focused with download instructions
- [ ] docs/ARCHITECTURE.md exists with diagrams
- [ ] No ruff linting errors
