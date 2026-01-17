# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Phase 0: Versioning & Release System**
  - Commitizen for automated version management and changelog generation
  - Conventional Commits policy documented in README.md and CONSTITUTION.md
  - Project Constitution (CONSTITUTION.md) defining core principles and standards
  - GitHub Actions workflows for automated version bumping and releases
  - Commit message guidelines and examples
  
- **Phase 2: CLI Enhancement**
  - Colorized CLI output with colorama (cyan status, green success, red error, yellow warning)
  - Progress timing indicators showing elapsed time for each operation
  - URL validation with protocol checks (http:// or https://)
  - File existence validation with helpful error messages
  - Enhanced help text with usage examples and command descriptions
  - Unit tests for CLI output and validation (20+ test cases)

- **Phase 3: Build & Packaging System**
  - PyPI package configuration with entry point (pagereader command)
  - Setuptools package discovery for src/ module structure
  - PyInstaller support for standalone Windows executable builds
  - Automated build script (build_exe.py) with hidden imports configuration
  - Comprehensive build documentation (docs/BUILD.md)
  - Local editable install testing (-e flag support)

- **Phase 4: Testing & Validation**
  - End-to-end integration tests (tests/integration/test_end_to_end.py)
  - Manual validation with real URLs (example.com, Wikipedia)
  - Standalone exe testing (31.98 MB executable, works without Python)
  - Performance validation (<1s total for simple URLs, well under 5s target)
  - 206 total tests passing (up from 185 baseline)

### Changed
- Updated README.md with commit message policy and Commitizen usage instructions
- Enhanced CLI error messages with helpful troubleshooting suggestions
- Improved URL and file validation with clear error output

### Performance Improvements
- Simple URL reading: <1 second total (0.22s fetch + 0.01s synthesis)
- Complex URL (Wikipedia): 0.85s fetch for 79KB content
- Synthesis: 342KB audio generated in 0.01s

### Technical
- Python 3.13.5 compatibility verified
- All dependencies updated to latest versions
- Coverage: 50% (baseline maintained, gaps in deferred v2.0 features)

## [1.0.0] - Not Yet Released

### Added
- Initial project setup with Python 3.13
- Core application structure:
  - Browser tab detection module (`src/browser/`)
  - Text extraction module (`src/extraction/`)
  - Text-to-speech synthesis module (`src/tts/`)
  - Session management module (`src/session/`)
  - CLI interface (`src/ui/`)
  - Utility modules (`src/utils/`)
- Comprehensive test suite:
  - Unit tests (≥80% coverage)
  - Integration tests (URL → speech, tab → speech)
  - Contract tests (API boundaries)
  - Performance benchmarks
- Development tooling:
  - pytest for testing with coverage reporting
  - ruff for linting and formatting
  - pre-commit hooks for code quality
  - GitHub Actions CI/CD pipelines
- Documentation:
  - README.md with quick start and usage examples
  - Implementation plan (specs/001-web-reader-ai/plan.md)
  - Task breakdown (specs/001-web-reader-ai/tasks.md)
  - Specification (specs/001-web-reader-ai/spec.md)

### Technical Details
- **Language**: Python 3.13
- **TTS Engine**: Piper (open-source, offline-capable neural TTS)
- **HTML Parsing**: BeautifulSoup4
- **Browser Detection**: pywinauto (Windows API integration)
- **Platform**: Windows 11 (initial release)

### Known Limitations (v1.0 Scope)
- URL-only input (browser tab detection deferred to v1.1)
- File path input removed (may return in v1.1)
- Basic playback controls (OS volume controls recommended)
- No session persistence (save/resume deferred to v1.1)
- English language only (multi-language support in v1.1)
- Windows-only (macOS/Linux support planned for v2.0)

### Performance
- URL fetch + text extraction + synthesis: <5 seconds for simple pages
- Memory footprint: <500 MB during synthesis
- Supports pages up to 100 MB

### Breaking Changes
- N/A (initial release)

---

## Release Process

### Automated Version Bumping
This project uses [Commitizen](https://commitizen-tools.github.io/commitizen/) for automated version management:

```bash
# Bump version automatically based on commit history
cz bump

# Bump to specific version
cz bump --increment MAJOR|MINOR|PATCH

# Preview version bump without making changes
cz bump --dry-run
```

### Changelog Generation
The changelog is automatically updated when you run `cz bump`. It parses commit messages following [Conventional Commits](https://www.conventionalcommits.org/) to categorize changes.

### Release Workflow
1. **Merge to main**: Pull requests are merged to `main` branch
2. **Auto-version bump**: GitHub Actions workflow detects new commits and runs `cz bump`
3. **Changelog update**: CHANGELOG.md is automatically updated
4. **Tag creation**: Create release tag manually or via `cz bump` (format: `vMAJOR.MINOR.PATCH`)
5. **Release artifacts**: Tag push triggers release workflow:
   - PyPI package published
   - Standalone exe built and uploaded to GitHub Releases
   - Release notes generated from CHANGELOG.md

### Manual Release (Maintainers)
```bash
# 1. Ensure you're on main branch with latest changes
git checkout main
git pull origin main

# 2. Bump version and update changelog
cz bump

# 3. Push changes and tags
git push origin main --tags

# 4. GitHub Actions will handle PyPI and exe publishing
```

### Version Numbering Guide
- **MAJOR** (1.0.0 → 2.0.0): Breaking changes (API incompatibility)
  - Example: Removing a CLI command, changing function signatures
- **MINOR** (1.0.0 → 1.1.0): New features (backward-compatible)
  - Example: Adding multi-language support, PDF reading
- **PATCH** (1.0.0 → 1.0.1): Bug fixes (backward-compatible)
  - Example: Fixing HTML parsing bug, improving error handling

---

[Unreleased]: https://github.com/AidanInceer/PageReader/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/AidanInceer/PageReader/releases/tag/v1.0.0
