import gym
from gym import spaces
import numpy as np

class EVBaseEnv(gym.Env):
    def __init__(self):
        super(EVBaseEnv, self).__init__()
        self.action_space = spaces.Discrete(3)  # Actions: stop, go, slow
        self.observation_space = spaces.Box(low=0, high=255, shape=(84, 84, 3), dtype=np.uint8)

    def reset(self):
        return np.zeros((84, 84, 3), dtype=np.uint8)

    def step(self, action):
        obs = np.zeros((84, 84, 3), dtype=np.uint8)
        reward = 0
        done = False
        info = {}
        return obs, reward, done, info

    def render(self, mode='human'):
        pass

    def close(self):
        pass
