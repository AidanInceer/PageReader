# PageReader Project Constitution v1.0.0

This document defines the core principles, standards, and workflows that govern the PageReader project. All contributors must follow these guidelines to maintain code quality, consistency, and alignment with project goals.

---

## 1. Core Principles

### 1.1 Test-First Development (TDD)
- **Mandate**: All production code must have tests written **before** implementation
- **Coverage**: Minimum 80% overall coverage; 95%+ for critical paths (text extraction, TTS, browser detection)
- **Test Types**: Unit tests (isolated), integration tests (component interaction), contract tests (API boundaries)
- **Tools**: pytest with coverage reporting, GitHub Actions enforces coverage gates

### 1.2 Text-Based I/O Protocol
- **Rationale**: Text streams are universal, testable, and composable
- **Design Pattern**: Core operations work with text (stdin/stdout/JSON), layered services add rich features (audio, UI)
- **Examples**: 
  - Browser tab detection → JSON output of tab metadata
  - Text extraction → plain text or structured data
  - TTS synthesis → audio playback from text input

### 1.3 Clear API Contracts
- **Documentation**: Every module exports well-defined interfaces with input/output specifications
- **Validation**: Use type hints (Python 3.13 typing), validate inputs at module boundaries
- **Principles**: SOLID (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion)

### 1.4 Semantic Versioning
- **Format**: `MAJOR.MINOR.PATCH`
  - **MAJOR**: Breaking changes (API incompatibility)
  - **MINOR**: New features (backward-compatible additions)
  - **PATCH**: Bug fixes (backward-compatible corrections)
- **Tags**: Version tags follow format `vMAJOR.MINOR.PATCH` (e.g., `v1.0.0`)
- **Automation**: Commitizen manages version bumps based on commit types

