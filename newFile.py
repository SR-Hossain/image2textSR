import pyscreenshot as ImageGrab
from pynput import mouse
from PIL import Image
import pytesseract
import pyperclip
import pyautogui
import pygetwindow as gw

# Initialize the overlay window
overlay = pyautogui.screenshot(region=(0, 0, pyautogui.size().width, pyautogui.size().height))
overlay = Image.new("RGBA", overlay.size, (255, 255, 255, 0))

start_x, start_y = None, None
end_x, end_y = None, None

# Create a transparent overlay window
overlay_window = gw.ImageBox(
    overlay,
    "Overlay",
    (0, 0),
    img_path=None,
    img_scale=None,
    img_offset=None,
    delay=0,
    box_zoom=1,
)

def on_click(x, y, button, pressed):
    global start_x, start_y, end_x, end_y

    if pressed:
        # Record the starting position when the mouse button is pressed.
        start_x, start_y = x, y
    else:
        # Record the ending position when the mouse button is released.
        end_x, end_y = x, y

        # Capture the screen region defined by the start and end coordinates.
        if start_x is not None and start_y is not None and end_x is not None and end_y is not None:
            x1, x2 = min(start_x, end_x), max(start_x, end_x)
            y1, y2 = min(start_y, end_y), max(start_y, end_y)
            capture = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            capture.save("screenshot.png")
            extracted_text = pytesseract.image_to_string(Image.open('screenshot.png'))
            pyperclip.copy(extracted_text)

            # Terminate the program here
            overlay_window.close()
            exit()

# Start listening for mouse events.
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# Keep the overlay window on top
overlay_window.top()

# Keep the script running.
mouse_listener.join()
