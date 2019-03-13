from utils import *
from actions import *

import tensorforce
from tensorforce.agents import DQNAgent as DQN
from time import sleep as wait
from os import getcwd
from os.path import join
from tensorforce.agents import Agent
from math import ceil

def agent_build():
    clear()
    user_input = input('Do you want to create a new model or just use a pre-existing model? ("create", "use"): ')
    while user_input != 'use' and user_input != 'create':
        user_input = input('Invalid response. Do you want to create a new model or just use a pre-existing model? ("create", "use"): ')
    if user_input == 'use':
        print('Loading model.')
        wait(1)
        clear()
        network = [
            dict(type='conv1d', size=128, activation='swish'),
            dict(type='conv1d', size=128, activation='swish'),
            dict(type='conv1d', size=128, activation='swish'),
            dict(type='conv1d', size=128, activation='swish'),
            dict(type='conv1d', size=128, activation='swish'),
            dict(type='flatten'),
            dict(type='dense', size=32, activation='swish')
            #dict(type='dense', size=16, activation='swish'),
            #dict(type='dense', size=16, activation='swish')
            ]
        agent = DQN(
            states=dict(type='float', shape=(screen_size()[1], screen_size()[0])),
            actions=dict(type='int', num_actions=ceil(act_screen_size()[1]*.001)*1000),
            batching_capacity = 1,
            update_mode = dict(units='episodes', batch_size=1, frequency=1),
            network = network,
            actions_exploration = 'epsilon_decay'
        )
        agent.restore_model(join(getcwd(), "models"))
        print("Agent loaded successfully...")

    if user_input == 'create':
        print('Creating model.')
        wait(1)
        clear()
        network = [
            dict(type='conv1d', size=128, activation='swish'),
            dict(type='conv1d', size=128, activation='swish'),
            dict(type='conv1d', size=128, activation='swish'),
            dict(type='conv1d', size=128, activation='swish'),
            dict(type='conv1d', size=128, activation='swish'),
            dict(type='flatten'),
            dict(type='dense', size=32, activation='swish')
            #dict(type='dense', size=16, activation='swish'),
            #dict(type='dense', size=16, activation='swish')
            ]

        print("Creating agent.")
        agent = DQN(
            states=dict(type='float', #Int may be more appropriate...
                        shape=(screen_size()[1], screen_size()[0])),
            actions=dict(type='int', num_actions=ceil(act_screen_size()[1]*.001)*1000),
            network=network,
            update_mode = dict(units='episodes', batch_size=1, frequency=1),
            batching_capacity = 1,
            actions_exploration = 'epsilon_decay'
        )
    return agent
