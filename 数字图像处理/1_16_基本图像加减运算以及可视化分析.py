# 导入字体管理器中的FontProperties类，用于设置字体属性
from matplotlib.font_manager import FontProperties
# 初始化字体属性，加载指定路径的字体文件，设置字体大小为12
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)

# 导入skimage库中的data模块，用于获取示例图像数据
from skimage import data
# 导入matplotlib库中的pyplot模块，用于绘图
from matplotlib import pyplot as plt

# 加载示例图像数据：月球图像
moon = data.moon()
# 加载示例图像数据：摄影师图像
camera = data.camera()
# 计算月球图像与摄影师图像的差值
image_minus = moon - camera
# 计算月球图像与摄影师图像的和
image_plus = moon + camera

# 设置matplotlib的灰度色彩映射
plt.set_cmap(cmap='gray')

# 开始绘图，设置2x2子图布局
plt.subplot(2, 2, 1)
# 设置子图标题，使用之前定义的字体属性
plt.title('月亮图像', fontproperties=font_set)
# 显示月亮图像
plt.imshow(moon)

plt.subplot(2, 2, 2)
# 设置子图标题，使用之前定义的字体属性
plt.title('摄影师图像', fontproperties=font_set)
# 显示摄影师图像
plt.imshow(camera)

plt.subplot(2, 2, 3)
# 设置子图标题，使用之前定义的字体属性
plt.title('月亮加摄影师图像', fontproperties=font_set)
# 显示月亮图像与摄影师图像的和
plt.imshow(image_plus)

plt.subplot(2, 2, 4)
# 设置子图标题，使用之前定义的字体属性
plt.title('月亮减摄影师图像', fontproperties=font_set)
# 显示月亮图像与摄影师图像的差值
plt.imshow(image_minus)

# 显示所有子图
plt.show()

# 该Python函数实现以下功能：

# 使用matplotlib和skimage库加载并显示示例图像（月球和摄影师图像）。
# 计算并显示这两幅图像的和与差。
# 设置图像标题字体为宋体，字号为12，并通过2x2的子图布局展示原始及处理后的图像。