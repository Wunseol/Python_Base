import matplotlib.pyplot as plt
import numpy as np
from skimage import data, color

img = data.coffee()
img = color.rgb2gray(img)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
s1 = np.log(np.abs(fshift))


def butterworthPassFilter(image, d, n):
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)

    def make_transform_matrix(d):
        transfor_matrix = np.zeros(image.shape)
        center_point = tuple(map(lambda x: (x - 1) / 2, s1.shape))
        for i in range(transfor_matrix.shape[0]):
            for j in range(transfor_matrix.shape[1]):
                def cal_distance(pa, pb):
                    from math import sqrt
                    dis = sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)
                    return dis

                dis = cal_distance(center_point, (i, j))
                transfor_matrix[i, j] = 1 / (1 + (dis / d) ** (2 * n))
        return transfor_matrix

    d_matrix = make_transform_matrix(d)
    d_matrix = 1 - d_matrix
    new_img = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift * d_matrix)))
    return new_img


plt.subplot(221)
plt.axis('off')
plt.title('Original')
plt.imshow(img, cmap='gray')
plt.subplot(222)
plt.axis('off')
plt.title('Butter 100 1')
butter_100_1 = butterworthPassFilter(img, 100, 1)
plt.imshow(butter_100_1, cmap='gray')
plt.subplot(223)
plt.axis('off')
plt.title('Butter 30 1')
butter_30_1 = butterworthPassFilter(img, 30, 1)
plt.imshow(butter_30_1, cmap='gray')
plt.subplot(224)
plt.axis('off')
plt.title('Butter 30 5')
butter_30_5 = butterworthPassFilter(img, 30, 5)
plt.imshow(butter_30_5, cmap='gray')

plt.show()

