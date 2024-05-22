import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Step 1: 生成随机数据集
np.random.seed(42)
n_samples = 1000  # 数据样本数量
input_dim = 1     # 输入特征维度（此处仅使用一个特征）
output_dim = 1    # 输出目标维度（线性回归目标为一个标量）

X = np.random.rand(n_samples, input_dim)  # 随机生成输入特征
true_w = np.array([2.0])   # 真实权重值（线性关系中的斜率）
true_b = np.array([0.5])   # 真实偏置值（线性关系中的截距）

noise_std = 0.1  # 添加噪声的标准差
y = X @ true_w + true_b + np.random.normal(scale=noise_std, size=(n_samples,))  # 计算带噪声的目标值

# 将numpy数组转换为PyTorch张量
X = torch.from_numpy(X).float()
y = torch.from_numpy(y).float()

# 划分训练集和测试集
train_ratio = 0.8
train_split_idx = int(n_samples * train_ratio)

X_train, y_train = X[:train_split_idx], y[:train_split_idx]
X_test, y_test = X[train_split_idx:], y[train_split_idx:]

# Step 2: 定义模型结构
class LinearRegression(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.linear(x)

model = LinearRegression(input_dim, output_dim)

# Step 3: 设置损失函数和优化器
criterion = nn.MSELoss()  # 均方误差损失函数
optimizer = optim.SGD(model.parameters(), lr=0.01)  # 使用随机梯度下降优化器，学习率为0.01

# Step 4: 训练模型
num_epochs = 100  # 总训练轮数（epoch）
for epoch in range(num_epochs):
    optimizer.zero_grad()  # 每轮开始时清零梯度

    # 前向传播
    predictions = model(X_train)

    # 计算并打印损失
    loss = criterion(predictions, y_train)
    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch + 1}/{num_epochs}，损失: {loss.item():.4f}")

    # 反向传播及参数更新
    loss.backward()
    optimizer.step()

# Step 5: 在测试集上评估模型
with torch.no_grad():
    test_predictions = model(X_test)
    test_loss = criterion(test_predictions, y_test)
print("\n测试损失:", test_loss.item())

print("\n真实权重:", true_w, "\n真实偏置:", true_b)
print("学习到的权重:", model.linear.weight.item(), "\n学习到的偏置:", model.linear.bias.item())