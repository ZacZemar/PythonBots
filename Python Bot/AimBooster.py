#Aim Booster Link http://www.aimbooster.com/

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    #We say leftdown because we click with the left part of our mouse 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.01) #Pauses script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

while keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(585, 422, 751, 530))

    width, height = pic.size
    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = pic.getpixel((x, y))
            if b == 195 and r == 255 and g == 219:
                flag = 1
                click(x + 585, y + 422)
                time.sleep(0.05)
                break
        if flag == 1:
            break