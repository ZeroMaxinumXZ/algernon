from agent import *
from utils import get_screen as env
from random import uniform
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers.convolutional import Conv1D
from keras import backend as K

def swisher(x):
    return K.sigmoid(x) * x * x

def model_build():
    model = Sequential()
    model.add(Conv1D(filters=256 * 3, kernel_size=5, strides=1, activation=swisher))
    model.add(Conv1D(filters=256 * 2, kernel_size=5, strides=1, activation=swisher))
    model.add(Flatten())
    #model.add(Dense(256 * 5, activation='sigmoid'))
    #model.add(Dense(256 * 3, activation='relu'))
    #model.add(Dense(256 * 2, activation='sigmoid'))
    model.add(Dense(256 * 1, activation='sigmoid'))
    model.add(Dense(4))
    return model

def curiousity_rewarder(action1, action2, action3, action4, model, rewards=0.0):
    y = np.array([[action1, action2, action3, action4]])
    history = model.fit(x=np.array([env()]), y = y)
    loss = history.history['loss'][0]
    rewards = (loss * .01)
    return rewards
