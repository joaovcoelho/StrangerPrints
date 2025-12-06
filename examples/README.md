# StrangerPrints Examples

This directory contains example scripts demonstrating how to use StrangerPrints.

## Basic Usage

The `basic_usage.py` script shows how to use StrangerPrints programmatically:

```bash
python basic_usage.py
```

## CLI Usage

You can also use StrangerPrints from the command line after installation:

```bash
strangerprints
```

Then follow the interactive prompts:
1. Enter the URL of the website you want to capture
2. Specify the output filename
3. Set the wait time (in seconds) for the page to load

## Tips

- URLs without `http://` or `https://` will automatically be prefixed with `https://`
- Longer wait times may be needed for pages with heavy JavaScript or slow loading
- The default resolution is Full HD (1920x1080)
- Screenshots are saved in PNG format
