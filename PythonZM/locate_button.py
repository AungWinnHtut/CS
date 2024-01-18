import pyautogui
import pygetwindow as gw
import time

def capture_screen_and_find_button():
    # Capture the screen
    screenshot = pyautogui.screenshot()

    # Find the "OK" button on the screen
    ok_button_location = pyautogui.locateOnScreen('ok.png', confidence=0.8)

    if ok_button_location:
        print("OK button found at:", ok_button_location)
        
        # You can click on the button if needed
        pyautogui.click(ok_button_location.left + ok_button_location.width / 2, 
                        ok_button_location.top + ok_button_location.height / 2)
    else:
        print("OK button not found.")

if __name__ == "__main__":
    # Replace 'YourSoftwareWindowTitle' with the actual title of the software window
    software_window_title = 'Open file'

    # Bring the software window to the front
    try:
        software_window = gw.getWindowsWithTitle(software_window_title)[0]
        software_window.activate()
    except IndexError:
        print(f"Window with title '{software_window_title}' not found.")
        exit()

    # Wait for the window to be in focus
    time.sleep(2)

    # Capture the screen and find the "OK" button
    capture_screen_and_find_button()
