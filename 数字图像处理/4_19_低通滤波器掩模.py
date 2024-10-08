from skimage import data, color
import numpy as np
import matplotlib.pyplot as plt


def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong']
    mpl.rcParams['axes.unicode_minus'] = False


set_ch()
D = 10
# 读入图像
new_img = data.coffee()
new_img = color.rgb2gray(new_img)
# numpy中的傅里叶变换
fl = np.fft.fft2(new_img)
fl_shift = np.fft.fftshift(fl)
# 使用 np.fft.fftshift()函数实现平移，让直流分量输出图像的重心#实现理想低通滤波器
rows, cols = new_img.shape
crow, ccol = int(rows / 2), int(cols / 2)  # 计算频谱中心
mask = np.zeros((rows, cols), np.uint8)  # 生成 rows 行 cols 列的矩阵，数据格式为uint8
for i in range(rows):
    for j in range(cols):
        if np.sqrt(i * i + j * j) <= D:
            mask[crow - D:crow + D, ccol - D:ccol + D] = 1
fl_shift = fl_shift * mask
f_ishift = np.fft.ifftshift(fl_shift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
img_back = (img_back - np.amin(img_back)) / (np.amax(img_back) - np.amin(img_back))
# plt.figure(figsize=(15,8))
plt.figure()
plt.subplot(121), plt.imshow(new_img, cmap='gray'), plt.title('原始图像')
plt.subplot(122), plt.imshow(img_back, cmap='gray'), plt.title('滤波后的图像')

plt.show()


# 该脚本功能如下：

# 设置Matplotlib字体以正确显示中文和符号。
# 定义变量D用于设定滤波器半径。
# 读取并灰度化一张咖啡图像。
# 对图像执行傅里叶变换，并将频谱中心移到图像中央。
# 创建一个低通滤波器掩模（Mask），允许半径D内的频率通过。
# 应用掩模进行滤波，逆变换后得到处理过的图像。
# 显示原图与滤波后的结果。