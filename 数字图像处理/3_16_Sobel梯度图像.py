# 导入所需的库
from skimage import data, filters
from matplotlib import pyplot as plt

# 加载一张内置的图片数据
img = data.camera()

# 使用Sobel滤镜分别提取水平和竖直方向的边缘
img_sobel_h = filters.sobel_h(img)
img_sobel_v = filters.sobel_v(img)

# 使用Sobel滤镜提取整体边缘
img_sobel = filters.sobel(img)

# 创建一个新的图形以展示结果
plt.figure()

# 显示原始图像
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')

# 显示水平方向的Sobel边缘图像
plt.subplot(2,2,2)
plt.imshow(img_sobel_h, cmap='gray')

# 显示竖直方向的Sobel边缘图像
plt.subplot(2,2,3)
plt.imshow(img_sobel_v, cmap='gray')

# 显示整体Sobel梯度图像
plt.subplot(2,2,4)
plt.imshow(img_sobel, cmap='gray')

# 展示所有子图
plt.show()

