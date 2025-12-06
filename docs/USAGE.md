# Usage Guide

This guide covers various ways to use StrangerPrints across different versions.

## GUI Usage (v2.0 - Recommended)

### Starting the Application

Run the graphical interface:

```bash
python releases/strangerprints-v2.0.py
```

### Using the GUI

**Step-by-Step Guide:**

1. **Launch the application** - A dark-themed window will appear with "StrangerPrints" header

2. **Enter Target URL**
   - Type the website URL in the "Target URL" field
   - Protocol is optional: `github.com` or `https://github.com`
   - URL is automatically prefixed with `https://` if needed

3. **Select Resolution**
   - Click the "Resolution" dropdown
   - Choose from:
     - **Full HD (1920x1080)**: Standard desktop screenshot
     - **4K UHD (3840x2160)**: Ultra high definition for detailed captures
     - **Mobile (375x812)**: iPhone-sized viewport for mobile testing
     - **Instagram (1080x1080)**: Perfect square for social media

4. **Set Wait Time**
   - Use the "Wait (s)" spinner to set load time (0-30 seconds)
   - Recommended: 3-5 seconds for static sites, 5-10 for dynamic content

5. **Capture Screenshot**
   - Click the **"RENDER SCREENSHOT"** button
   - Progress bar shows real-time status
   - Status label updates: "Waking up engine..." → "Navigating..." → "Waiting..." → "Capturing..." → "Complete."

6. **Preview Results**
   - Thumbnail preview appears automatically below the progress bar
   - Click **"Open Full View"** to see the screenshot in your default image viewer
   - Note: Full View can only be opened once per capture

7. **Save Screenshot**
   - Click **"Save to Disk"**
   - Choose location and filename in the file dialog
   - File is saved with PNG optimization

### GUI Features

**Real-Time Status**: The status label at the bottom shows current operation status

**Progress Tracking**: Visual progress bar fills during the wait phase

**Resource Management**: The application automatically frees memory after 2 minutes of inactivity (you'll see "Idle (Resources Freed)" status)

**Engine Warm-up**: On first launch, the application initializes Chrome in the background

**Error Handling**: Failures are shown in red status text with "Failed." message

### Example Workflow

```
1. Launch app → Status: "Initializing Engine..." then "Ready."
2. Enter: github.com
3. Select: 4K UHD (3840x2160)
4. Wait: 5 seconds
5. Click: "RENDER SCREENSHOT"
6. Watch: Progress bar fills over 5 seconds
7. See: Thumbnail preview appears
8. Click: "Open Full View" (opens in default viewer)
9. Click: "Save to Disk"
10. Choose: ~/Pictures/github-screenshot.png
11. Done: Status shows "Saved."
```

## CLI Usage (v0.1 - Legacy)

### Basic Usage

Start the interactive CLI:

```bash
python releases/strangerprints-v0.1.py
```

### Interactive Prompts

The CLI will prompt you for:

1. **URL**: Enter the website URL
   - Can include protocol: `https://example.com`
   - Or without protocol: `example.com` (automatically adds `https://`)
   - Type `exit`, `quit`, or `sair` (Portuguese for "exit") to quit

2. **Filename**: Output screenshot filename
   - Can include `.png` extension or not
   - Example: `screenshot.png` or just `screenshot`

3. **Wait Time**: Time in seconds to wait for page load
   - Default: 5 seconds
   - Increase for pages with heavy JavaScript or slow loading

### Example CLI Session (v0.1)

```
URL (or 'exit'): github.com
Filename: github
Wait time (s): 5

Navigating to https://github.com...
Waiting 5 seconds...
Saved to: github.png

URL (or 'exit'): exit
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

**v2.0 GUI** supports multiple resolutions:
- Full HD (1920x1080) - Standard desktop
- 4K UHD (3840x2160) - Ultra high definition  
- Mobile (375x812) - iPhone X/11/12 viewport
- Instagram (1080x1080) - Social media square

**v0.1 CLI** captures at Full HD (1920x1080) only

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
