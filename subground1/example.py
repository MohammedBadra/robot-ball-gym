import pyvirtualdisplay


_display = pyvirtualdisplay.Display(visible=False,  # use False with Xvfb
                                    size=(1400, 900))
_ = _display.start()


import time
import gymnasium as gym
env = gym.make("FetchPickAndPlace-v2", render_mode = "human")
observation, info = env.reset(seed = 42)
for _ in range(1000):
   action = policy(observation)  # User-defined policy function
   observation, reward, terminated, truncated, info = env.step(action)

   if terminated or truncated:
      observation, info = env.reset()

time.sleep(10)
# env.close()