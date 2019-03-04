from agent import *
from utils import *
from rewarders import *

from os import system

def main_loop(agent):
    system("clear")
    print("-" * 30) 
    timer = 10
    
    print("Control-C to quit.")
    print("Try moving to the top-left corner of screen if AI gets somewhere it shouldn't, lol... Restart your computer if it doesn't work.")
    print("This is an experimental reinforcement-learning AI that controls mouse input.")
    
    print("Timer in case you want to quit this program: ")
    while timer != 0:
        print(str(timer) + '...')
        wait(1)
        timer -= 1
    print("Entering main agent loop")
    while True:
        img = get_screen()
        #text = get_screen_text()
        action1 = agent.act(states=get_screen())
        action2 = agent.act(states=get_screen())
        action3 = agent.act(states=get_screen())
        action_sum = action1 + action2 + action3
        #action4 = agent.act(states=get_screen())
        reward, x, y = actionizer(action1,action2, action3)
        reward = smart_rewarder(reward, action_sum)
        #rwward = object_rewarder(reward, img)
        reward = xystoreandcheck(x, y, reward)
        agent.observe(reward=reward, terminal=False)
        #agent.save_model(join(getcwd(), "models", "model"))

agent = agent_build()
main_loop(agent)
