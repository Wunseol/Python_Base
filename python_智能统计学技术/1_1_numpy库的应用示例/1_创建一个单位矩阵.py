# 导入numpy库，用于进行科学计算
import numpy as np

# 创建一个3x3的单位矩阵，单位矩阵的主对角线上的元素为1，其他位置上的元素为0
n = np.eye(3)

# 打印矩阵n，展示其结构
print(n)

# 打印矩阵n的数据类型，了解矩阵元素的存储方式
print(n.dtype)

# 打印矩阵n的特定元素，此处打印的是第二行第二列的元素，索引从0开始
print(n[1][1])

# 打印二维列表n的第二个元素的第一个元素，即n[0][1]
print(n[0][1])


