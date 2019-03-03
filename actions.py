from pyautogui import click
from pyautogui import moveTo
from pyautogui import position

def bounds(action, bound1, bound2):
    if action >= bound1 and action <= bound2:
         return True
    else:
         return False

def actionizer(act_click, act_vert, act_horiz, reward = 0, prev_x = None, prev_y = None):
    if act_click <= 1000:
        reward += 0.01
        click()
        print("Agent has clicked.")
    else:
        reward += 0
    if act_vert <= 980 and act_vert >= 100:
        y = act_vert
        print("Agent will move to y: " + str(y))
        reward += 0.001
        fakey = y
    else:
        print("Agent will do nothing in y.") 
        reward = -1
        y = None
        fakey = -1
    if act_horiz <= 1920:
        x = act_horiz
        print("Agent will move to x: " + str(x))
        reward += 0.001
        fakex = x
    else:
        print("Agent will do nothing in x.")
        reward = -1
        x = None
        fakex = -1


    moveTo(x, y, 1)
    return reward, fakex, fakey


