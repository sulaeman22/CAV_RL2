import torch
import torch.nn as nn
import torch.optim as optim
import gym
from GRL_Envs import EVSpecificEnv

class REINFORCE(nn.Module):
    def __init__(self, input_dim, action_dim):
        super(REINFORCE, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim)
        )

    def forward(self, x):
        return self.net(x)

env = EVSpecificEnv()
model = REINFORCE(env.observation_space.shape[0], env.action_space.n)
optimizer = optim.Adam(model.parameters(), lr=3e-4)
