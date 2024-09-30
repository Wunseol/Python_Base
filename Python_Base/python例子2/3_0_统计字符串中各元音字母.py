# -*- coding: UTF-8 -*-
# coding=gbk
# 3.	输入一行字符串，分别统计字符串中各元音字母（AEIOU）的个数（不分大小写）。

# str = list(input("Enter the string :")) 
# a = e = i = o = u = 0        
# for z in str:                         
#     if z == 'a' or i == 'A':       
#         a = a+1                    
#     elif z == 'e' or i == 'E':
#         e = e+1
#     elif z == 'i' or i == 'I':
#         i = i+1
#     elif z == 'o' or i == 'O':
#         o = o+1
#     elif z == 'u' or i == 'U':
#         u = u+1
# print("A:%s \nE:%s \nI:%s \nO:%s \nU:%s\n" % (a, e, i, o, u))


str = list(input("Enter the string :"))  # 获取用户输入的字符串并转换为列表
a = e = i = o = u = 0  # 初始化变量a、e、i、o、u为0
for z in str:  # 遍历字符串中的每个字符
    if z == 'a' or z == 'A':  # 判断字符是否为'a'或'A'
        a = a + 1  # 如果是，则将a加1
    elif z == 'e' or z == 'E':  # 判断字符是否为'e'或'E'
        e = e + 1  # 如果是，则将e加1
    elif z == 'i' or z == 'I':  # 判断字符是否为'i'或'I'
        i = i + 1  # 如果是，则将i加1
    elif z == 'o' or z == 'O':  # 判断字符是否为'o'或'O'
        o = o + 1  # 如果是，则将o加1
    elif z == 'u' or z == 'U':  # 判断字符是否为'u'或'U'
        u = u + 1  # 如果是，则将u加1
print("A:%s \nE:%s \nI:%s \nO:%s \nU:%s\n" % (a, e, i, o, u))  # 打印结果


