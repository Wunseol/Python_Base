import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Step 1: Generate random dataset
np.random.seed(42)
n_samples = 1000
input_dim = 1  # For simplicity, we'll use a single input feature
output_dim = 1  # Our regression target is a scalar value

X = np.random.rand(n_samples, input_dim)  # Random inputs
true_w = np.array([2.0])  # True weight for the linear relationship
true_b = np.array([0.5])  # True bias

noise_std = 0.1  # Add some noise to the targets
y = X @ true_w + true_b + np.random.normal(scale=noise_std, size=(n_samples,))

# Convert to PyTorch tensors
X = torch.from_numpy(X).float()
y = torch.from_numpy(y).float()

# Split into training and test sets
train_ratio = 0.8
train_split_idx = int(n_samples * train_ratio)

X_train, y_train = X[:train_split_idx], y[:train_split_idx]
X_test, y_test = X[train_split_idx:], y[train_split_idx:]

# Step 2: Define the model structure
class LinearRegression(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.linear(x)

model = LinearRegression(input_dim, output_dim)

# Step 3: Set up loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Step 4: Train the model
num_epochs = 100
for epoch in range(num_epochs):
    optimizer.zero_grad()  # Zero out the gradients before each epoch

    # Forward pass
    predictions = model(X_train)

    # Compute and print loss
    loss = criterion(predictions, y_train)
    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch + 1}/{num_epochs}, Loss: {loss.item():.4f}")

    # Backward pass and optimization step
    loss.backward()
    optimizer.step()

# Step 5: Evaluate the model on the test set
with torch.no_grad():
    test_predictions = model(X_test)
    test_loss = criterion(test_predictions, y_test)
print("\nTest Loss:", test_loss.item())

print("\nTrue weights:", true_w, "\nTrue bias:", true_b)
print("Learned weights:", model.linear.weight.item(), "\nLearned bias:", model.linear.bias.item())