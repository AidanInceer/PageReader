# Research: App Modernization & Polish

**Feature**: 005-app-modernization  
**Date**: January 21, 2026  
**Status**: Complete

---

## Research Tasks

### 1. Light Mode Theme Selection (ttkbootstrap)

**Question**: Which ttkbootstrap theme best matches Windows 11 native look?

**Research**:

- ttkbootstrap offers several light themes: litera, flatly, cosmo, journal, lumen, minty, pulse, sandstone, united, yeti
- "litera" is the most Windows 11-like: clean, professional, minimal color accents
- "flatly" is a close second: slightly more colorful but still modern

**Decision**: Use "litera" theme
**Rationale**:

- Clean white/light gray backgrounds match Windows 11 aesthetic
- Subtle blue accent color for primary actions
- Professional appearance without visual clutter
- Good contrast ratios (WCAG AA compliant)

**Alternatives considered**:

- "flatly": Slightly more colorful, felt less native to Windows 11
- "cosmo": Too much visual weight in headers
- Custom theme: Unnecessary complexity for this iteration

---

### 2. PyInstaller Bundling Strategy

**Question**: How to bundle Piper TTS and Whisper models without excessive file size?

**Research**:

- Current vox.spec already includes `collect_data_files('piper_tts')`
- faster-whisper models are downloaded on first use (~150MB for small model)
- Piper TTS models are ~30MB each
- Total executable size: ~100-150MB without models, ~300-400MB with bundled models

**Decision**: Bundle minimal models, download larger models on first use
**Rationale**:

- Keeps initial download size reasonable (<150MB)
- Users who need high-quality models can download them
- Matches pattern used by other voice apps (e.g., Whisper desktop apps)

**Implementation**:

1. Bundle piper-tts core library (no models)
2. Bundle faster-whisper core library (no models)
3. First-run wizard downloads default models to user's AppData folder
4. Add progress indicator for model downloads

**Alternatives considered**:

- Bundle all models: Would create 500MB+ executable
- No bundled models: Would require immediate download, poor first experience

---

### 3. GUI-First Entry Point

**Question**: How to make the app launch GUI by default instead of CLI?

**Research**:

- Current main.py has `gui` as a subcommand
- Users expect double-clicking .exe to open GUI
- CLI mode should still be available for power users

**Decision**: GUI launches by default, CLI via `--cli` flag
**Rationale**:

- Double-click = GUI (expected behavior)
- `vox --cli read --url ...` for CLI mode
- Backwards-compatible: old CLI commands still work with `--cli` prefix

**Implementation**:

```python
def main():
    if len(sys.argv) == 1 or (len(sys.argv) > 1 and sys.argv[1] not in CLI_COMMANDS):
        # No args or first arg is not a CLI command -> launch GUI
        launch_gui()
    else:
        # CLI mode
        run_cli()
```

**Alternatives considered**:

- Separate executables (vox.exe, vox-cli.exe): Adds complexity
- Keep CLI-first: Poor user experience for desktop app

---

### 4. System Tray Integration

**Question**: How to minimize to system tray on Windows 11?

**Research**:

- pystray library is the standard for system tray icons
- tkinter/ttkbootstrap doesn't have native tray support
- Need to handle: minimize to tray, restore from tray, right-click menu

**Decision**: Use pystray for system tray integration
**Rationale**:

- Well-maintained library with Windows support
- Supports custom icons, menus, and notifications
- Integrates well with tkinter mainloop

**Implementation**:

1. Add `pystray` and `Pillow` (for icon) to dependencies
2. Create tray icon with menu: Show, Start Recording, Exit
3. Window close minimizes to tray (configurable)
4. Double-click tray icon restores window

**Alternatives considered**:

- No system tray: Hotkey-only operation is awkward
- Custom Win32 implementation: Too complex, pystray handles edge cases

---

### 5. Code Refactoring Strategy

**Question**: How to split large files while maintaining functionality?

**Research**:

- main.py (899 lines): Contains CLI commands inline
- main_window.py (662 lines): Contains all tab UIs inline
- SOLID principle: Single Responsibility = one reason to change

