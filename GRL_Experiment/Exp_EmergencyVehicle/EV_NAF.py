import torch
import torch.nn as nn
import torch.optim as optim
import gym
from GRL_Envs import EVSpecificEnv

class NAF(nn.Module):
    def __init__(self, input_dim, action_dim):
        super(NAF, self).__init__()
        self.feature = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU()
        )
        self.value = nn.Linear(128, 1)
        self.mu = nn.Linear(128, action_dim)
        self.L = nn.Linear(128, action_dim * (action_dim + 1) // 2)

    def forward(self, x):
        feature = self.feature(x)
        value = self.value(feature)
        mu = self.mu(feature)
        L = self.L(feature)
        return value, mu, L

env = EVSpecificEnv()
model = NAF(env.observation_space.shape[0], env.action_space.shape[0])
optimizer = optim.Adam(model.parameters(), lr=3e-4)
