from skimage import data, filters
from matplotlib import pyplot as plt

# img 为原始图像
img = data.camera()
# 罗伯特交叉梯度算子
img_robert_pos = filters.roberts_pos_diag(img)
img_robert_neg = filters.roberts_neg_diag(img)
img_robert = filters.roberts(img)
# 显示图像

plt.figure()
plt.subplot(2,2,1)
plt.imshow(img, cmap='gray')
# 显示原始图像
plt.subplot(2,2,2)
plt.imshow(img_robert_pos, cmap='gray')  # 显示罗伯特正对角线边缘图像plt.figure()
plt.subplot(2,2,3)
plt.imshow(img_robert_neg, cmap='gray')  # 显示罗伯特负对角线边缘图像plt.figure()
plt.subplot(2,2,4)
plt.imshow(img_robert, cmap='gray')
# 显示罗伯特梯度图像
plt.show()