**Decision**: Extract by responsibility, not by size
**Rationale**:

- CLI commands → src/cli/commands.py (each command is ~50-100 lines)
- Tab UIs → src/ui/components/{status,settings,history}\_tab.py
- Database operations → src/persistence/repositories/

**Refactoring sequence**:

1. Extract CLI (lowest risk, most isolated)
2. Extract UI components (medium risk, clear boundaries)
3. Extract repositories (highest risk, touches data layer)
4. Update main.py to be slim entry point

**Alternatives considered**:

- Big-bang refactor: High risk of breaking changes
- No refactoring: Doesn't meet spec requirements

---

### 6. Light Theme Color Palette

**Question**: What colors should be used for the light theme?

**Research**:

- Windows 11 uses: White backgrounds, #1a1a1a text, #0067c0 accent
- ttkbootstrap "litera" uses: #ffffff bg, #333333 text, #4582ec primary
- WCAG AA requires 4.5:1 contrast for normal text

**Decision**: Use ttkbootstrap litera defaults with minor adjustments
**Rationale**:

- Litera palette already meets accessibility requirements
- Minor tweaks for recording indicator (red) and success states (green)

**Color Palette**:

```python
COLORS = {
    "primary": "#4582ec",      # Blue (actions)
    "secondary": "#6c757d",    # Gray (secondary actions)
    "success": "#02b875",      # Green (success states)
    "info": "#17a2b8",         # Cyan (informational)
    "warning": "#f0ad4e",      # Orange (warnings)
    "danger": "#d9534f",       # Red (errors, recording)
    "background": "#ffffff",   # White (main bg)
    "surface": "#f8f9fa",      # Light gray (cards, panels)
    "foreground": "#333333",   # Dark gray (text)
    "muted": "#6c757d",        # Gray (secondary text)
}
```

---

### 7. README Structure for User Focus

**Question**: What structure makes the README compelling for users?

**Research**:

- Best open-source READMEs: hero image/GIF, one-line description, features, install, usage
- Anti-patterns: Technical jargon first, contribution guidelines prominent, no visuals

**Decision**: Hero-first structure with visual emphasis
**Rationale**:

- Users decide in 5 seconds if they're interested
- Visual demo > text description
- Installation should be one step (download exe)

**Structure**:

1. Logo + tagline (10 words max)
2. Hero GIF showing app in action
3. One-paragraph description
4. Download button (prominent)
5. Feature highlights (with icons)
6. Quick start (3 steps max)
7. Screenshots gallery
8. FAQ (common questions)
9. Footer: License, Credits, Contributing link

---

### 8. Engineering Documentation Scope

**Question**: What should the engineering summary contain?

**Research**:

- Target audience: New contributors, future maintainers
- Goal: Understand architecture in <15 minutes
- Anti-patterns: Repeating code comments, implementation details

**Decision**: Architecture overview + component diagrams + event flows
**Rationale**:

- High-level understanding before diving into code
- Visual diagrams aid comprehension
- Event flows explain "how things work together"

**Sections**:

1. Architecture Overview (layers, dependencies)
2. Component Diagram (mermaid)
3. TTS Flow (user action → audio output)
4. STT Flow (hotkey → transcription → paste)
5. Data Model (entities and relationships)
6. Design Decisions (why certain patterns were chosen)
7. Development Setup (quick reference)

---

## Summary

| Topic            | Decision                              | Rationale                         |
| ---------------- | ------------------------------------- | --------------------------------- |
| Theme            | litera                                | Most Windows 11-native appearance |
| Bundling         | Minimal models, download on first use | Balance size vs experience        |
| Entry Point      | GUI default, CLI via flag             | Expected desktop app behavior     |
| System Tray      | pystray library                       | Standard, well-maintained         |
| Refactoring      | Extract by responsibility             | SOLID compliance, manageable risk |
| Colors           | Litera defaults + tweaks              | Accessibility compliant           |
| README           | Hero-first, visual emphasis           | User engagement focus             |
| Engineering Docs | Architecture + flows                  | Quick contributor onboarding      |
