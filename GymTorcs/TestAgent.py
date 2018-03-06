from gym_torcs import TorcsEnv
import numpy as np 



en=TorcsEnv(vision=True, )

#print(en.vision)
#en.reset()
obs,reward,done,_ = en.step(np.tanh(np.random.rand(1)))
focus, speedX, speedY, speedZ, opponents, rpm, track, wheelSpinVel, vision = ob
print(vision)
