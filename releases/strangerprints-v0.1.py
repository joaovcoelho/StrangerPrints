import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def take_fullhd_screenshot(url, save_path, wait_time=5):
    # Auto-fix URL
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    # Setup
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
    finally:
        driver.quit()

def user_input():
    target_url = input("\nURL (or 'exit'): ").strip()
    if target_url.lower() in ['sair', 'exit', 'quit']: return False

    output_file = input("Filename: ").strip()
    if not output_file.endswith(".png"): output_file += ".png"

    try:
        wait = int(input("Wait time (s): "))
    except ValueError:
        wait = 5

    take_fullhd_screenshot(target_url, output_file, wait_time=wait)
    return True

if __name__ == "__main__":
    running = True
    while running:
        running = user_input()