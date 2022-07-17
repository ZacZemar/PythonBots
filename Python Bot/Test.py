import pyautogui

#First is the x pos the screenshot starts on, 2nd is the y, 
#3rd is the width of the image, 4th is the height of the image
iml  = pyautogui.screenshot(region=(585, 422, 751, 530))
iml.save(r"C:\Users\zacze\OneDrive\Desktop\Python Bot\AimBooster.png")