# 导入所需的库
from skimage import data
from matplotlib import pyplot as plt
import numpy as np

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

# 创建一个空的图像窗口
fig, ax = plt.subplots()
ax.imshow(image1.astype('uint8'))
plt.title("Downsampled Image")
plt.axis('off')
plt.show(block=False)

# 遍历下采样后的图片数组，进行下采样处理
for i in range(image1.shape[0]):
    for j in range(image1.shape[1]):
        for k in range(image1.shape[2]):
            # 提取原图中对应的子区域
            delta = image[i * ratio:(i + 1) * ratio, j * ratio: (j + 1) * ratio, k]
            # 计算子区域的平均值，作为下采样图片对应像素的值
            image1[i, j, k] = np.mean(delta)
        
        # 更新图像并暂停一小段时间
        if j % 1 == 0:  # 只在特定的列更新图像
            ax.imshow(image1.astype('uint8'))
            plt.pause(0.001)  # 暂停时间

# 显示最终的下采样后的图片
plt.show()



