from pyautogui import click
from pyautogui import moveTo
from pyautogui import position, press

def bounds(action, bound1, bound2):
    if action >= bound1 and action <= bound2:
         return True
    else:
         return False

def actionizer(act_click, act_vert, act_horiz, act_type, reward = 0, prev_x = None, prev_y = None):
    if act_click <= 1000:
        #reward += 0.01
        click()
        print("Agent has clicked.")
    else:
        temp = 0
        #reward -= 0.01
    if act_horiz <= 1920:
        x = act_horiz
        print("Agent will move to x: " + str(x))
        #reward += 0.001
        fakex = x
    else:
        print("Agent will do nothing in x.")
        #reward = -1
        x = None
        fakex = -1
    if act_type <= 333:
        press('command')
    elif act_type <= 666:
        press('up')
    elif act_type <= 999:
        press('left')
    elif act_type <= 1332:
        press('right')
    elif act_type <= 1665:
        press('down')
    elif act_type <= 2000:
        pass
    y = act_vert // 2
    print("Agent will move to y: " + str(y))
    fakey = y

    moveTo(x, y, 1)
    return fakex, fakey

