#! python3
# pyautoguiGetScreenSize.py - an example on how to get the screen size

import pyautogui
import time
# have the program sleep for 3 seconds so that i can bring up the text editor
time.sleep(3)

print(pyautogui.size())

# demo of mouse moving in a rectangle
for i in range(5):
    pyautogui.moveTo(100, 100, duration=.25)
    pyautogui.moveTo(200, 100, duration=.25)
    pyautogui.moveTo(200, 200, duration=.25)
    pyautogui.moveTo(100, 200, duration=.25)


# demo of mouse moving in a rectange from where the mouse is at currently
for i in range(5):
    pyautogui.moveRel(100, 0, duration=.25)
    pyautogui.moveRel(0, 100, duration=.25)
    pyautogui.moveRel(-100, 0, duration=.25)
    pyautogui.moveRel(0, -100, duration=.25)

# get the mouse position
pyautogui.position()


# how to send a left click
pyautogui.click(10,5)
# there is also doubleClick, mouseUp, mouseDown, rightClick, and .scroll methods

# how to send keyboard interactions via pyautogui
pyautogui.click(50,50, duration=.25); pyautogui.typewrite('Hello World', .25)

# these are the different keys that can be pressed
print(pyautogui.KEYBOARD_KEYS)

# to type a "$" this is how it could be done
pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

# this presses a hotkey
pyautogui.hotkey('ctrl', 'c')
