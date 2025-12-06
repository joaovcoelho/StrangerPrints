"""
Basic usage example for StrangerPrints.

This example demonstrates how to use StrangerPrints programmatically
to take screenshots of web pages.
"""

from strangerprints import take_fullhd_screenshot

# Example 1: Simple screenshot with default wait time
print("Example 1: Taking a screenshot of GitHub")
take_fullhd_screenshot("https://github.com", "github_screenshot.png")

# Example 2: Screenshot with custom wait time
print("\nExample 2: Taking a screenshot with 10 second wait time")
take_fullhd_screenshot("https://www.python.org", "python_screenshot.png", wait_time=10)

# Example 3: URL without protocol (auto-fixed)
print("\nExample 3: Taking a screenshot with auto-fixed URL")
take_fullhd_screenshot("google.com", "google_screenshot.png")

print("\nAll screenshots completed!")
