# -*- coding: UTF-8 -*-
# coding=gbk

# 5.	从键盘输入三角形的3条边长x, y, z（整型数），判断此3边能否构成三角形。
# 若能，则判定构成的三角形是等边三角形或是等腰三角形还是任意三角形，并求出所构成三角形的面积。

# import math                     
# x, y, z=map(int,input('Enter the size length of triangle :').split(' '))  
# flag = 1                            
# if x+y > z and y+z > x and x+z > y:      
#     if x == y == z:                      
#         print('this is equilateral triangle \n')
#     elif (x == y and x != z) or (x == z and x != y) or (y == z and y != x): 
#         print('this is isosceles triangle \n')
#     else:
#         print('this is the other triangle \n')
# else:
#     print('it can not construct a triangle \n')
#     flag = 0
# if flag == 1:               
#     p = (x+y+z)/2
#     area = math.sqrt(p*(p-x)*(p-y)*(p-z))  
#     print("the area of this triangle:%0.2f\n" % area)   
# print("finish\n") 

import math

# 获取用户输入的三角形的边长
x, y, z = map(int, input('请输入三角形的边长（以空格分隔）：').split(' '))

# 校验是否能构成三角形
flag = 1
if x + y > z and y + z > x and x + z > y:
    if x == y == z:
        print('这是一个等边三角形 \n')
    elif (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
        print('这是一个等腰三角形 \n')
    else:
        print('这是一个其他类型的三角形 \n')
else:
    print('无法构成三角形 \n')
    flag = 0

# 如果能构成三角形，则计算三角形的面积
if flag == 1:
    p = (x + y + z) / 2
    area = math.sqrt(p * (p - x) * (p - y) * (p - z))
    print("这个三角形的面积为：%.2f\n" % area)

print("结束\n")

