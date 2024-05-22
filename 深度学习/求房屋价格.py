# import torch
# from torch.utils.data import TensorDataset, DataLoader

# # 假设你已经有了训练数据（面积）和对应的房价（目标值）
# # 并且已经将它们转换为PyTorch张量格式
# # area_features是形状为(N, 1)的二维张量，其中N是样本数量，1是特征维度
# area_features = torch.tensor([[area1], [area2], ..., [areaN]])
# prices = torch.tensor([price1, price2, ..., priceN])

# # 将数据集封装为TensorDataset
# dataset = TensorDataset(area_features, prices)

# # 创建DataLoader以方便批量处理
# dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# # 定义模型，由于只有一个特征，我们只需要一个权重和一个偏置项
# class LinearRegressionModel(torch.nn.Module):
#     def __init__(self):
#         super(LinearRegressionModel, self).__init__()
#         self.linear = torch.nn.Linear(1, 1)  # 输入维度为1，输出维度也为1

#     def forward(self, x):
#         return self.linear(x)

# model = LinearRegressionModel()

# # 定义损失函数和优化器
# criterion = torch.nn.MSELoss()  # 均方误差作为损失函数
# optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # 使用随机梯度下降优化器

# # 训练模型
# num_epochs = 100
# for epoch in range(num_epochs):
#     for inputs, targets in dataloader:
#         # 前向传播计算预测值
#         outputs = model(inputs)

#         # 计算损失
#         loss = criterion(outputs, targets)

#         # 反向传播并更新参数
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

# # 在训练结束后，可以对新样本进行预测
# new_area = torch.tensor([[new_area_value]])  # 新房屋的面积
# predicted_price = model(new_area).item()  # 预测房价，注意.item()用于获取标量结果

# print("预测的房价是：", predicted_price)