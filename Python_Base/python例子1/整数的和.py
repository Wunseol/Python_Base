# -*- coding: UTF-8 -*-

# 函数mysum的功能是计算n个整数中数值在70~80之间（含70和80）的整数的和，程序从键盘输入8个整数，通过调用函数mysum计算这8个整数中数值在70~80之间的整数的和，然后输出。

# x=list(map(int,input('Please enter eight digits:').split( )))
# def mysum(x):
#     sum=0
#     for i in x:
#         if i>=70 and i<=80:
#             sum+=i
#     print("The sum of the numbers is:%d"%sum)
# mysum(x)

x = list(map(int, input('请以空格分隔输入八个数字:').split()))  # 输入八个数字并以列表形式存储
def mysum(x):
    sum = 0  # 初始化变量sum为0
    for i in x:  # 遍历x中的每个元素
        if i >= 70 and i <= 80:  # 判断元素是否在70到80之间
            sum += i  # 如果在，则将元素累加到sum中
    print("这些数值在70~80之间（含70和80）的整数的和为：%d" % sum)  # 输出这些数字的和
mysum(x)  # 调用mysum函数，传入x作为参数

