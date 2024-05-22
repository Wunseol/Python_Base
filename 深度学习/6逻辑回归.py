import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# 定义模型参数
input_dim = 9000  # 每个样本的特征维度
output_dim = 1  # 输出维度（二分类问题）

# 生成模拟数据集
X_data = torch.from_numpy(np.random.randn(1000, input_dim)).float()  # 生成 torch.float32 类型的张量

# 初始化模型参数，确保它们与 X_data 的数据类型一致
slope = torch.randn(input_dim, output_dim, dtype=torch.float32)
intercept = torch.randn(output_dim, dtype=torch.float32)

# 计算真实标签
y_true = torch.sigmoid((X_data @ slope + intercept).sum(dim=1)) > 0.5  # 计算真实标签
y_true = y_true.to(torch.float32).unsqueeze(-1)  # 将 y_true 从布尔值转换为浮点数，并增加一个维度以适应后续操作

# 定义逻辑回归模型
class LogisticRegression(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LogisticRegression, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return torch.sigmoid(self.linear(x))

model = LogisticRegression(input_dim, output_dim)

# 定义损失函数和优化器
criterion = nn.BCELoss()  # 二元交叉熵损失函数
optimizer = optim.Adam(model.parameters(), lr=0.001)  # 使用 Adam 优化器

# 训练循环
num_epochs = 100
for epoch in range(num_epochs):
    optimizer.zero_grad()  # 清零梯度

    # 前向传播
    y_pred = model(X_data)

    # 计算损失
    loss = criterion(y_pred, y_true)

    # 反向传播并更新权重
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch + 1}: Loss = {loss.item():.4f}")



