import torch
import torch.nn as nn
import torch.optim as optim
from GRL_Envs import EVEnv
import numpy as np

class ActorCritic(nn.Module):
    def __init__(self, input_dim, action_dim):
        super(ActorCritic, self).__init__()
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

def train(env, model, optimizer, num_episodes=1000):
    for episode in range(num_episodes):
        state = env.reset()
        done = False
        while not done:
            state = torch.FloatTensor(state.flatten())
            logits, value = model(state)
            dist = torch.distributions.Categorical(logits=logits)
            action = dist.sample()
            next_state, reward, done, _ = env.step(action.item())
            next_state = torch.FloatTensor(next_state.flatten())
            _, next_value = model(next_state)
            
            # Compute advantage
            advantage = reward + 0.99 * next_value - value
            actor_loss = -(dist.log_prob(action) * advantage).mean()
            critic_loss = advantage.pow(2).mean()
            
            loss = actor_loss + critic_loss
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            state = next_state

if __name__ == "__main__":
    env = EVEnv(config_file="path/to/your/sumo/config/file.sumocfg")
    model = ActorCritic(env.observation_space.shape[0] * env.observation_space.shape[1] * env.observation_space.shape[2], env.action_space.n)
    optimizer = optim.Adam(model.parameters(), lr=3e-4)
    train(env, model, optimizer)
