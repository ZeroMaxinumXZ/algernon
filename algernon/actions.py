from pyautogui import click
from pyautogui import moveTo
from pyautogui import position, press
from math import ceil
from utils import act_screen_size

def bounds(action, bound1, bound2):
    if action >= bound1 and action <= bound2:
         return True
    else:
         return False

def actionizer(act_click, act_vert, act_horiz, act_type, reward = 0, prev_x = None, prev_y = None):
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
    
    screen_type_act_num = act_screen_size()[1] // 6
    if act_type <= screen_h:
        press('command')
    elif act_type <= screen_h * 2:
        press('up')
    elif act_type <= screen_h * 3:
        press('left')
    elif act_type <= screen_h * 4:
        press('right')
    elif act_type <= screen_h * 5:
        press('down')
    elif act_type <= screen_h * 6:
        pass
    print("Agent will move to y: " + str(y))
    fakey = y

    moveTo(x, y, 1)
    return fakex, fakey
