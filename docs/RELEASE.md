# Release Guide

This guide explains how to create and publish releases for StrangerPrints.

## Version Numbering

StrangerPrints follows [Semantic Versioning](https://semver.org/) (SemVer):

- **MAJOR** version (X.0.0): Incompatible API changes
- **MINOR** version (0.X.0): Backwards-compatible new features
- **PATCH** version (0.0.X): Backwards-compatible bug fixes

## Pre-Release Checklist

Before creating a release:

- [ ] All tests pass locally
- [ ] Code is merged to `main` branch
- [ ] CHANGELOG.md is updated with all changes
- [ ] Documentation is up to date
- [ ] Version number is updated in:
  - [ ] `src/strangerprints/__init__.py` (`__version__`)
  - [ ] `setup.py` (`version`)
  - [ ] `pyproject.toml` (`version`)

## Release Process

### 1. Update Version Numbers

Edit these files to update the version:

```python
# src/strangerprints/__init__.py
__version__ = "1.1.0"  # Update this
```

```python
# setup.py
setup(
    name="strangerprints",
    version="1.1.0",  # Update this
    ...
)
```

```toml
# pyproject.toml
[project]
version = "1.1.0"  # Update this
```

### 2. Update CHANGELOG.md

Add a new section for the release:

```markdown
## [1.1.0] - 2024-12-15

### Added
- New feature X
- Support for Y

### Changed
- Improved performance of Z

### Fixed
- Bug in feature A

[1.1.0]: https://github.com/joaovcoelho/StrangerPrints/compare/v1.0.0...v1.1.0
```

### 3. Commit Changes

```bash
git add src/strangerprints/__init__.py setup.py pyproject.toml CHANGELOG.md
git commit -m "Bump version to 1.1.0"
git push origin main
```

### 4. Create Git Tag

```bash
# Create annotated tag
git tag -a v1.1.0 -m "Release version 1.1.0"

# Push tag to GitHub
git push origin v1.1.0
```

### 5. Automated GitHub Release

Once you push a tag (format: `v*.*.*`), GitHub Actions will automatically:
- Build the package (`.tar.gz` and `.whl`)
- Create a GitHub Release
- Attach distribution files to the release
- Generate release notes

The workflow is defined in `.github/workflows/release.yml`.

### 6. Publish to PyPI (Optional)

To publish to PyPI, you need to:

1. Create a PyPI account at https://pypi.org
2. Generate an API token in PyPI account settings
3. Add token as GitHub secret: `PYPI_API_TOKEN`
4. Uncomment the PyPI publish step in `.github/workflows/release.yml`

Then releases will automatically publish to PyPI.

## Manual Release (Alternative)

If you prefer manual releases:

### Build the Package

```bash
# Install build tools
pip install build twine

# Build distribution files
python -m build

# Check the package
twine check dist/*
```

### Publish to PyPI

```bash
# Upload to PyPI
twine upload dist/*
```

### Create GitHub Release

1. Go to https://github.com/joaovcoelho/StrangerPrints/releases
2. Click "Draft a new release"
3. Choose the tag (or create new: `v1.1.0`)
4. Fill in release notes
5. Attach `dist/strangerprints-1.1.0.tar.gz` and `.whl` files
6. Click "Publish release"

## Release Types

### Patch Release (Bug Fix)

Example: 1.0.0 → 1.0.1

```bash
# Update version numbers
# Update CHANGELOG.md
git commit -m "Bump version to 1.0.1"
git tag -a v1.0.1 -m "Release version 1.0.1"
git push origin main
git push origin v1.0.1
```

### Minor Release (New Features)

Example: 1.0.1 → 1.1.0

```bash
# Update version numbers
# Update CHANGELOG.md
git commit -m "Bump version to 1.1.0"
git tag -a v1.1.0 -m "Release version 1.1.0"
git push origin main
git push origin v1.1.0
```

### Major Release (Breaking Changes)

Example: 1.1.0 → 2.0.0

```bash
# Update version numbers
# Update CHANGELOG.md (highlight breaking changes)
# Update migration guide if needed
git commit -m "Bump version to 2.0.0"
git tag -a v2.0.0 -m "Release version 2.0.0"
git push origin main
git push origin v2.0.0
```

## Pre-Release Versions

For alpha/beta/rc releases:

```bash
# Alpha: v1.1.0-alpha.1
git tag -a v1.1.0-alpha.1 -m "Release version 1.1.0-alpha.1"

# Beta: v1.1.0-beta.1
git tag -a v1.1.0-beta.1 -m "Release version 1.1.0-beta.1"

# Release Candidate: v1.1.0-rc.1
git tag -a v1.1.0-rc.1 -m "Release version 1.1.0-rc.1"
```

Mark these as "pre-release" on GitHub.

## Hotfix Process

For critical bugs in production:

1. Create hotfix branch from main: `git checkout -b hotfix/1.0.1`
2. Fix the bug
3. Update version to patch release (e.g., 1.0.1)
4. Update CHANGELOG.md
5. Merge to main
6. Tag and release

## Post-Release Checklist

After release:

- [ ] Verify release appears on GitHub
- [ ] Test installation: `pip install strangerprints`
- [ ] Verify CLI works: `strangerprints`
- [ ] Announce release (if applicable):
  - [ ] GitHub Discussions
  - [ ] Social media
  - [ ] Mailing list

## Versioning Examples

| Change Type | Example | Version |
|-------------|---------|---------|
| Bug fix | Fixed screenshot timeout | 1.0.0 → 1.0.1 |
| New feature | Added 4K support | 1.0.1 → 1.1.0 |
| Breaking change | Changed API signature | 1.1.0 → 2.0.0 |
| Multiple features | Added features A, B, C | 1.1.0 → 1.2.0 |

## Rolling Back a Release

If a release has critical issues:

1. **Immediately yank from PyPI**: Mark as "yanked" in PyPI
2. **Create hotfix**: Fix the issue
3. **Release patch**: Create new patch release
4. **Update GitHub release**: Add warning to release notes

```bash
# Create hotfix
git checkout -b hotfix/1.1.1 v1.1.0
# Fix issue
git commit -m "Fix critical bug"
git checkout main
git merge hotfix/1.1.1
git tag -a v1.1.1 -m "Hotfix: Fix critical bug"
git push origin main
git push origin v1.1.1
```

## Questions?

If you have questions about the release process:
- Check [CONTRIBUTING.md](../CONTRIBUTING.md)
- Open an issue with the `question` label
- Contact maintainers

## See Also

- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Python Packaging Guide](https://packaging.python.org/)
