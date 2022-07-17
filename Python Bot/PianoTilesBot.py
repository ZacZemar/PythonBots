#This is a simple piano tiles bot 
#Grab the position of all four tiles bottom tiles using pyautogui.displayMousePosition()
#Create a click function that will constantly press down on the x, y coord set 
# then "move them up" with a 0.01 pause to account for error if the clicks are too fast
#Link to go to the piano tiles https://www.agame.com/game/magic-piano-tiles


from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 Position: X: 530   Y: 400    RGB: (156, 161, 231)
#Tile 2 Position: X: 606   Y: 400    RGB: (155, 161, 230)
#Tile 3 Position: X: 729   Y: 400    RGB: (168, 172, 232)
#Tile 4 Position: X: 865   Y: 400    RGB: (253,  18,   1)

#2 second delay to set it

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    #We say leftdown because we click with the left part of our mouse 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.01) #Pauses script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

#While q is pressed down returns True could use any letter 
#This will allow me to stop bot
while keyboard.is_pressed('q') == False:
    #Checks if R value is 0 (in this case black)
    #The [0] checks for R(red) value
    if pyautogui.pixel(530, 400) [0] == 0:
        #Once the script can tell its black we want it to click
        #the instant it does
        click(530, 400)
    if pyautogui.pixel(606, 400) [0] == 0:
        click(606, 400)
    if pyautogui.pixel(729, 400) [0] == 0:
        click(729, 400)
    if pyautogui.pixel(865, 400) [0] == 0:
        click(865, 400)

#Could possibly create another part of the bot to where if any of the bottom tiles are red 
#which signifies that the game is over then create a script to auto run it back 
#maybe make script to make ads


    
