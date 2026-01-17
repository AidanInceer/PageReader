# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Commitizen for automated version management and changelog generation
- Conventional Commits policy documented in README.md and CONSTITUTION.md
- Project Constitution (CONSTITUTION.md) defining core principles and standards
- Commit message guidelines and examples

### Changed
- Updated README.md with commit message policy and Commitizen usage instructions

## [1.0.0] - 2026-01-17

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
