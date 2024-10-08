# 导入所需的库
from skimage import data
from matplotlib import pyplot as plt
import numpy as np

# 加载内置的咖啡杯图片数据
image = data.coffee()
plt.show()
# 打印图片的形状，即高度、宽度和通道数
print(image.shape)
# 打印图片数据的类型
print(type(image))

# 定义下采样的比例
ratio = 20

# 初始化一个新的零数组，用于存放下采样后的图片数据
image1 = np.zeros((int(image.shape[0] / ratio),
                  int(image.shape[1] / ratio), image.shape[2]), dtype='int32')

# 遍历下采样后的图片数组，进行下采样处理
for i in range(image1.shape[0]):
    for j in range(image1.shape[1]):
        for k in range(image1.shape[2]):
            # 提取原图中对应的子区域
            delta = image[i * ratio:(i + 1) * ratio, j * ratio: (j + 1) * ratio, k]
            # 计算子区域的平均值，作为下采样图片对应像素的值
            image1[i, j, k] = np.mean(delta)

# 显示下采样后的图片
plt.imshow(image1)
plt.show()


# 该函数执行以下操作：

# 加载内置咖啡杯图像并打印其尺寸和数据类型。
# 设置下采样比例为20。
# 创建一个初始化为零的新数组，用于存放缩小后的图像。
# 使用三重循环遍历新数组的每个像素，并从原始图像中提取对应的子区域。
# 计算每个子区域的平均颜色值，用作下采样图像相应像素的颜色。
# 最后显示下采样后的图像。

