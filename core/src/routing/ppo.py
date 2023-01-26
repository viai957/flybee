import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# Define the input and output data
data = torch.tensor(np.load('coordinates_distances.npy'), dtype=torch.float32)
X = data[:, :4]
y = data[:, 4:]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Define the model
class ShortestDistanceModel(nn.Module):
    def __init__(self):
        super(ShortestDistanceModel, self).__init__()
        self.layer1 = nn.Linear(4, 32)
        self.layer2 = nn.Linear(32, 64)
        self.layer3 = nn.Linear(64, 128)
        self.output = nn.Linear(128, 1)

    def forward(self, x):
        x = torch.relu(self.layer1(x))
        x = torch.relu(self.layer2(x))
        x = torch.relu(self.layer3(x))
        x = self.output(x)
        return x

model = ShortestDistanceModel()

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters())

# Define the DataLoader for training data
train_data = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)

# Train the model
for epoch in range(100):
    for i, (x, y) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(x)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()

# Make predictions on new data
new_data = torch.tensor([[12.9716, 77.5946, 13.0827, 80.2707]], dtype=torch.float32)
predictions = model(new_data)
print("Shortest Distance:", predictions)
