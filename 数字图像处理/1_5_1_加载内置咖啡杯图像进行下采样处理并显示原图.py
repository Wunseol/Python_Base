# 导入所需的库
from skimage import data
from matplotlib import pyplot as plt
import numpy as np
import time

# 加载内置的咖啡杯图片数据
image = data.coffee()

# 打印图片的形状，即高度、宽度和通道数
print(image.shape)
# 打印图片数据的类型
print(type(image))

# 定义下采样的比例
ratio = 20

# 初始化一个新的零数组，用于存放下采样后的图片数据
image1 = np.zeros((int(image.shape[0] / ratio),
                  int(image.shape[1] / ratio), image.shape[2]), dtype='int32')

# 显示原始图像
plt.imshow(image)
plt.title("Original Image")
plt.show(block=False)
plt.pause(3)  # 暂停 3 秒

# 遍历下采样后的图片数组，进行下采样处理
for i in range(image1.shape[0]):
    for j in range(image1.shape[1]):
        for k in range(image1.shape[2]):
            # 提取原图中对应的子区域
            delta = image[i * ratio:(i + 1) * ratio, j * ratio: (j + 1) * ratio, k]
            # 计算子区域的平均值，作为下采样图片对应像素的值
            image1[i, j, k] = np.mean(delta)

# 显示下采样后的图片
plt.figure()
plt.imshow(image1)
plt.title("Downsampled Image")
plt.show()


