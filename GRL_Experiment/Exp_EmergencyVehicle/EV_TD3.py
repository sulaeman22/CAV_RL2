import torch
import torch.nn as nn
import torch.optim as optim
import gym
from GRL_Envs import EVSpecificEnv

class TD3Actor(nn.Module):
    def __init__(self, input_dim, action_dim):
        super(TD3Actor, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Tanh()
        )

    def forward(self, x):
        return self.net(x)

class TD3Critic(nn.Module):
    def __init__(self, input_dim, action_dim):
        super(TD3Critic, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim + action_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 1)
        )

    def forward(self, x, a):
        return self.net(torch.cat([x, a], 1))

env = EVSpecificEnv()
actor = TD3Actor(env.observation_space.shape[0], env.action_space.shape[0])
critic1 = TD3Critic(env.observation_space.shape[0], env.action_space.shape[0])
critic2 = TD3Critic(env.observation_space.shape[0], env.action_space.shape[0])
actor_optimizer = optim.Adam(actor.parameters(), lr=3e-4)
critic1_optimizer = optim.Adam(critic1.parameters(), lr=3e-4)
critic2_optimizer = optim.Adam(critic2.parameters(), lr=3e-4)
