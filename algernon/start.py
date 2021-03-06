from agent import *
from utils import *
from rewarders import *
from os import system

if False: 
    curiousity_engine = keras.models.load_model(join(getcwd(), "curiousity_engine_models", 'model.h5'))
    print("Curiousity engine model loaded successfully.")
if True:
    print("Building curiousity engine.") 
    curiousity_engine = model_build()

curiousity_engine.compile(optimizer = 'adam', loss='mean_squared_logarithmic_error')


def main_loop(agent):
    system("clear")
    print("-" * 30) 
    timer = 30
    
    print("Control-C to quit.")
    print("This is Algernon, an experimental reinforcement-learning AI that controls mouse input.")
    print("Instructions for quitting: \nForce the mouse to the top-left corner of the screen, or just tap Control-C on your keyboard.")
    print("Timer in case you want to quit this program: ")
    while timer != 0:
        print(str(timer) + '...')
        wait(1)
        timer -= 1
    print("Entering main agent loop")
    acc  = 0
    while True:
        img = get_screen()
        #text = get_screen_text()
        action1 = agent.act(states=get_screen())
        action2 = agent.act(states=get_screen())
        action3 = agent.act(states=get_screen())
        action4 = agent.act(states=get_screen())
        x, y = actionizer(action1, action2, action3, action4)
        reward = curiousity_rewarder(action1, action2, action3, action4, curiousity_engine)
        #rwward = object_rewarder(reward, img)
        #reward = xystoreandcheck(x, y, reward)
        agent.observe(reward=reward, terminal=False)

        acc += 1
        if acc == 20: 
            acc = 0 
            print("Saving...")
            agent.save_model(join(getcwd(), "models", "model"), append_timestep=False)
            curiousity_engine.save(join(getcwd(), "curiousity_engine_models", 'model.h5'))


agent = agent_build()
main_loop(agent)
