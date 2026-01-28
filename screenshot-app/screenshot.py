import pyautogui
import os
from datetime import datetime
import time

def take_screenshot():
    
    print("Screenshot will be taken in 3 seconds...")
    time.sleep(3)
    
    folder_name = "image"
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Created folder: {folder_name}")
    
    # Generate timestamp for filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create filename with timestamp
    filename = f"{folder_name}/screenshot_{timestamp}.png"
    
    # Take screenshot and save it
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    
    print(f"Screenshot saved as: {filename}")

if __name__ == "__main__":
    take_screenshot()
