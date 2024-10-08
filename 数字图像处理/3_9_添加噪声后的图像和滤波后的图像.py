import numpy as np
from scipy import ndimage
from skimage import data, util
from matplotlib import pyplot as plt

# 初始化原始图像
img = data.astronaut()
# 初始化用于存储添加噪声后图像的数组
noise_img = np.zeros(img.shape)
# 初始化用于存储滤波后图像的数组
new_img = np.zeros(img.shape)

# 对图像的每个颜色通道进行处理
for i in range(3):
    # 提取当前颜色通道的灰度图像
    grayimg = data.astronaut()[:, :, i]
    # 对图像添加椒盐噪声
    noise_img[:, :, i] = util.random_noise(grayimg, mode='s&p', rng=None, clip=True)
    # 使用中值滤波进行去噪
    n = 3
    new_img[:, :, i] = ndimage.median_filter(noise_img[:, :, i], (n, n))

# 显示原始图像、添加噪声后的图像和滤波后的图像
plt.figure()
plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title('原始图像')

plt.subplot(1,3,2)
plt.imshow(noise_img, cmap='gray')
plt.title('添加椒盐噪声后的图像')

plt.subplot(1,3,3)
plt.imshow(new_img, cmap='gray')
plt.title('中值滤波后的图像')

plt.show()

