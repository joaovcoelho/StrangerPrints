# StrangerPrints - Browser Screenshot Renderer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

StrangerPrints is an open-source tool designed to allow users to generate high-resolution screenshots (up to 4K) from web applications. With an easy-to-use CLI and programmatic API, capturing web pages has never been simpler!

## ✨ Features

- 📸 **High-Resolution Screenshots**: Generate Full HD (1920x1080) screenshots with support for higher resolutions
- 🎯 **Simple CLI Interface**: Interactive command-line interface for quick screenshot captures
- 🔧 **Auto-Fix URLs**: Automatically adds `https://` to URLs without protocol
- 🚀 **No Manual Setup**: Automatically manages ChromeDriver installation
- 🐍 **Programmatic API**: Use StrangerPrints in your Python scripts
- ⏱️ **Configurable Wait Time**: Set custom page load times for dynamic content
- 🌐 **Cross-Platform**: Works on Windows, macOS, and Linux

## 📦 Installation

### From PyPI (coming soon)

```bash
pip install strangerprints
```

### From Source

1. Clone the repository:
```bash
git clone https://github.com/joaovcoelho/StrangerPrints.git
cd StrangerPrints
```

2. Install the package:
```bash
pip install -e .
```

Or install dependencies directly:
```bash
pip install -r requirements.txt
```

## 🚀 Quick Start

### CLI Usage

Run the interactive CLI:

```bash
strangerprints
```

Then follow the prompts:
1. Enter the URL of the website (e.g., `google.com` or `https://example.com`)
2. Specify the output filename (e.g., `screenshot.png`)
3. Set the wait time in seconds (default: 5)

### Programmatic Usage

Use StrangerPrints in your Python code:

```python
from strangerprints import take_fullhd_screenshot

# Take a screenshot with default settings
take_fullhd_screenshot("https://github.com", "github.png")

# Take a screenshot with custom wait time
take_fullhd_screenshot("https://example.com", "example.png", wait_time=10)

# URL without protocol (auto-fixed to https://)
take_fullhd_screenshot("google.com", "google.png")
```

## 📚 Documentation

For more examples, see the [examples](examples/) directory.

### API Reference

#### `take_fullhd_screenshot(url, save_path, wait_time=5)`

Captures a Full HD screenshot of a web page.

**Parameters:**
- `url` (str): The URL of the web page to capture
- `save_path` (str): The file path where the screenshot will be saved
- `wait_time` (int, optional): Time in seconds to wait for page load (default: 5)

**Example:**
```python
take_fullhd_screenshot("https://python.org", "python_homepage.png", wait_time=8)
```

## 🛠️ Requirements

- Python 3.12+ (supports Python 3.12, 3.13, and 3.14)
- Chrome browser installed
- Internet connection (for initial ChromeDriver download)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔄 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes in each version.

## 🐛 Bug Reports & Feature Requests

Please use the [GitHub Issues](https://github.com/joaovcoelho/StrangerPrints/issues) page to report bugs or request features.

## 📧 Contact

For questions or support, please open an issue on GitHub.

## 🌟 Acknowledgments

- Built with [Selenium](https://www.selenium.dev/)
- ChromeDriver management by [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager)

---

Made with ❤️ by the StrangerPrints community
