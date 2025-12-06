# Installation Guide

This guide will help you install StrangerPrints on your system.

## Prerequisites

Before installing StrangerPrints, ensure you have:

- Python 3.7 or higher installed
- Chrome browser installed on your system
- Internet connection (for initial ChromeDriver download)

## Installation Methods

### Method 1: Install from PyPI (Recommended)

Once published to PyPI, you can install using pip:

```bash
pip install strangerprints
```

### Method 2: Install from Source

1. Clone the repository:
```bash
git clone https://github.com/joaovcoelho/StrangerPrints.git
cd StrangerPrints
```

2. Install using pip:
```bash
pip install -e .
```

Or install dependencies directly:
```bash
pip install -r requirements.txt
```

### Method 3: Install from GitHub

You can install directly from GitHub:

```bash
pip install git+https://github.com/joaovcoelho/StrangerPrints.git
```

## Verify Installation

After installation, verify that StrangerPrints is installed correctly:

```bash
strangerprints
```

You should see the StrangerPrints CLI interface.

To verify the Python package:

```python
python -c "from strangerprints import __version__; print(__version__)"
```

This should output: `1.0.0`

## Troubleshooting

### ChromeDriver Issues

If you encounter issues with ChromeDriver, ensure:
- Chrome browser is installed on your system
- You have an active internet connection for the first run
- The webdriver-manager package can download and cache ChromeDriver

### Permission Issues

If you get permission errors during installation:
- Use `pip install --user` to install in your user directory
- Or use a virtual environment (recommended)

### Virtual Environment (Recommended)

It's recommended to use a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install StrangerPrints
pip install strangerprints
```

## Uninstallation

To uninstall StrangerPrints:

```bash
pip uninstall strangerprints
```

## Next Steps

After installation, check out:
- [Quick Start Guide](../README.md#-quick-start)
- [Usage Examples](../examples/README.md)
- [API Reference](../README.md#api-reference)
