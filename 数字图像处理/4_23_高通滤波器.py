from skimage import data, color
import numpy as np
import matplotlib.pyplot as plt


D = 10
img = data.coffee()
img = color.rgb2gray(img)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)


# 实现理想高通滤波器
rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)   # 计算频谱中心
mask = np.zeros((rows, cols), np.uint8)   # 生成rows行cols列的矩阵，数据格式为uint8
for i in range(rows):
    for j in range(cols):
        if np.sqrt(i*i+j*j) <= D:
            # 将距离频谱中心小于D的部分低通信息设置为1，属于低通滤波
            mask[crow-D:crow+D, ccol-D:ccol+D] = 1
mask = 1-mask
fshift = fshift*mask


# 傅里叶逆变换
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
img_back = (img_back-np.amin(img_back))/(np.amax(img_back)-np.amin(img_back))

plt.figure()
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.subplot(122), plt.imshow(img_back, cmap='gray')

plt.show()
