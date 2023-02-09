import time

import pyautogui


def unMaximizeChrome(x, y):
    lastPosition = pyautogui.position()
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.moveTo(lastPosition)
    print("unmaximizing chrome")