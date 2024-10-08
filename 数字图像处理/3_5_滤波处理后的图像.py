import numpy as np
from scipy import signal
from skimage import data
from matplotlib import pyplot as plt


# 滤波处理是一种信号处理方法，主要用于从信号中去除不需要的成分，如噪声或某些频率范围内的信号。在图像处理领域，滤波处理通常用来平滑图像、锐化边缘、去除噪声或突出特定特征。

# 在这个Python脚本中，滤波处理通过定义不同大小的盒状滤波器（box filter）来实现。盒状滤波器是一种简单的线性滤波器，它通过对图像中的每个像素及其周围的邻居像素应用一个平均权重来实现平滑效果。具体来说：

# 3x3盒状滤波模板：会对每个像素及其周围8个相邻像素取平均值。
# 5x5盒状滤波模板：会对每个像素及其周围24个相邻像素取平均值。
# 9x9盒状滤波模板：会对每个像素及其周围80个相邻像素取平均值。
# 这些操作有助于减少图像中的高频噪声，使得图像看起来更加平滑。较大的滤波器尺寸会导致更强的平滑效果，但也可能模糊掉一些细节。

# 定义二维灰度图像的空间滤波函数
# 此函数用于计算图像与其滤波窗口之间的二维相关性
# 参数:
#   img: 待处理的灰度图像数组
#   window: 滤波窗口（或称卷积核），用于对图像进行滤波处理
# 返回值:
#   经过滤波处理后的图像数组
def correl2d(img, window):
    s = signal.correlate2d(img, window, mode='same', boundary='fill')
    return s.astype(np.uint8)

# img为原始图像
img = data.camera()
# 3x3盒状滤波模板
window1 = np.ones((3, 3)) / (3 ** 2)
# 5x5 盒状滤波模板
window2 = np.ones((5, 5)) / (5 ** 2)
# 9x9盒状滤波模板
window3 = np.ones((9, 9)) / (9 ** 2)
# 生成滤波结果
new_img1 = correl2d(img, window1)
new_img2 = correl2d(img, window2)
new_img3 = correl2d(img, window3)
# 显示图像
plt.figure()
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
plt.subplot(2,2,2)
plt.imshow(new_img1, cmap='gray')
plt.subplot(2,2,3)
plt.imshow(new_img2, cmap='gray')  # 显示 5x5盒状滤波结果
plt.subplot(2,2,4)
plt.imshow(new_img3, cmap='gray')  # 显示 9x9盒状滤波结果
plt.show()

