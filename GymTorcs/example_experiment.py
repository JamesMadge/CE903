from gym_torcs import TorcsEnv
from sample_agent import Agent
import numpy as np
import scipy.misc
vision = True
episode_count = 100
max_steps = 20
reward = 0
done = False
step = 0
file=open("Torcs_Test.txt","w")
# Generate a Torcs environment
env = TorcsEnv(vision=vision, throttle=False)

agent = Agent(1)  # steering only


print("TORCS Experiment Start.")
for i in range(episode_count):
    print("Episode : " + str(i))
    file.write(str(i)+"...............................\n")
    if np.mod(i, 3) == 0:
        #Sometimes you need to relaunch TORCS because of the memory leak error
        ob = env.reset(relaunch=True)
    else:
        ob = env.reset()
    file.write(ob.__repr__())
    file.write("\n")
    total_reward = 0.
    for j in range(max_steps):
        action = agent.act(ob, reward, done, vision)
        env.get_state()
        print(env.client.port)
        ob, reward, done, _ = env.make_action(action)
        #print(ob.keys())
        total_reward += reward

        step += 1
        if done:




            break

    print("TOTAL REWARD @ " + str(i) +" -th Episode  :  " + str(total_reward))
    print("Total Step: " + str(step))
    print("")

env.end()  # This is for shutting down TORCS
print("Finish.")
