# Feature Specification: App Modernization & Polish

**Feature Branch**: `005-app-modernization`  
**Created**: January 21, 2026  
**Status**: Draft  
**Input**: Convert CLI to downloadable executable, improve UI with modern light mode, remove redundant code, improve code quality following SOLID principles, update README to be user-focused, add engineering summary documentation

---

## User Scenarios & Testing _(mandatory)_

### User Story 1 - Download and Run Application (Priority: P1)

As a Windows user, I want to download a single executable file and run Vox as a native desktop application without needing to install Python or use command-line tools.

**Why this priority**: This is the core user experience transformation—users cannot experience any other improvements until they can easily install and run the app.

**Independent Test**: Download `vox.exe`, double-click to launch, verify the application window opens with all features accessible.

**Acceptance Scenarios**:

1. **Given** a user downloads `vox.exe` from the releases page, **When** they double-click the file, **Then** the Vox application window opens within 5 seconds
2. **Given** the application is running, **When** the user closes the window, **Then** all background processes terminate cleanly
3. **Given** a Windows 11 system without Python installed, **When** the user runs `vox.exe`, **Then** the application launches without errors
4. **Given** the user runs `vox.exe`, **When** the system tray is checked, **Then** a Vox icon is visible for minimized operation

---

### User Story 2 - Modern Light-Mode UI Experience (Priority: P1)

As a user, I want a clean, modern light-themed interface that feels native to Windows 11 and is visually appealing.

**Why this priority**: The UI is the primary user touchpoint—a polished, professional appearance builds trust and improves usability.

**Independent Test**: Launch the application and verify the light theme displays correctly with proper contrast, readable text, and visually consistent styling.

**Acceptance Scenarios**:

1. **Given** the application is launched, **When** the main window appears, **Then** it displays with a light color scheme (white/light gray background, dark text)
2. **Given** any UI element, **When** the user interacts with it, **Then** hover/focus states are visually clear with smooth transitions
3. **Given** the application is open, **When** compared to Windows 11 native apps, **Then** the styling feels consistent and modern (rounded corners, proper spacing, consistent fonts)
4. **Given** any screen in the application, **When** accessibility contrast is tested, **Then** all text meets WCAG AA contrast requirements (4.5:1 minimum)

---

### User Story 3 - Simplified Main Interface (Priority: P2)

As a user, I want a streamlined main window that shows me the essential controls without overwhelming me with options.

**Why this priority**: A clean interface reduces cognitive load and makes the app more approachable for first-time users.

**Independent Test**: Launch the app and complete both TTS and STT tasks using only the visible controls on the main screen.

**Acceptance Scenarios**:

1. **Given** the app is launched, **When** viewing the main window, **Then** the primary actions (Read Aloud, Voice Input) are immediately visible and prominent
2. **Given** the main window, **When** counting visible elements, **Then** there are no more than 5-7 primary interactive elements visible
3. **Given** advanced settings exist, **When** they are accessed, **Then** they are in a separate Settings panel, not cluttering the main view

---

### User Story 4 - Professional User-Focused Documentation (Priority: P2)

As a potential user visiting the GitHub page, I want to quickly understand what Vox does, see it in action, and know how to get started.

**Why this priority**: The README is the project's "front page"—it determines whether users try the app.

**Independent Test**: Show the README to someone unfamiliar with the project; they should understand what Vox does within 30 seconds.

**Acceptance Scenarios**:

1. **Given** a user visits the GitHub repo, **When** they view the README, **Then** they see a compelling hero section with the app's value proposition in the first viewport
2. **Given** the README, **When** scanning for installation, **Then** the download link for the executable is prominent and easy to find
3. **Given** the README, **When** looking for usage info, **Then** there are screenshots or GIFs showing the app in action
4. **Given** the README, **When** a user wants to contribute, **Then** they are directed to a separate CONTRIBUTING.md file

---

### User Story 5 - Developer Engineering Reference (Priority: P3)

As a developer interested in the codebase, I want a concise technical overview that explains the architecture and key design decisions.

**Why this priority**: Supports future contributors and maintainers, but not essential for end users.

**Independent Test**: A developer can read the engineering summary and understand the codebase structure without reading all the code.

