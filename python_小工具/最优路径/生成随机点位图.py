import numpy as np
import matplotlib.pyplot as plt

# 设定随机种子以确保结果可复现
np.random.seed(1)

# 随机生成10个点的坐标
num_points = 100
# 通过np.random.rand函数随机生成一个形状为(num_points, 2)的数组points，其中num_points为点的数量，每个点的坐标为一个长度为2的数组
points = np.random.rand(num_points, 2)

# 绘制随机生成的点
plt.figure(figsize=(8, 6))
plt.scatter(points[:, 0], points[:, 1], color='red')
for i, point in enumerate(points):
    plt.text(point[0], point[1], f'P{i}', fontsize=12, ha='center', va='bottom')
plt.title('Randomly Generated Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()



