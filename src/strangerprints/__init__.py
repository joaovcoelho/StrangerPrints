"""
StrangerPrints - Browser Screenshot Renderer

An open-source tool for generating high-resolution screenshots from web applications.
"""

__version__ = "1.0.0"
__author__ = "StrangerPrints Contributors"
__license__ = "MIT"

from .renderer import take_fullhd_screenshot

__all__ = ["take_fullhd_screenshot", "__version__"]
