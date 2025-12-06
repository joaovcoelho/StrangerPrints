# Contributing to StrangerPrints

First off, thank you for considering contributing to StrangerPrints! It's people like you that make StrangerPrints such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by respect and professionalism. By participating, you are expected to uphold this standard.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to see if the problem has already been reported. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** to demonstrate the steps
- **Describe the behavior you observed** and what behavior you expected to see
- **Include screenshots** if relevant
- **Include your environment details** (OS, Python version, browser version)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful** to most StrangerPrints users
- **List any similar features** in other tools if applicable

### Pull Requests

1. Fork the repository and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure your code follows the existing style conventions
4. Make sure your code lints without errors
5. Update the documentation if needed
6. Write a clear and descriptive commit message
7. Include relevant issue numbers in the PR description

## Development Setup

1. Clone your fork of the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/StrangerPrints.git
   cd StrangerPrints
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   pip install -r requirements.txt
   ```

4. Make your changes and test them:
   ```bash
   strangerprints
   ```

## Styleguides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line

### Python Styleguide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small when possible

## Release Process

Maintainers will handle the release process:

1. Update version in `src/strangerprints/__init__.py` and `setup.py`
2. Update `CHANGELOG.md` with the new version changes
3. Create a new git tag: `git tag -a v1.x.x -m "Release version 1.x.x"`
4. Push the tag: `git push origin v1.x.x`
5. Create a GitHub release with release notes

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

Thank you for contributing! 🎉
