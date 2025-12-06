"""
Core screenshot rendering functionality for StrangerPrints.
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def take_fullhd_screenshot(url, save_path, wait_time=5):
    """
    Take a Full HD (1920x1080) screenshot of a web page.
    
    Args:
        url (str): The URL of the web page to capture. URLs without protocol
                   will automatically be prefixed with 'https://'.
        save_path (str): The file path where the screenshot will be saved.
        wait_time (int): Time in seconds to wait for the page to load before
                         taking the screenshot. Default is 5 seconds.
    
    Returns:
        None
    
    Raises:
        Exception: If there's an error during the screenshot process.
    """
    # Auto-fix URL
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--window-size=1920,1080")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        print(f"\nNavigating to {url}...")
        driver.get(url)
        print(f"Waiting {wait_time} seconds...")
        time.sleep(wait_time) 
        driver.save_screenshot(save_path)
        print(f"Saved to: {save_path}")
    except Exception as e:
        print(f"Error: {e}")
        raise
    finally:
        driver.quit()
