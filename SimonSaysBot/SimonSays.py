from logging.config import listen
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    #We say leftdown because we click with the left part of our mouse 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.01) #Pauses script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

def colorcheck(x, listen):
    if pyautogui.pixel(762, 589) [0] != 19: #green
        while pyautogui.pixel(762, 589) [0] != 19:
            time.sleep(0.05)
        print("Green")
        x+=1
        if x > len(color_to_press):
            color_to_press.append(1)
            listen = False
    if pyautogui.pixel(933, 573) [0] != 166: #yellow
        while pyautogui.pixel(933, 573) [0] != 166:
            time.sleep(0.05)
        print("Yellow")
        x+=1
        if x > len(color_to_press):
            color_to_press.append(2)
            listen = False
    if pyautogui.pixel(784, 739) [0] != 57: #blue
        while pyautogui.pixel(784, 739) [0] != 57:
            time.sleep(0.05)
        print("Blue")
        x+=1
        if x > len(color_to_press):
            color_to_press.append(3)
            listen = False
    if pyautogui.pixel(935, 762) [0] != 187: #red
        while pyautogui.pixel(935, 762) [0] != 187:
            time.sleep(0.05)
        print("Red")
        x+=1
        if x > len(color_to_press):
            color_to_press.append(4)
            listen = False
    return x, listen 

color_to_press = []

x = 0
listen = True

while 1:
    if keyboard.is_pressed('q'):
        while 1:
            if listen:
                x, listen = colorcheck(x,listen)
            else:
                for number in color_to_press:
                    if number==1:
                        click(762, 589)
                    if number==2:
                        click(933, 573)
                    if number==3:
                        click(784, 739)
                    if number==4:
                        click(935, 762)
                time.sleep(0.2)
                listen = True
                x = 0
