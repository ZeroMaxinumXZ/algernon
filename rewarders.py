from agent import *
from utils import get_screen as env
from random import uniform
agent_rewards = smart_rewarder_build()

def smart_rewarder(rewards, actions = 0.01):
    action = agent_rewards.act(states=env())
    rewards += action - 5
    print("Actor rewards: " + str(rewards))
    SARrewards = (0.0001 * actions)
    #SARrewards = 0
    print("Smart rewarder's rewards: " + str(SARrewards))
    agent_rewards.observe(reward=SARrewards, terminal=False)
    return rewards
