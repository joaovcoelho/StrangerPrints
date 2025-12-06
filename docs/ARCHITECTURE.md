# Project Architecture

This document describes the architecture and structure of the StrangerPrints repository.

## Repository Structure

```
StrangerPrints/
├── .github/                      # GitHub-specific files
│   ├── ISSUE_TEMPLATE/          # Issue templates
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── PULL_REQUEST_TEMPLATE/   # PR template
│   │   └── pull_request_template.md
│   └── workflows/               # GitHub Actions CI/CD
│       ├── python-package.yml   # Test and lint workflow
│       └── release.yml          # Release automation
│
├── docs/                        # Documentation
│   ├── README.md               # Documentation index
│   ├── INSTALLATION.md         # Installation guide
│   ├── USAGE.md               # Usage guide
│   ├── RELEASE.md             # Release process guide
│   └── ARCHITECTURE.md        # This file
│
├── examples/                   # Example scripts
│   ├── README.md              # Examples documentation
│   └── basic_usage.py         # Basic usage example
│
├── src/                       # Source code
│   └── strangerprints/       # Main package
│       ├── __init__.py       # Package initialization
│       ├── cli.py           # CLI implementation
│       └── renderer.py      # Screenshot functionality
│
├── tests/                    # Test files (to be added)
│
├── .gitattributes           # Git attributes
├── .gitignore              # Git ignore rules
├── CHANGELOG.md            # Version history
├── CODE_OF_CONDUCT.md      # Community guidelines
├── CONTRIBUTING.md         # Contribution guide
├── LICENSE                 # MIT License
├── MANIFEST.in            # Package manifest
├── README.md              # Project overview
├── SECURITY.md           # Security policy
├── pyproject.toml        # Modern Python packaging config
├── requirements.txt      # Dependencies
├── setup.py             # Package setup (legacy)
└── version_1_0.py       # Original version (kept for reference)
```

## Design Principles

### 1. Separation of Concerns

The codebase is organized into distinct modules:

- **`renderer.py`**: Core screenshot functionality
- **`cli.py`**: Command-line interface
- **`__init__.py`**: Package API

### 2. Standard Structure

Following Python best practices:
- Source code in `src/` directory
- Package structure for proper imports
- Entry points defined in `pyproject.toml`

### 3. Documentation-First

Comprehensive documentation at multiple levels:
- Repository level (README.md)
- Module level (docstrings)
- User guides (docs/)
- Code examples (examples/)

## Module Overview

### `strangerprints/__init__.py`

Package initialization and public API definition.

```python
__version__ = "1.0.0"
from .renderer import take_fullhd_screenshot
```

**Exports:**
- `__version__`: Package version
- `take_fullhd_screenshot`: Main screenshot function

### `strangerprints/renderer.py`

Core screenshot rendering functionality using Selenium.

**Key Components:**
- `take_fullhd_screenshot(url, save_path, wait_time)`: Main function
- Chrome options configuration
- WebDriver management via webdriver-manager
- Error handling

**Dependencies:**
- selenium: Browser automation
- webdriver-manager: ChromeDriver management

### `strangerprints/cli.py`

Interactive command-line interface.

**Key Components:**
- `user_input()`: Handle user interaction
- `main()`: CLI entry point
- Input validation
- Loop control

**Entry Point:**
```bash
strangerprints  # Calls main()
```

## Package Distribution

### Build Artifacts

The package generates two distribution formats:

1. **Source Distribution** (`.tar.gz`): Source code archive
2. **Wheel** (`.whl`): Pre-built binary package

### Installation Methods

```bash
# From PyPI (when published)
pip install strangerprints

# From source
pip install -e .

# From GitHub
pip install git+https://github.com/joaovcoelho/StrangerPrints.git
```

## CI/CD Pipeline

### Test Workflow (`.github/workflows/python-package.yml`)

Runs on: Push to main/develop, Pull Requests

**Jobs:**
1. **Test Matrix**:
   - OS: Ubuntu, Windows, macOS
   - Python: 3.12, 3.13, 3.14
   - Installs package and verifies imports

2. **Lint**:
   - flake8: Python linting
   - black: Code formatting check

### Release Workflow (`.github/workflows/release.yml`)

Triggers on: Tag push (v*.*.*)

**Jobs:**
1. Build source and wheel distributions
2. Verify package with twine
3. Create GitHub Release
4. Attach distribution files
5. (Optional) Publish to PyPI

## Dependency Management

### Runtime Dependencies

Defined in `requirements.txt` and `pyproject.toml`:

- **selenium**: Browser automation library
- **webdriver-manager**: Automatic ChromeDriver management

