from skimage import data, filters
from matplotlib import pyplot as plt

# img 为原始图像
img = data.camera()

# 应用拉普拉斯滤波器进行边缘检测
img_laplace = filters.laplace(img, ksize = 3, mask = None)

# 原始图像与拉普拉斯图像叠加，实现边缘增强
img_enhance = img + img_laplace

# 显示图像
plt.figure()

# 显示原始图像
plt.subplot(1, 3, 1)
plt.imshow(img, cmap = 'gray')

# 显示拉普拉斯图像
plt.subplot(1, 3, 2)
plt.imshow(img_laplace, cmap = 'gray')

# 显示锐化增强图像
plt.subplot(1, 3, 3)
plt.imshow(img_enhance, cmap ='gray')

plt.show()
