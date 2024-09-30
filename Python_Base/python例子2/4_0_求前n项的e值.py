# -*- coding: UTF-8 -*-
# coding=gbk

# 4.利用公式e = 1 + 1/1! + 1/2! + … + 1/n! + …求前n项的e值。运行结果截屏，并伪代码解释说明（或流程图）。（15分）
# 如输入：4		则输出：2.708333
# 又输入：10		则输出：2.718282

# n = int(input("Enter n:"))        
# t = 1.0
# sum = 1.0                    
# for i in range(1, n+1):         
#         t = t*i
#         sum = sum+1.0/t       

# print(" %f" %sum)     

n = int(input("Enter n:"))  # 输入一个整数n
t = 1.0  # 初始化t为1.0
sum = 1.0  # 初始化sum为1.0
for i in range(1, n+1):  # 循环从1到n+1
    t = t*i  # 计算t乘以i
    sum = sum+1.0/t  # 计算sum加上1除以t

print(" %f" %sum)  # 输出sum的值      