### 1.5 Code Quality Standards
- **Linting**: ruff (all-in-one Python linter + formatter)
- **Formatting**: ruff format with 120 character line length, PEP 8 conventions
- **Refactoring**: Mandatory refactoring checkpoint between all development phases
- **Principles**: 
  - **DRY** (Don't Repeat Yourself): Extract common logic into reusable functions/classes
  - **KISS** (Keep It Simple Stupid): Prefer simple, readable code over clever optimizations
  - **YAGNI** (You Aren't Gonna Need It): Implement only what's needed for current requirements

---

## 2. Commit Message Policy

### 2.1 Conventional Commits
All commits must follow [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

**Commit Types**:
- `feat`: New feature for the user
- `fix`: Bug fix for the user
- `docs`: Documentation-only changes
- `style`: Code style changes (formatting, whitespace, etc.)
- `refactor`: Code refactoring without changing behavior
- `perf`: Performance improvements
- `test`: Adding or modifying tests
- `build`: Changes to build system or dependencies
- `ci`: Changes to CI/CD configuration files
- `chore`: Maintenance tasks, tooling updates, etc.
- `revert`: Reverts a previous commit

**Scope** (optional but recommended):
- `browser`: Browser detection and window management
- `extraction`: Text extraction from HTML/DOM
- `tts`: Text-to-speech synthesis and playback
- `session`: Session management and persistence
- `ui`: User interface (CLI/GUI)
- `tests`: Test infrastructure and fixtures
- `ci`: CI/CD pipelines and automation
- `docs`: Documentation updates

**Examples**:
```bash
feat(tts): add speed adjustment controls
fix(extraction): handle malformed HTML without crashing
docs(readme): update installation instructions
test(browser): add unit tests for tab detection
ci(actions): add workflow for automated releases
refactor(extraction): simplify DOM walker logic
```

### 2.2 Breaking Changes
For breaking changes, add `!` after type/scope or include `BREAKING CHANGE:` in footer:

```
feat(api)!: change tab detection API signature

BREAKING CHANGE: TabDetector.get_tabs() now returns TabInfo[] instead of dict
```

### 2.3 Commitizen Tool
Use Commitizen for interactive commit creation:

```bash
# Interactive commit prompt
cz commit

# Version bump (maintainers only)
cz bump

# Generate changelog
cz changelog
```

---

## 3. Development Workflow

### 3.1 Branch Strategy
- **Main Branch**: `main` (protected, requires PR approval)
- **Feature Branches**: `NNN-feature-name` (e.g., `001-web-reader-ai`)
- **Hotfix Branches**: `hotfix/description` (for urgent production fixes)

### 3.2 Pull Request Process
1. Create feature branch from `main`
2. Implement changes following TDD (tests first, then code)
3. Run `ruff format .` and `ruff check --fix` before commit
4. Write conventional commit messages
5. Ensure all tests pass: `pytest tests/ --cov=src --cov-fail-under=80`
6. Push branch and open PR against `main`
7. Wait for CI checks to pass (linting, tests, coverage)
8. Request review from maintainers
9. Address review feedback
10. Merge to `main` (squash or merge commit)

### 3.3 Release Process
1. **Version Bump**: Merge commits to `main` trigger auto-version bump (GitHub Actions)
2. **Changelog**: Changelog is automatically updated on version bump
3. **Tagging**: Create release tag manually or via `cz bump` locally
4. **Distribution**: Tag push triggers release workflow (PyPI + standalone exe)

---

## 4. Testing Requirements

### 4.1 Coverage Targets
- **Overall**: ≥80% line coverage across all modules
- **Critical Paths**: ≥95% coverage for:
  - `src/extraction/` (text extraction accuracy is critical)
  - `src/tts/` (speech synthesis must be reliable)
  - `src/browser/` (tab detection must work consistently)

### 4.2 Test Organization
```
tests/
├── unit/              # Isolated component tests
├── integration/       # Component interaction tests
├── contract/          # External API boundary tests
├── performance/       # Benchmarks and profiling
└── fixtures/          # Test data and mocks
```

### 4.3 Test Naming Convention
- **Files**: `test_<module_name>.py` (e.g., `test_text_extractor.py`)
- **Classes**: `Test<ClassName>` (e.g., `TestTextExtractor`)
- **Functions**: `test_<behavior>` (e.g., `test_extract_paragraph_text`)

### 4.4 Test Markers
Use pytest markers to categorize tests:
- `@pytest.mark.unit`: Unit tests (fast, isolated)
- `@pytest.mark.integration`: Integration tests (slower, requires dependencies)
- `@pytest.mark.contract`: Contract tests (external API boundaries)
- `@pytest.mark.performance`: Performance benchmarks

---

## 5. Code Review Guidelines

### 5.1 Review Checklist
- [ ] Tests written before implementation (TDD)
- [ ] All tests pass
- [ ] Coverage ≥80% (≥95% for critical paths)
- [ ] Ruff linting passes (no errors)
- [ ] Code follows SOLID principles
- [ ] No code duplication (DRY)
- [ ] Simple, readable code (KISS)
- [ ] Conventional commit messages
- [ ] Documentation updated (if needed)
- [ ] No breaking changes without major version bump

### 5.2 Review Focus Areas
1. **Test Quality**: Are tests comprehensive? Do they cover edge cases?
2. **Code Clarity**: Is the code easy to understand? Are variable names descriptive?
3. **Architecture**: Does the design follow SOLID principles?
4. **Performance**: Are there obvious performance issues?
5. **Security**: Are inputs validated? Are there potential security vulnerabilities?

---

## 6. Refactoring Checkpoints

### 6.1 Mandatory Refactoring Between Phases
After completing each development phase, perform these steps:

1. **Code Formatting**: `ruff format .`
2. **Code Linting**: `ruff check --fix`
3. **Manual Code Review**: Check for SOLID violations, DRY/KISS breaches
4. **Test Coverage**: `pytest tests/ --cov=src --cov-report=term-missing --cov-fail-under=80`
5. **Documentation**: Update docstrings, inline comments, README as needed
6. **Commit**: `git commit -m "refactor(phase-X): apply formatting, linting, and coverage check"`

### 6.2 Refactoring Rationale
- **Prevents Technical Debt**: Regular refactoring prevents accumulation of code smells
- **Maintains Consistency**: Ensures all code follows project standards
- **Enforces Quality Gates**: Coverage and linting gates are checked incrementally

---

## 7. Documentation Standards

### 7.1 Code Documentation
- **Module Docstrings**: Every module has a docstring explaining its purpose
- **Function Docstrings**: Every public function has a docstring with:
  - Brief description
  - Args section (parameter types and descriptions)
  - Returns section (return type and description)
  - Raises section (exceptions that may be raised)
- **Inline Comments**: Use sparingly; explain "why" not "what"

### 7.2 Project Documentation
- **README.md**: Quick start, usage examples, architecture overview
- **INSTALLATION.md**: Detailed installation instructions (PyPI + standalone exe)
- **CONTRIBUTING.md**: Development workflow, commit guidelines, testing requirements
- **CHANGELOG.md**: Auto-generated from conventional commits
- **docs/**: Additional documentation (architecture, API reference, etc.)

---

## 8. Continuous Integration (CI/CD)

### 8.1 GitHub Actions Workflows
- **CI Pipeline** (on PR and push to main):
  - Lint check: `ruff check`
  - Format check: `ruff format --check`
  - Test suite: `pytest tests/ --cov=src --cov-fail-under=80`
  - Coverage report: Upload to Codecov or similar
  
- **Version Bump Workflow** (on merge to main):
  - Auto-bump version using Commitizen
  - Update CHANGELOG.md
  - Commit and push version changes

- **Release Workflow** (on tag push):
  - Build PyPI package
  - Build standalone exe (PyInstaller)
  - Publish to PyPI
  - Create GitHub Release with artifacts

### 8.2 Branch Protection Rules
- **main branch**:
  - Require PR approval before merge
  - Require status checks to pass (CI pipeline)
  - Require linear history (squash or rebase merges)
  - No direct pushes (except automated version bump commits)

---

## 9. Versioning and Release Strategy

### 9.1 Version Numbering
- **Current Version**: v1.0.0
- **Next Minor**: v1.1.0 (new features, backward-compatible)
- **Next Major**: v2.0.0 (breaking changes)

### 9.2 Release Artifacts
- **PyPI Package**: `pip install pagereader`
- **Standalone Executable**: `pagereader.exe` (Windows)

### 9.3 Release Notes
- Auto-generated from CHANGELOG.md
- Include:
  - New features
  - Bug fixes
  - Breaking changes
  - Known issues

---

## 10. Performance and Scalability

### 10.1 Performance Targets (v1.0)
- Extract text from browser tab: <3 seconds
- Generate speech from text: <5 seconds
- Switch between tabs: <2 seconds
- Resume saved session: <1 second
- Memory footprint: <300 MB during operation

### 10.2 Scalability Considerations
- Single-user desktop utility (v1.0)
- Future multi-user server mode (v2.0+)
- Batch processing support (v1.1+)

---

## 11. Security and Privacy

### 11.1 Data Handling
- **User Data**: Reading sessions stored locally (SQLite or JSON)
- **No Telemetry**: Application does not send usage data to external servers
- **Offline-First**: TTS engine (Piper) runs fully offline, no API keys required

### 11.2 Input Validation
- Validate all user inputs (URLs, file paths, tab IDs)
- Sanitize HTML before text extraction (prevent XSS in extracted content)
- Handle untrusted content safely (malformed HTML, large files)

---

## 12. Amendment Process

### 12.1 Constitution Updates
This constitution may be updated to reflect project evolution:
1. Propose amendment via GitHub issue
2. Discuss with maintainers and community
3. Submit PR with proposed changes
4. Require maintainer approval
5. Update version: `vMAJOR.MINOR.PATCH` (MINOR bump for non-breaking clarifications, MAJOR for fundamental changes)

### 12.2 Version History
- **v1.0.0** (2026-01-17): Initial constitution

---

## 13. Contact and Support

- **Repository**: https://github.com/AidanInceer/PageReader
- **Issues**: https://github.com/AidanInceer/PageReader/issues
- **Maintainer**: Aidan

---

**Last Updated**: 2026-01-17  
**Version**: 1.0.0
