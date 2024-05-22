import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms

# 设置超参数
batch_size = 32
learning_rate = 0.01
epochs = 100
input_size = 28 * 28
hidden_size1 = 400
hidden_size2 = 300
hidden_size3 = 200
hidden_size4 = 100

# 数据预处理
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# 定义五层全连接神经网络模型
class FCN(nn.Module):
    def __init__(self, input_size, hidden_size1, hidden_size2, hidden_size3, hidden_size4, output_size=10):
        super(FCN, self).__init__()

        self.fc_layers = nn.Sequential(
            nn.Linear(input_size, hidden_size1),
            nn.ReLU(),
            nn.BatchNorm1d(hidden_size1),

            nn.Linear(hidden_size1, hidden_size2),
            nn.ReLU(),
            nn.BatchNorm1d(hidden_size2),

            nn.Linear(hidden_size2, hidden_size3),
            nn.ReLU(),
            nn.BatchNorm1d(hidden_size3),

            nn.Linear(hidden_size3, hidden_size4),
            nn.ReLU(),
            nn.BatchNorm1d(hidden_size4),

            nn.Linear(hidden_size4, output_size)
        )

    def forward(self, x):
        x = x.view(-1, input_size)
        out = self.fc_layers(x)
        return out

model = FCN(input_size, hidden_size1, hidden_size2, hidden_size3, hidden_size4)

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# 训练循环
for epoch in range(epochs):
    running_loss = 0.0
    for i, (images, labels) in enumerate(train_loader):
        images, labels = images, labels.long()

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    print(f'Epoch [{epoch + 1}/{epochs}], Loss: {running_loss / len(train_loader)}')

print('Training completed.')

# 测试模型性能（可选）
with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in test_loader:
        images, labels = images, labels.long()
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    print(f'Test Accuracy: {correct / total * 100}%')




