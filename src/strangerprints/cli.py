"""
Command-line interface for StrangerPrints.
"""

from .renderer import take_fullhd_screenshot


def user_input():
    """
    Handle user input for screenshot generation.
    
    Returns:
        bool: False if user wants to exit, True to continue.
    """
    target_url = input("\nURL (or 'exit'): ").strip()
    if target_url.lower() in ['sair', 'exit', 'quit']: 
        return False

    output_file = input("Filename: ").strip()
    if not output_file.endswith(".png"): 
        output_file += ".png"

    try:
        wait = int(input("Wait time (s): "))
    except ValueError:
        wait = 5

    take_fullhd_screenshot(target_url, output_file, wait_time=wait)
    return True


def main():
    """
    Main entry point for the CLI application.
    """
    print("=" * 50)
    print("StrangerPrints - Browser Screenshot Renderer v1.0")
    print("=" * 50)
    
    running = True
    while running:
        running = user_input()
    
    print("\nThank you for using StrangerPrints!")


if __name__ == "__main__":
    main()
