"""
Setup configuration for StrangerPrints.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Define requirements directly to ensure they're always available
requirements = [
    "selenium>=4.0.0",
    "webdriver-manager>=3.8.0",
    "Pillow>=10.0.0",
]

setup(
    name="strangerprints",
    version="1.0.0",
    author="StrangerPrints Contributors",
    description="An open-source tool for generating high-resolution screenshots from web applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joaovcoelho/StrangerPrints",
    project_urls={
        "Bug Reports": "https://github.com/joaovcoelho/StrangerPrints/issues",
        "Source": "https://github.com/joaovcoelho/StrangerPrints",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Multimedia :: Graphics :: Capture :: Screen Capture",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    python_requires=">=3.12",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "strangerprints=strangerprints.cli:main",
        ],
    },
    keywords="screenshot, web, selenium, browser, automation, testing",
)
