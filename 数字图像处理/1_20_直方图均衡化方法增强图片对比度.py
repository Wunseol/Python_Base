# 导入所需的库
from skimage import data, exposure
import matplotlib.pyplot as plt

# 加载内置的月亮图片数据
img = data.moon()

# 创建一个名为"hist"的图形窗口，设置窗口大小为8x8英寸
plt.figure("hist", figsize=(8, 8))

# 将图片转换为一维数组，以便进行直方图计算
arr = img.flatten()

# 子图1: 显示原始图片
plt.subplot(221)
plt.imshow(img, plt.cm.gray)

# 子图2: 显示原始图片的直方图
plt.subplot(222)
plt.hist(arr, bins=256, density=1, edgecolor='None', facecolor='red')

# 使用直方图均衡化方法增强图片对比度
img1 = exposure.equalize_hist(img)
# 将处理后的图片转换为一维数组
arr1 = img1.flatten()

# 子图3: 显示经过直方图均衡化处理后的图片
plt.subplot(223)
plt.imshow(img1, plt.cm.gray)

# 子图4: 显示经过直方图均衡化处理后的图片的直方图
plt.subplot(224)
plt.hist(arr1, bins=256, density=1, edgecolor='None', facecolor='red')

# 显示所有子图
plt.show()


