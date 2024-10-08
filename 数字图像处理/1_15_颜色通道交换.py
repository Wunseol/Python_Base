# 导入所需的库
from skimage import data, io
from matplotlib import pyplot as plt

# 加载内置的咖啡杯图片数据
image = data.coffee()

# 分离图片的红色通道
image_r = image[:, :, 0]
# 分离图片的绿色通道
image_g = image[:, :, 1]
# 分离图片的蓝通道
image_b = image[:, :, 2]

# 交换红色通道和蓝通道，进行颜色变换
temp = image_r
image_r = image_b
image_b = temp

# 将变换后的红色通道重新赋值回图片的红色通道
image[:, :, 0] = image_r
# 将变换后的蓝通道重新赋值回图片的蓝通道
image[:, :, 2] = image_b

# 显示经过颜色变换后的图片
plt.imshow(image)
plt.show()


# 该Python函数功能如下：

# 导入所需库：skimage用于图像处理，matplotlib.pyplot用于绘图。
# 加载内置咖啡杯图像数据。
# 分离图像的红（R）、绿（G）、蓝（B）三个颜色通道。
# 交换图像的红色通道与蓝通道，实现颜色变换效果。
# 将变换后的颜色通道重新赋值给图像。
# 使用matplotlib显示变换后的图像。

