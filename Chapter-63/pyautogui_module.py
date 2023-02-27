#  pyautogui is a module used to control mouse and keyboard. This module is basically used to automate mouse click and keyboard press tasks.
# Used to programmatically control the mouse & keyboard.

import pyautogui

# mouse functions
pyautogui.write('Hello world!', interval=0.25)
pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.