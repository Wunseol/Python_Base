# 设计一个卷积神经网络(结构如下)，实现MNIST手写数字识别。
# Net(
#     (conv1):Conv2d(1, 32, kernel_size=(3, 3),stride=(1, 1))
#     (conv2): Conv2d(32, 64, kernel_size=(3, 3), stride=(1, 1))
#     (dropout1): Dropout2d(P=0.25, inplace=False)
#     (dropout2): Dropout2d(p=0.5, inplace= False)
#     (fe1): Linear(in_features=9216, out_features=128, bias=True)
#     (fc2): Linear(in_features=128, out_features=10, bias=True)
# )

import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import numpy as np

# 定义卷积神经网络模型
class MNISTClassifier(nn.Module):
    def __init__(self):
        super(MNISTClassifier, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1)
        self.dropout1 = nn.Dropout2d(p=0.25)
        self.dropout2 = nn.Dropout2d(p=0.5)
        self.fc1 = nn.Linear(9216, 128)  # 假设经过卷积和池化后的特征图尺寸得到的线性层输入大小
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = torch.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = x.view(-1, 9216)  # Flatten
        x = torch.relu(self.fc1(x))
        x = self.dropout2(x)
        x = self.fc2(x)
        return torch.log_softmax(x, dim=1)

# 数据预处理与加载
def load_data():
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])
    train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
    test_dataset = datasets.MNIST('./data', train=False, download=True, transform=transform)
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=True)
    return train_loader, test_loader

# 训练模型
def train_model(model, train_loader, criterion, optimizer, device, num_epochs):
    for epoch in range(num_epochs):
        model.train()
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}/{num_epochs}")

# 测试模型
def test_model(model, test_loader, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = 100 * correct / total
    print(f"Accuracy on 10000 test images: {accuracy}%")

def visualize_predictions(model, test_loader, device, num_images=10):
    model.eval()
    fig = plt.figure(figsize=(10, 10))
    
    # 计算所需的最大行数，保证不超过num_images
    num_rows = (num_images + 1) // 2 if num_images % 2 != 0 else num_images // 2
    for i, (images, labels) in enumerate(test_loader):
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, preds = torch.max(outputs, 1)
        
        for j in range(min(images.size(0), num_images)):
            # 确保子图索引不超过总图数量
            ax = plt.subplot(num_rows, 2, j + 1)
            ax.axis('off')
            ax.set_title(f'Actual: {labels[j].item()} \n Predicted: {preds[j].item()}')
            image_np = images.cpu().numpy()[j].transpose((1, 2, 0))
            image_np = np.clip(image_np, 0, 1)
            plt.imshow(image_np)
            
            # 一旦达到num_images就跳出循环
            if j + 1 == num_images:
                break
        
        # 所有需要的图像已经绘制完成，退出循环
        if j + 1 == num_images:
            break
    
    plt.tight_layout()
    plt.show()

# 主程序
if __name__ == "__main__":
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = MNISTClassifier().to(device)
    train_loader, test_loader = load_data()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    num_epochs = 10

    train_model(model, train_loader, criterion, optimizer, device, num_epochs)
    test_model(model, test_loader, device)
    visualize_predictions(model, test_loader, device)

