# Usage Guide

This guide covers various ways to use StrangerPrints.

## CLI Usage

### Basic Usage

Start the interactive CLI:

```bash
strangerprints
```

### Interactive Prompts

The CLI will prompt you for:

1. **URL**: Enter the website URL
   - Can include protocol: `https://example.com`
   - Or without protocol: `example.com` (automatically adds `https://`)
   - Type `exit`, `quit`, or `sair` to quit

2. **Filename**: Output screenshot filename
   - Can include `.png` extension or not
   - Example: `screenshot.png` or just `screenshot`

3. **Wait Time**: Time in seconds to wait for page load
   - Default: 5 seconds
   - Increase for pages with heavy JavaScript or slow loading

### Example Session

```
==================================================
StrangerPrints - Browser Screenshot Renderer v1.0
==================================================

URL (or 'exit'): github.com
Filename: github
Wait time (s): 5

Navigating to https://github.com...
Waiting 5 seconds...
Saved to: github.png

URL (or 'exit'): exit

Thank you for using StrangerPrints!
```

## Programmatic Usage

### Basic Screenshot

```python
from strangerprints import take_fullhd_screenshot

# Take a screenshot
take_fullhd_screenshot("https://example.com", "example.png")
```

### Custom Wait Time

```python
from strangerprints import take_fullhd_screenshot

# Wait 10 seconds for page to load
take_fullhd_screenshot("https://example.com", "example.png", wait_time=10)
```

### Auto-Fix URL

```python
from strangerprints import take_fullhd_screenshot

# URL without protocol - automatically adds https://
take_fullhd_screenshot("google.com", "google.png")
```

### Multiple Screenshots

```python
from strangerprints import take_fullhd_screenshot

websites = [
    ("https://github.com", "github.png"),
    ("https://python.org", "python.png"),
    ("google.com", "google.png"),
]

for url, filename in websites:
    try:
        take_fullhd_screenshot(url, filename, wait_time=8)
    except Exception as e:
        print(f"Failed to capture {url}: {e}")
```

### Error Handling

```python
from strangerprints import take_fullhd_screenshot

try:
    take_fullhd_screenshot("https://example.com", "output.png")
    print("Screenshot captured successfully!")
except Exception as e:
    print(f"Error: {e}")
```

## Tips and Best Practices

### Wait Time

- **Fast static sites**: 3-5 seconds
- **Sites with JavaScript**: 5-10 seconds
- **Heavy single-page applications**: 10-15 seconds
- **Slow connections**: 15+ seconds

### File Naming

- Use descriptive names: `homepage.png`, `dashboard.png`
- Include dates for tracking: `screenshot_2024-12-06.png`
- Use directories: `screenshots/homepage.png`

### URL Formats

All these formats work:
- `https://example.com`
- `http://example.com`
- `example.com` (auto-converts to `https://example.com`)
- `www.example.com` (auto-converts to `https://www.example.com`)

### Resolution

Current version captures at Full HD (1920x1080). Future versions will support:
- HD (1280x720)
- 2K (2560x1440)
- 4K (3840x2160)

## Advanced Usage

### Custom Script

Create a custom script for batch processing:

```python
#!/usr/bin/env python3
"""Batch screenshot capture script"""

from strangerprints import take_fullhd_screenshot
import sys

def capture_batch(urls_file, output_dir="screenshots"):
    """Capture screenshots for URLs listed in a file"""
    import os
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    with open(urls_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
    
    for i, url in enumerate(urls, 1):
        filename = os.path.join(output_dir, f"screenshot_{i}.png")
        print(f"[{i}/{len(urls)}] Capturing {url}...")
        try:
            take_fullhd_screenshot(url, filename, wait_time=8)
        except Exception as e:
            print(f"  ✗ Failed: {e}")
        else:
            print(f"  ✓ Saved to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python batch_capture.py urls.txt")
        sys.exit(1)
    
    capture_batch(sys.argv[1])
```

Save as `batch_capture.py` and use:
```bash
python batch_capture.py urls.txt
```

Where `urls.txt` contains:
```
https://github.com
https://python.org
google.com
```

## Troubleshooting

### Screenshots are blank
- Increase wait time
- Check if the website blocks headless browsers
- Verify the URL is accessible

### ChromeDriver errors
- Ensure Chrome is installed
- Check internet connection for first run
- Clear ChromeDriver cache: `~/.wdm/` directory

### Memory issues
- Reduce number of simultaneous captures
- Close other applications
- Increase system swap space

## Getting Help

- Check [FAQ](../README.md)
- Review [examples](../examples/)
- Open an [issue](https://github.com/joaovcoelho/StrangerPrints/issues)
