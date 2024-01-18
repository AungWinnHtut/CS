import pyautogui
import pygetwindow as gw
import time

def find_and_type_textbox(text_to_type,found_window):
    # Find the active window
    active_window = found_window #gw.getActiveWindow()

    if active_window is None:
        print("No active window found.")
        print("Open windows:")
        
        for window in gw.getAllWindows():
            print(window.title)
        return

    # Wait for the window to be in focus
    time.sleep(2)

    # Find the text box with placeholder "Type a message..."
    text_box_location = pyautogui.locateOnScreen('search.png', confidence=0.8)

    if text_box_location:
        print("Text box found at:", text_box_location)
        
        # Click on the text box to focus on it
        pyautogui.click(text_box_location.left + text_box_location.width / 2,
                        text_box_location.top + text_box_location.height / 2)

        # Type the text into the text box
        pyautogui.write(text_to_type)
    else:
        print("Text box with placeholder 'Type a message...' not found.")

if __name__ == "__main__":
    # Replace 'YourSoftwareWindowTitle' with the actual title of the software window
    software_window_title = 'Rakuten Viber'

    # Bring the software window to the front
    try:
        software_window = gw.getWindowsWithTitle(software_window_title)[0]
        software_window.activate()
        find_and_type_textbox("ZinMin",software_window)
    except IndexError:
        print(f"Window with title '{software_window_title}' not found.")
        print("Open windows:")
        for window in gw.getWindows():
            print(window.title)
            if window.title == 'Rakuten Viber':
                print('Found')
                window.activate()
                find_and_type_textbox("Zin Min",window)
        

    # Enter "1234" in the text box with placeholder "Type a message..."
    
