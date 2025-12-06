# StrangerPrints - Browser Screenshot Renderer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/joaovcoelho/StrangerPrints/releases)

StrangerPrints is a powerful open-source tool designed to generate high-resolution screenshots (up to 4K) from web applications. Featuring a modern GUI, advanced memory management, and real-time preview capabilities, capturing web pages has never been easier or more efficient!

## ✨ Features

### 🎨 New in v2.0 - Massive Update!

- 🖥️ **Modern GUI Interface**: Beautiful dark-themed graphical interface with intuitive controls
- 🏗️ **Resource-Efficient Architecture**: Single instance engine design that reuses browser for optimal performance
- 📐 **Multiple Resolution Support**: 
  - Full HD (1920x1080)
  - 4K UHD (3840x2160)
  - Mobile (375x812)
  - Instagram Square (1080x1080)
- 👁️ **Live Preview**: See thumbnail previews of captured screenshots before saving
- 🔍 **Full Preview Mode**: Open screenshots in your default image viewer
- 💾 **Custom Save Location**: Choose exactly where to save your screenshots
- ⚡ **Threading & Performance**: Non-blocking UI with background processing
- 🧹 **Smart Memory Management**: Automatic resource cleanup and garbage collection
- 📊 **Progress Tracking**: Real-time progress bar and status updates
- 🛡️ **Resource Watchdog**: Automatic cleanup after 2 minutes of inactivity to free system resources

### 🔧 Core Features

- 📸 **High-Resolution Screenshots**: Generate screenshots up to 4K resolution
- 🔧 **Auto-Fix URLs**: Automatically adds `https://` to URLs without protocol
- 🚀 **No Manual Setup**: Automatically manages ChromeDriver installation
- 🐍 **Programmatic API**: Use StrangerPrints in your Python scripts (legacy CLI version available)
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

### GUI Application (v2.0)

Run the graphical interface:

```bash
python releases/strangerprints-v2.0.py
```

**Using the GUI:**
1. **Enter the target URL** in the URL field (e.g., `google.com` or `https://example.com`)
2. **Select the resolution** from the dropdown menu:
   - Full HD (1920x1080) - Standard desktop
   - 4K UHD (3840x2160) - Ultra high definition
   - Mobile (375x812) - iPhone X/11/12 size
   - Instagram (1080x1080) - Perfect for social media
3. **Set the wait time** (0-30 seconds) for dynamic content to load
4. **Click "RENDER SCREENSHOT"** to capture the page
5. **Preview** the thumbnail in the app
6. **Open Full View** to see the screenshot in your default image viewer
7. **Save to Disk** to choose where to save the image

**Key GUI Features:**
- Real-time progress bar shows capture status
- Status messages keep you informed
- Automatic resource management (frees memory after 2 minutes of inactivity)
- Thread-safe operations prevent UI freezing
- One-click preview and save functionality

### CLI Usage (v0.1 - Legacy)

Run the interactive CLI:

```bash
python releases/strangerprints-v0.1.py
```

Then follow the prompts:
1. Enter the URL of the website (e.g., `google.com` or `https://example.com`)
2. Specify the output filename (e.g., `screenshot.png`)
3. Set the wait time in seconds (default: 5)

### Programmatic Usage (Package)

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

## 🚀 What's New in v2.0?

Version 2.0 represents a complete reimagining of StrangerPrints with enterprise-grade features:

### Architecture Improvements

**Single Instance Design**: The application creates one `ScreenshotEngine` instance that reuses the browser driver across multiple captures. Thread-safe operations ensure only one browser instance is active at a time, preventing memory bloat and resource conflicts.

**Threading & Concurrency**: Background threads handle browser operations, preventing the GUI from freezing during captures. Thread locks ensure safe concurrent access to shared resources.

**Resource Watchdog**: A daemon thread monitors driver activity. If the browser hasn't been used for 2 minutes, it automatically terminates the process and frees memory. This prevents the application from consuming resources when idle.

**Garbage Collection**: Explicit calls to Python's garbage collector (`gc.collect()`) ensure memory is freed immediately after browser cleanup, not at the next automatic GC cycle.

### User Experience Enhancements

**GUI Interface**: Modern dark-themed interface built with Tkinter provides an intuitive, point-and-click experience. No more command-line complexity.

**Live Preview**: See what you captured immediately with an in-app thumbnail. No need to navigate to files to verify your screenshot.

**Multiple Resolutions**: Preset resolutions for common use cases (desktop, mobile, 4K, social media) eliminate the need to remember dimensions.

**Progress Feedback**: Real-time progress bar and status messages keep users informed during the capture process.

**Save Anywhere**: File dialog allows users to choose exactly where to save screenshots, with the proper filename and location.

### Performance Optimizations

- **Smart Page Loading**: Uses WebDriverWait with DOM-ready detection for faster captures
- **Optimized Chrome Options**: Configured for minimal memory usage and maximum performance
- **Non-Blocking Operations**: All time-consuming tasks run in background threads
- **Resource Reuse**: Driver persists between captures when possible, avoiding repeated initialization overhead

### Why These Changes Matter

**Before (v0.1)**: Simple CLI tool that created a new browser instance for each screenshot, had no preview capabilities, required manual file management, and could consume unbounded memory.

**After (v2.0)**: Professional-grade application with automatic resource management, real-time feedback, flexible resolution options, and a user-friendly interface suitable for both technical and non-technical users.

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

- Python 3.7+
- Chrome browser installed
- Internet connection (for initial ChromeDriver download)
- **Additional for v2.0 GUI**: Tkinter (usually included with Python), Pillow (PIL)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📦 Releases

All versioned releases are available in the [`releases/`](releases/) directory:

- **v2.0** (`strangerprints-v2.0.py`) - GUI with Singleton, Threading, Memory Management, Multiple Resolutions
- **v0.1** (`strangerprints-v0.1.py`) - Original CLI version

## 🔄 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed list of changes in each version.

### Version History

- **v2.0.0** (2025-12-06) - Massive update with GUI, Singleton implementation, Threading, Performance optimization
- **v0.1.0** (2024-12-06) - Initial CLI release

## 🐛 Bug Reports & Feature Requests

Please use the [GitHub Issues](https://github.com/joaovcoelho/StrangerPrints/issues) page to report bugs or request features.

## 📧 Contact

For questions or support, please open an issue on GitHub.

## 🌟 Acknowledgments

- Built with [Selenium](https://www.selenium.dev/)
- ChromeDriver management by [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager)

---

Made with ❤️ by the StrangerPrints community
