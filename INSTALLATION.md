# Installation Guide

PageReader can be installed in two ways: as a Python package via PyPI or as a standalone Windows executable. Choose the method that best fits your needs.

---

## Installation Method 1: PyPI Package (For Developers)

This method installs PageReader as a Python package that integrates with your Python environment.

### Prerequisites
- Python 3.13 or higher
- pip or [uv](https://astral.sh/blog/uv/) package manager
- Windows 11 (current version)

### Installation Steps

#### Option A: Using pip
```bash
# Install from PyPI
pip install pagereader

# Verify installation
pagereader --version
```

#### Option B: Using uv (recommended for faster installs)
```bash
# Install uv if you haven't already
pip install uv

# Install pagereader using uv
uv pip install pagereader

# Verify installation
pagereader --version
```

#### Option C: From source (for contributors)
```bash
# Clone the repository
git clone https://github.com/AidanInceer/PageReader.git
cd PageReader

# Install in development mode
pip install -e ".[dev]"

# Verify installation
python -m src.main --version
```

### First Run
```bash
# Read from a URL
pagereader read --url https://example.com

# Show help
pagereader --help
```

---

## Installation Method 2: Standalone Executable (For End Users)

This method requires no Python installation. The executable includes everything needed to run PageReader.

### Prerequisites
- Windows 11
- No Python installation required

### Installation Steps

1. **Download the latest release**:
   - Visit the [Releases page](https://github.com/AidanInceer/PageReader/releases)
   - Download `pagereader.exe` from the latest release

2. **Move to desired location**:
   ```powershell
   # Example: Move to C:\Program Files\PageReader
   mkdir "C:\Program Files\PageReader"
   Move-Item -Path ".\Downloads\pagereader.exe" -Destination "C:\Program Files\PageReader\pagereader.exe"
   ```

3. **(Optional) Add to PATH**:
   ```powershell
   # Add to system PATH so you can run `pagereader` from anywhere
   [Environment]::SetEnvironmentVariable(
       "Path",
       [Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Program Files\PageReader",
       "User"
   )
   
   # Restart PowerShell or Command Prompt to apply changes
   ```

4. **Verify installation**:
   ```powershell
   # If added to PATH:
   pagereader --version
   
   # Or run directly:
   & "C:\Program Files\PageReader\pagereader.exe" --version
   ```

### First Run
```powershell
# Read from a URL
pagereader read --url https://example.com

# Show help
pagereader --help
```

---

## Usage Examples

### Reading Web Pages
```bash
# Read from a URL
pagereader read --url https://news.ycombinator.com

# Read from a local HTML file
pagereader read --file ~/Documents/article.html
```

### Session Management (Future Feature)
```bash
# List saved sessions
pagereader sessions

# Resume a saved session
pagereader resume my-article

# Delete a session
pagereader delete-session my-article
```

---

## Troubleshooting

### Python Package Issues

**Problem**: `pip install pagereader` fails with "No matching distribution found"
- **Solution**: Ensure you have Python 3.13+ installed. Check with `python --version`

**Problem**: `pagereader: command not found` after installation
- **Solution**: 
  - Check if the package is installed: `pip show pagereader`
  - If installed, the Scripts folder might not be in your PATH. Add it:
    ```bash
    # Windows (PowerShell)
    $env:Path += ";$env:LOCALAPPDATA\Programs\Python\Python313\Scripts"
    
    # Or find your Python Scripts folder
    python -m site --user-base
    ```

**Problem**: Import errors when running `pagereader`
- **Solution**: Ensure all dependencies are installed: `pip install -e ".[dev]"`

### Standalone Executable Issues

**Problem**: Windows Defender blocks the executable
- **Solution**: 
  - This is a false positive due to PyInstaller bundling
  - Add an exception: Windows Security → Virus & threat protection → Manage settings → Add exclusion
  - Or download from official GitHub Releases only

**Problem**: "VCRUNTIME140.dll not found" error
- **Solution**: Install Microsoft Visual C++ Redistributable:
  - Download from: https://aka.ms/vs/17/release/vc_redist.x64.exe
  - Run installer and restart your computer

**Problem**: Executable fails to start or crashes immediately
- **Solution**:
  - Run from Command Prompt to see error messages:
    ```cmd
    cd "C:\Program Files\PageReader"
    pagereader.exe --help
    ```
  - Check if antivirus is blocking execution
  - Ensure you have administrator privileges if installed in Program Files

### Audio Playback Issues

**Problem**: No audio output when reading
- **Solution**:
  - Check system volume is not muted
  - Verify speakers/headphones are connected
  - Check Windows audio settings: Settings → System → Sound

**Problem**: Audio is choppy or stuttering
- **Solution**:
  - Close other audio applications
  - Check CPU usage (Task Manager)
  - Try a shorter text passage to test

---

## Updating PageReader

### Updating PyPI Package
```bash
# Upgrade to latest version
pip install --upgrade pagereader

# Or using uv
uv pip install --upgrade pagereader
```

### Updating Standalone Executable
1. Download the latest `pagereader.exe` from [Releases](https://github.com/AidanInceer/PageReader/releases)
2. Replace the old executable with the new one
3. No uninstallation required

---

## Uninstallation

### Uninstalling PyPI Package
```bash
# Using pip
pip uninstall pagereader

# Or using uv
uv pip uninstall pagereader
```

### Uninstalling Standalone Executable
1. Delete the executable file:
   ```powershell
   Remove-Item "C:\Program Files\PageReader\pagereader.exe"
   ```
2. Remove from PATH if you added it:
   ```powershell
   # Edit environment variables manually through Windows Settings
   # Control Panel → System → Advanced system settings → Environment Variables
   ```

---

## Development Setup (For Contributors)

If you want to contribute to PageReader, follow these steps:

### 1. Clone Repository
```bash
git clone https://github.com/AidanInceer/PageReader.git
cd PageReader
```

### 2. Create Virtual Environment
```bash
# Using venv
python -m venv .venv

# Activate on Windows
.\.venv\Scripts\Activate.ps1

# Activate on Linux/macOS
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
# Install all development dependencies
pip install -e ".[dev]"

# Or using uv
uv pip install -e ".[dev]"
```

### 4. Install Pre-commit Hooks (Optional but Recommended)
```bash
# Install pre-commit
pip install pre-commit

# Install git hooks
pre-commit install
```

### 5. Run Tests
```bash
# Run full test suite
pytest tests/ --cov=src --cov-report=term-missing

# Run specific test category
pytest tests/unit/
pytest tests/integration/
```

### 6. Format and Lint Code
```bash
# Format code
ruff format .

# Lint code
ruff check --fix
```

### 7. Build Standalone Executable (Optional)
```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
python build_exe.py

# Test executable
dist\pagereader.exe --help
```

---

## Release Workflow (For Maintainers)

PageReader uses automated versioning and releases through GitHub Actions and Commitizen.

### Conventional Commits

All commits must follow [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

**Types**:
- `feat`: New feature (triggers MINOR version bump)
- `fix`: Bug fix (triggers PATCH version bump)
- `docs`: Documentation changes
- `style`: Code formatting (no functional changes)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding/modifying tests
- `build`: Build system or dependency changes
- `ci`: CI/CD configuration changes
- `chore`: Maintenance tasks
- `BREAKING CHANGE`: Breaking change (triggers MAJOR version bump)

**Examples**:
```bash
feat(tts): add speed adjustment controls
fix(extraction): handle malformed HTML without crashing
docs(readme): update installation instructions
```

### Using Commitizen for Commits

Instead of manually writing commit messages, use Commitizen:

```bash
# Interactive commit (prompts for type, scope, description, etc.)
cz commit

# Shorthand
cz c
```

This ensures all commits follow the correct format.

### Version Bumping

**Automated** (recommended):
1. Merge PRs to `main` branch with conventional commits
2. GitHub Actions automatically runs `cz bump` on merge
3. Version is bumped based on commit types (feat=MINOR, fix=PATCH, BREAKING CHANGE=MAJOR)
4. CHANGELOG.md is automatically updated
5. New version is committed and pushed to `main`

**Manual** (for hotfixes or special cases):
```bash
# Bump version locally (requires maintainer permissions)
cz bump

# Push changes and tags
git push origin main --follow-tags
```

### Creating a Release

**Automated** (recommended):
1. After version bump, create a git tag:
   ```bash
   git tag v1.1.0
   git push origin v1.1.0
   ```
2. GitHub Actions automatically:
   - Builds PyPI package
   - Builds Windows executable
   - Publishes to PyPI
   - Creates GitHub Release with artifacts

**Manual** (if automation fails):
1. Build PyPI package:
   ```bash
   python -m build
   twine upload dist/*
   ```
2. Build Windows executable:
   ```bash
   python build_exe.py
   ```
3. Create GitHub Release manually and upload `pagereader.exe`

### Release Checklist

Before releasing a new version:
- [ ] All tests pass (`pytest tests/`)
- [ ] Code coverage ≥80% (`pytest --cov`)
- [ ] Linting passes (`ruff check`)
- [ ] Formatting is consistent (`ruff format --check`)
- [ ] CHANGELOG.md is up to date (auto-generated by `cz bump`)
- [ ] README.md is accurate
- [ ] All documentation is current

### Troubleshooting Release Issues

**Problem**: `cz bump` says "No commits to bump"
- **Solution**: Ensure you have conventional commits (feat, fix, etc.) since the last version

**Problem**: GitHub Actions release workflow fails
- **Solution**: 
  - Check workflow logs in GitHub Actions tab
  - Ensure PyPI credentials are configured in repository secrets
  - Verify `build_exe.py` script exists and is executable

**Problem**: PyPI upload fails with "File already exists"
- **Solution**: 
  - Version already exists on PyPI, bump version again
  - Or use `twine upload --skip-existing dist/*`

---

## Support

For issues, questions, or feature requests:
- Open an issue: [GitHub Issues](https://github.com/AidanInceer/PageReader/issues)
- Check documentation: [README.md](README.md) and [CONSTITUTION.md](CONSTITUTION.md)
- Review changelog: [CHANGELOG.md](CHANGELOG.md)

---

**Last Updated**: 2026-01-17  
**Version**: 1.0.0
