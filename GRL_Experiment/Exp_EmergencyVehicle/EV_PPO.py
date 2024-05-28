import torch
import torch.nn as nn
import torch.optim as optim
import gym
from GRL_Envs import EVSpecificEnv

class PPOActorCritic(nn.Module):
    def __init__(self, input_dim, action_dim):
        super(PPOActorCritic, self).__init__()
        self.actor = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim)
        )
        self.critic = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, x):
        return self.actor(x), self.critic(x)

env = EVSpecificEnv()
model = PPOActorCritic(env.observation_space.shape[0], env.action_space.n)
optimizer = optim.Adam(model.parameters(), lr=3e-4)
