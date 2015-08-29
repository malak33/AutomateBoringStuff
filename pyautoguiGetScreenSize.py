#! python3
# pyautoguiGetScreenSize.py - an example on how to get the screen size

import pyautogui
print(pyautogui.size())

"""
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
"""
# get the mouse position
pyautogui.position()


# how to send a left click
pyautogui.click(10,5)
# there is also doubleClick, mouseUp, mouseDown, rightClick methods

