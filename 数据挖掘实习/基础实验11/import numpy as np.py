import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

stacked_array = np.vstack((array1, array2))  # 或者 np.column_stack((array1, array2))
print(stacked_array)

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

stacked_vector = np.hstack((vector1, vector2))
print(stacked_vector)

import numpy as np

# 原始数组
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# 使用转置操作将行变成列
transposed_array = np.transpose(array)

# 或者使用简写形式 array.T
# transposed_array = array.T

# 输出转置后的数组
print("转置后的数组：")
print(transposed_array)