**Acceptance Scenarios**:

1. **Given** a developer navigates to `docs/`, **When** they open the engineering summary, **Then** they find a concise (<500 lines) technical overview
2. **Given** the engineering document, **When** reviewing architecture, **Then** it explains the major components and their responsibilities
3. **Given** the engineering document, **When** looking for patterns, **Then** it describes the design patterns used (SOLID principles, clean architecture, etc.)

---

### Edge Cases

- What happens when the application is run without microphone permissions? → Show clear permission request dialog
- How does the system handle corrupted configuration files? → Reset to defaults with user notification
- What happens on very high DPI displays? → UI scales correctly maintaining readability
- How does the app behave when system audio is muted? → TTS features show visual indication that audio is muted

---

## Requirements _(mandatory)_

### Functional Requirements

**Executable Distribution:**

- **FR-001**: System MUST package as a single Windows executable using PyInstaller
- **FR-002**: System MUST bundle core TTS/STT libraries; models downloaded on first launch with progress indicator
- **FR-003**: System MUST start within 5 seconds on typical hardware (SSD, 8GB RAM, Intel i5 equivalent)
- **FR-004**: System MUST run without requiring Python installation on the user's machine
- **FR-005**: System MUST minimize to system tray when closed (optional setting to fully exit)

**UI Modernization:**

- **FR-006**: System MUST use a light theme as the default appearance
- **FR-007**: System MUST use `ttkbootstrap` with the "litera" theme
- **FR-008**: System SHOULD use rounded styling where supported by ttkbootstrap theme defaults
- **FR-009**: System MUST configure the "Segoe UI Variable" font family for Windows 11 consistency
- **FR-010**: System MUST use ttkbootstrap default hover/focus states for visual feedback

**Code Quality:**

- **FR-011**: All source files MUST be under 300 lines of code (excluding imports/comments)
- **FR-012**: All functions MUST have a single responsibility and be under 30 lines
- **FR-013**: All classes MUST follow the Single Responsibility Principle (one reason to change)
- **FR-014**: System MUST remove all unused/dead code paths
- **FR-015**: All public functions MUST have type hints and docstrings

**Documentation:**

- **FR-016**: README MUST lead with user benefits, not technical details
- **FR-017**: README MUST include visual media (screenshots/GIFs) showing the app
- **FR-018**: README MUST have a clear "Download" section with release links
- **FR-019**: Engineering summary MUST describe module responsibilities
- **FR-020**: Engineering summary MUST explain the event flow for TTS and STT operations

### Key Entities

- **Application Window**: The main UI container with tabs for Status, Settings, and History
- **Recording Indicator**: Floating overlay showing recording/processing state
- **Configuration**: User preferences stored locally (hotkey, theme, clipboard settings)
- **Transcription History**: Past voice-to-text conversions with timestamps

---

## Success Criteria _(mandatory)_

### Measurable Outcomes

- **SC-001**: Users can download and launch the app with zero configuration in under 60 seconds
- **SC-002**: Application startup time is under 5 seconds on standard hardware
- **SC-003**: All source files are under 300 lines, all functions under 30 lines
- **SC-004**: UI contrast ratio meets WCAG AA (4.5:1 for normal text)
- **SC-005**: README communicates value proposition within the first screen (no scrolling needed)
- **SC-006**: New contributors can understand the architecture from engineering docs in under 15 minutes
- **SC-007**: No unused imports, dead code, or commented-out code blocks remain in the codebase
- **SC-008**: All UI elements are accessible via keyboard navigation

---

## Assumptions

- Users have Windows 11 with standard system fonts installed
- The light theme will be well-received (dark mode can be added later as optional)
- PyInstaller can bundle Whisper and Piper models without excessive file size (target: <200MB)
- The existing feature set is complete; this modernization focuses on polish, not new features
- "speckit" branding in README refers to the specification-driven development workflow used

---

## Out of Scope

- macOS or Linux support (Windows-only for this iteration)
- Dark mode toggle (future feature)
- Auto-update mechanism (manual download for now)
- Installer (MSI/NSIS) — single executable is sufficient
- Cloud sync of settings or history
- Adding new TTS/STT features (this is polish only)
