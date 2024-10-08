import numpy as np
from scipy import signal
from skimage import data
from matplotlib import pyplot as plt
import math

# 定义二维灰度图像的空间滤波函数
# 此函数用于计算图像的二维相关性，常用于图像处理中的滤波操作
# 参数:
#   img: 输入的二维灰度图像数组
#   window: 滤波窗口，即用于卷积的核
# 返回值:
#   经过空间滤波后的图像数组
def correl2d(img, window):
    s = signal.correlate2d(img, window, mode='same', boundary='fill')
    return s.astype(np.uint8)

# 定义二维高斯函数
# 该函数用于计算二维高斯分布的值
# 参数:
#   i, j: 高斯分布中的坐标点
#   sigma: 高斯分布的标准差
# 返回值:
#   计算得到的高斯值
def gauss(i, j, sigma):
    return 1 / (2 * math.pi * sigma ** 2) * math.exp(-(i ** 2 + j ** 2) / (2 * sigma ** 2))

# 定义radius x radius 的高斯平滑模板
# 该函数用于生成一个高斯平滑滤波窗口
# 参数:
#   radius: 模板的半径，决定了模板的大小
#   sigma: 高斯函数的标准差，控制模板的平滑程度
# 返回值:
#   生成的高斯平滑模板窗口
def gauss_window(radius, sigma):
    window = np.zeros((radius * 2 + 1, radius * 2 + 1))
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            window[i + radius][j + radius] = gauss(i, j, sigma)
    return window / np.sum(window)

# img为原始图像
img = data.camera()

# 3x3高斯平滑滤波模板
window1 = gauss_window(3, 1.0)
# 5x5高斯平滑滤波模板
window2 = gauss_window(5, 1.0)
# 9x9高斯平滑滤波模板
window3 = gauss_window(9, 1.0)

# 生成滤波结果
new_img1 = correl2d(img, window1)
new_img2 = correl2d(img, window2)
new_img3 = correl2d(img, window3)

# 显示图像
plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
# 显示原始图像
plt.subplot(2, 2, 2)
plt.imshow(new_img1, cmap='gray')
plt.subplot(2, 2, 3)
plt.imshow(new_img2, cmap='gray')
plt.subplot(2, 2, 4)
plt.imshow(new_img3, cmap='gray')
plt.show()

