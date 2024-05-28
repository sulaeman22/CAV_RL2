import torch
import torch.nn as nn

class EVNetwork(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(EVNetwork, self).__init__()
        self.gcn = GCN(input_dim, hidden_dim)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x, adj):
        x = self.gcn(x, adj)
        x = self.fc(x)
        return x

class GCN(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(GCN, self).__init__()
        self.conv1 = nn.Linear(input_dim, hidden_dim)
        self.conv2 = nn.Linear(hidden_dim, hidden_dim)

    def forward(self, x, adj):
        x = torch.relu(self.conv1(torch.matmul(adj, x)))
        x = self.conv2(torch.matmul(adj, x))
        return x
