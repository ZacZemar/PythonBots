#Bot that can detect if an image is present on the screen

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    #Using built in function checks on screen if it can see the image on the png file
    #Use the confidence parameter to account for slight difference in image,
    #especially in real time changes
    #0.8 means 80% confidence
    if pyautogui.locateOnScreen('stickman.png', region=(13,311,618,423), grayscale = True, confidence = 0.8) != None:
        print("I can see")
        time.sleep(0.5)
    else:
        print("I cant see it")
        time.sleep(0.5)