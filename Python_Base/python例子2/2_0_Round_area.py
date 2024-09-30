# -*- coding: UTF-8 -*-
# 2.    计算半径为1~n的圆的面积，仅打印超过 50 的圆面积。

import math

# 打印提示信息，显示程序计算圆的面积
print('This program calculates the area of a circle.')
# 打印提示信息，要求用户输入圆的半径
print('Please enter the radius of the circle')
# 获取用户输入的半径，并将其转换为整数
r = int(input('Enter radius of the largest circle :'))
# 打印提示信息，显示计算圆面积的条件
print('area > 50 : ')
# 循环遍历，当半径大于等于0时执行以下操作
while r >= 0:
    # 计算圆的面积
    area = r * r * math.pi
    # 如果圆的面积小于等于50，则结束循环
    if area <= 50:        
        break
    # 打印圆的面积
    print("%f" % area)      
    # 将半径减1
    r = r - 1 
