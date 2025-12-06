# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-12-06

### Added - Massive Update
- **Graphical User Interface (GUI)**: Modern, dark-themed interface built with Tkinter
- **Singleton Pattern Implementation**: ScreenshotEngine with resource-efficient design
- **Multiple Resolution Support**: Full HD (1920x1080), 4K UHD (3840x2160), Mobile (375x812), Instagram (1080x1080)
- **Live Preview**: In-app thumbnail preview before saving
- **Full Preview Mode**: Open captured screenshot in default image viewer
- **Custom Save Location**: Choose where to save screenshots via file dialog
- **Threading Implementation**: Background processing for non-blocking UI
- **Resource Watchdog**: Automatic resource cleanup after 2 minutes of inactivity
- **Garbage Collection**: Explicit memory management to prevent memory leaks
- **Smart Progress Tracking**: Visual progress bar with real-time status updates
- **Performance Optimization**: Multi-threaded architecture prevents UI freezing

### Changed
- Migrated from CLI-only to GUI-based application
- Enhanced error handling and user feedback
- Improved memory management with automatic cleanup
- Better browser initialization with timeout controls

### Technical Improvements
- Thread-safe operations with locking mechanisms
- Daemon threads for background processes
- Optimized driver initialization and reuse
- Advanced Chrome options for better memory handling
- DOM-ready detection for faster captures

## [0.1.0] - 2024-12-06 (Previously labeled as 1.0.0)

### Added
- Initial release of StrangerPrints
- Full HD (1920x1080) screenshot capture functionality
- Interactive CLI for easy screenshot generation
- Automatic URL fixing (adds https:// if missing)
- Headless Chrome browser support via Selenium
- Configurable page load wait time
- Support for multiple screenshot captures in one session
- Command-line entry point via `strangerprints` command

### Features
- High-resolution screenshot generation (up to 4K support planned)
- Simple and robust CLI interface
- No manual browser driver installation required (uses webdriver-manager)
- Cross-platform support (Windows, macOS, Linux)

[2.0.0]: https://github.com/joaovcoelho/StrangerPrints/releases/tag/v2.0.0
[0.1.0]: https://github.com/joaovcoelho/StrangerPrints/releases/tag/v0.1.0
