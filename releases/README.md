# StrangerPrints Releases

This directory contains all versioned releases of StrangerPrints. Each version is a standalone, self-contained Python script that can be run directly.

## Available Versions

### v2.0 - GUI Edition (Current)
**File**: `strangerprints-v2.0.py`  
**Released**: 2025-12-06

**Major Features:**
- 🖥️ Modern graphical user interface (GUI)
- 🏗️ Single instance architecture for resource efficiency
- 📐 Multiple resolution support (Full HD, 4K, Mobile, Instagram)
- 👁️ Live preview and full view capabilities
- 💾 Custom save location dialog
- ⚡ Threading for non-blocking UI
- 🧹 Automatic memory management and garbage collection
- 📊 Real-time progress tracking
- 🛡️ Resource watchdog (auto-cleanup after 2min inactivity)

**Usage:**
```bash
python strangerprints-v2.0.py
```

**Requirements:**
```bash
pip install selenium webdriver-manager pillow
```

**When to use:**
- You want a user-friendly GUI interface
- You need multiple resolution options
- You want to preview before saving
- You need efficient memory management for long sessions
- You prefer point-and-click over command-line

---

### v0.1 - CLI Edition (Legacy)
**File**: `strangerprints-v0.1.py`  
**Released**: 2024-12-06

**Features:**
- 📋 Simple command-line interface
- 📸 Full HD (1920x1080) screenshots
- 🔧 Auto-fix URLs (adds https://)
- ⏱️ Configurable wait time
- 🔄 Multiple captures in one session

**Usage:**
```bash
python strangerprints-v0.1.py
```

**Requirements:**
```bash
pip install selenium webdriver-manager
```

**When to use:**
- You prefer command-line interfaces
- You need a simple, lightweight solution
- You're scripting or automating captures
- You only need Full HD resolution
- You're running in environments without GUI support

---

## Choosing a Version

| Feature | v0.1 (CLI) | v2.0 (GUI) |
|---------|-----------|-----------|
| Interface | Command-line | Graphical |
| Resolutions | 1 (Full HD) | 4 (Full HD, 4K, Mobile, Instagram) |
| Preview | ❌ | ✅ |
| Save Dialog | ❌ | ✅ |
| Memory Management | Basic | Advanced with auto-cleanup |
| Threading | ❌ | ✅ (Non-blocking) |
| Resource Efficiency | Low | High (Instance reuse + Watchdog) |
| Progress Tracking | Text only | Visual progress bar |
| Best For | Scripts, automation | Interactive use, design work |

## Version Naming Convention

Files follow the pattern: `strangerprints-v{MAJOR}.{MINOR}.py`

- **MAJOR**: Significant architectural changes or breaking changes
- **MINOR**: New features, improvements (backward-compatible)

## Running Without Installation

Each version is a standalone script. You can run them directly after installing dependencies:

```bash
# Install dependencies (run once)
pip install selenium webdriver-manager pillow

# Run v2.0 (GUI)
python strangerprints-v2.0.py

# OR run v0.1 (CLI)
python strangerprints-v0.1.py
```

## Migration Guide

### From v0.1 to v2.0

**What stays the same:**
- URL auto-fixing (adds https:// automatically)
- ChromeDriver auto-installation
- Headless browser operation
- PNG output format

**What's new:**
- GUI replaces CLI prompts
- Choose resolution from dropdown instead of fixed Full HD
- Preview before saving instead of auto-save
- Progress bar instead of text messages
- Automatic resource cleanup

**No code changes needed** - Just run the new version and use the GUI!

## Changelog

See [CHANGELOG.md](../CHANGELOG.md) for detailed version history.

## Support

For issues or questions about specific versions:
- Open an issue: https://github.com/joaovcoelho/StrangerPrints/issues
- Specify which version you're using (v0.1 or v2.0)
- Include your Python version and operating system

## License

All versions are released under the MIT License. See [LICENSE](../LICENSE) for details.
