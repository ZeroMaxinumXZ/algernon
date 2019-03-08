import pyscreenshot as screen
from PIL import Image
import numpy as np
from time import sleep
import json

mouseX = []
mouseY = []

def screen_size():
    return 192, 108

#def get_screen_text():
#    img = screen.grab()
#    return pytesseract.image_to_string(img)

def get_screen():
    img = screen.grab()
    img = img.resize(screen_size())
    img = img.convert('L')
    img = np.array(img)
    return img

def xystoreandcheck(x, y, reward):
    global mouseX
    mouseX.append(x)
    global mouseY
    mouseY.append(y)
    try:
        if mouseX[0] == mouseX[1] or mouseX[2] == mouseX[0]:
            reward += -2.00
            print("Actor reward is now " + str(reward) + " due to agent failing to move mouse pointer in X coords.")
        if mouseY[0] == mouseY[1] or mouseY[2] == mouseY[0]:
            reward += -2.00
            print("Actor reward is now " + str(reward) + " due to agent failing to move mouse pointer in Y coord.")
        del mouseX[:-4]
        del mouseY[:-4]
        return reward
    except IndexError as error:
        return reward
