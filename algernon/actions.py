from pyautogui import click
from pyautogui import moveTo
from pyautogui import position, press
from math import ceil
from utils import act_screen_size
from keyboard import keys
from numpy.random import randint


def bounds(action, bound1, bound2):
    if action >= bound1 and action <= bound2:
         return True
    else:
         return False

def actionizer(act_click, act_vert, act_horiz, act_type, reward = 0, prev_x = None, prev_y = None, acc = 0):
    if act_click <= ceil(act_screen_size()[1]) // 2:
        #reward += 0.01
        click()
        print("Agent has clicked.")
    else:
        temp = 0
        #reward -= 0.01
    if act_horiz <= act_screen_size()[1]:
        x = act_horiz 
        print("Agent will move to x: " + str(x))
        #reward += 0.001
        fakex = x
    else:
        print("Agent will do nothing in x.")
        #reward = -1
        x = None
        fakex = -1
    
    y = act_vert // 2
    
    screen_h = act_screen_size()[1] // len(keys())
    for i, key in enumerate(keys(), start = 1):
        if act_type <= i * screen_h:
            press(key)
            print("Agent has pressed " + key)
            break
            
    print("Agent will move to y: " + str(y))
    fakey = y

    moveTo(x, y, .5)
    return fakex, fakey
