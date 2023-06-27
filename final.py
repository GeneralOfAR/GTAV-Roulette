# tweak values of confidence in image recognition to fix bugs, depends on your table

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

times_ran = 1

while True:

    if pyautogui.locateOnScreen('time.png', confidence=0.9) is not None:
        print("test 1")
        if times_ran == 3:
            times_ran += 1
            if pyautogui.locateOnScreen('doublezero.png', confidence=0.9) is not None:
                print("winning")
                x, y = pyautogui.locateCenterOnScreen('doublezero.png', confidence=0.7)
                click(x, y)
                time.sleep(0.5)

        if times_ran == 2:
            times_ran += 1
            if pyautogui.locateOnScreen('doublezero.png', confidence=0.9) is not None:
                print("winning")
                x, y = pyautogui.locateCenterOnScreen('doublezero.png', confidence=0.7)
                click(x, y)
                time.sleep(0.5)

        if times_ran == 1:
            times_ran += 1
            if pyautogui.locateOnScreen('singlezero.png', confidence=0.9) is not None:
                print("losing")
                x, y = pyautogui.locateCenterOnScreen('singlezero.png', confidence=0.7)
                click(x, y)
                time.sleep(0.5)

    time.sleep(3)

    # function to stop when the script doesn't need to be running (turned off completely)
    if keyboard.is_pressed('j'):
        print("Aborting...")
        break

    if times_ran == 4:
        times_ran = 1