### Development Dependencies

Additional tools for development:
- **build**: Package building
- **twine**: PyPI upload
- **flake8**: Linting
- **black**: Code formatting

## Configuration Files

### `pyproject.toml`

Modern Python packaging configuration:
- Project metadata
- Dependencies
- Build system requirements
- Entry points

### `setup.py`

Legacy setuptools configuration (for compatibility):
- Package metadata
- Dependencies
- Classifiers
- Entry points

### `requirements.txt`

Plain text file listing runtime dependencies:
- Used for development and direct installation (`pip install -r requirements.txt`)
- Easy to read and version control
- Compatible with tools like pip-compile and Dependabot

### `MANIFEST.in`

Specifies additional files to include in distributions:
- Documentation files
- License
- Examples
- Changelog

### Why Both `setup.py` and `requirements.txt`?

The project maintains both for different use cases:

1. **`setup.py` / `pyproject.toml`**: 
   - Defines package metadata and dependencies for distribution
   - Used when installing the package (`pip install strangerprints`)
   - Required for uploading to PyPI
   - Dependencies are embedded in the package metadata

2. **`requirements.txt`**:
   - Provides a simple, standalone list of dependencies
   - Useful for development and testing environments
   - Compatible with tools that don't parse package metadata
   - Often used in CI/CD pipelines and containerization

**Best Practice**: Both files should be kept in sync. When adding a new dependency, update both `requirements.txt` and the `dependencies` list in `setup.py` / `pyproject.toml`.

## Extension Points

### Adding New Features

1. **New screenshot modes**: Add functions to `renderer.py`
2. **CLI options**: Extend `cli.py`
3. **Configuration**: Add config file support

### Future Architecture Considerations

Potential future enhancements:

1. **Configuration System**
   ```
   src/strangerprints/config.py  # Configuration management
   ```

2. **Multiple Browser Support**
   ```
   src/strangerprints/browsers/
   ├── chrome.py    # Chrome implementation
   ├── firefox.py   # Firefox implementation
   └── base.py      # Browser interface
   ```

3. **Plugin System**
   ```
   src/strangerprints/plugins/
   ├── __init__.py
   └── base.py      # Plugin interface
   ```

4. **Advanced Features**
   ```
   src/strangerprints/
   ├── resolution.py  # Resolution management
   ├── batch.py      # Batch processing
   └── async_render.py  # Async support
   ```

## Testing Strategy

### Test Structure (Planned)

```
tests/
├── __init__.py
├── test_renderer.py    # Renderer tests
├── test_cli.py        # CLI tests
└── fixtures/          # Test fixtures
```

### Test Categories

1. **Unit Tests**: Individual function testing
2. **Integration Tests**: End-to-end screenshot capture
3. **CLI Tests**: Command-line interface testing

## Version Control Strategy

### Branch Structure

- `main`: Stable production code
- `develop`: Development integration branch
- `feature/*`: Feature branches
- `hotfix/*`: Emergency fixes

### Commit Convention

Using conventional commits:
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation changes
- `chore:` Maintenance tasks
- `test:` Test additions/changes

## Release Strategy

Following Semantic Versioning (SemVer):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward-compatible)
- **PATCH**: Bug fixes (backward-compatible)

See [RELEASE.md](RELEASE.md) for detailed release process.

## Security Considerations

### Dependency Security

- Monitor dependencies for vulnerabilities
- Regular updates via Dependabot
- Security advisories via GitHub

### Safe Practices

- No credential storage
- Isolated browser sessions
- HTTPS for downloads
- Headless operation

See [SECURITY.md](../SECURITY.md) for security policy.

## Community Structure

### Contribution Process

1. Fork repository
2. Create feature branch
3. Make changes
4. Submit pull request
5. Code review
6. Merge to main

See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.

### Code of Conduct

All contributors must follow [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md).

## Resources

### Internal Documentation
- [Installation Guide](INSTALLATION.md)
- [Usage Guide](USAGE.md)
- [Release Guide](RELEASE.md)
- [Contributing Guide](../CONTRIBUTING.md)

### External Resources
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Python Packaging Guide](https://packaging.python.org/)
- [Semantic Versioning](https://semver.org/)

## Maintenance

### Regular Tasks

- [ ] Update dependencies
- [ ] Review and merge PRs
- [ ] Triage issues
- [ ] Update documentation
- [ ] Release new versions

### Health Metrics

Monitor:
- Test coverage
- Build status
- Issue response time
- PR merge time
- Documentation completeness

## Questions?

For questions about the architecture:
- Open an issue with `architecture` label
- Contact maintainers
- Review existing documentation
