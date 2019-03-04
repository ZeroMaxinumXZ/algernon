from utils import *
from actions import *

import tensorforce
from tensorforce.agents import DQNAgent as DQN
from time import sleep as wait
from os import getcwd
from os.path import join
from tensorforce.agents import Agent

def agent_build():
    #try:
    #    agent = DQN.restore_model(join(getcwd(), "models"))
    #except:
    if True:
        network = [
            #dict(type='conv1d', size=256, window=1, stride=1),  
            dict(type='flatten'),
            dict(type='dense', size=1024, activation='swish'),
            dict(type='dense', size=1024, activation='swish')
            ]

        print("Creating agent.")
        agent = DQN(
            states=dict(type='float', #Int may be more appropriate...
                        shape=(screen_size()[1], screen_size()[0])),
            actions=dict(type='int', num_actions=2000),
            network=network,
            update_mode = dict(units='episodes', batch_size=1, frequency=1),
            batching_capacity = 32
        )
    return agent

def smart_rewarder_build():
    network = [
        dict(type='flatten'),
        dict(type='dense', size=512, activation='swish'),
        dict(type='dense', size=512, activation='swish')
            ]
    agent = DQN(
        states = dict(type='float', #Int may be more appropriate...
                      shape=(screen_size()[1], screen_size()[0])),
        actions = dict(type = 'int', num_actions=11), # -5...10
        network=network,
        action_exploration = tensorforce.core.exploration.
        )
    return agent
