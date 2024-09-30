# -*- coding: UTF-8 -*-
# coding=gbk

# 6.编写程序，实现以下成绩处理功能（输出格式参见示例）。
# （1）输入n和n个成绩（成绩为浮点数类型，假设1≤n≤50）；
# （2）计算并输出成绩的累加和（记为sum）与平均成绩（记为ave），将≥ave的成绩归为A档，将＜ave的成绩归为B档；
# （3）分别统计A、B两档的人数，计算在总人数中的比率；
# （4）求出A档学生的最低分和B档学生的最高分，它们与平均成绩的差值；
# 运行示例：
# 输入：9  55.5  99.5  50.0  90.0  88  59.5  48  60  78.0
# 输出：
# Sum=628.5, Ave=69.8
# A: 4,44.4%  B: 5,55.6%
# MinA: 78.0,+8.2  MaxB: 60.0,-9.8

# n = int(input("Enter n : "))          
# s = list(map(float, input("enter %d  scores :" % n).split(" ")))  
# if 1 <=n<= 50:                  
#     sum = 0                           
#     for i in s:
#         sum = sum + i
#     ave = sum / n                  
#     print('Sum=%.1f, Ave=%.1f' % (sum, ave))  
#     A = B = 0                           
#     a = []                         
#     b = []
#     for i in s:                       
#         if i >= ave:
#             A = A+1
#             a = a+[i]
#         else:
#             B = B + 1
#             b = b+[i]
#     print('A: %d,%.1f%%  B: %d,%.1f%%' % (A, A/n*100, B, B/n*100))  
#     Min = min(a)                    
#     Max = max(b)
#     print('MinA: %.1f,+%.1f  MaxB: %.1f,-%.1f' % (Min, Min-ave, Max, ave-Max)) 
# else:
#     print('error!\n')      


n = int(input("Enter n : "))  # 输入n的值
s = list(map(float, input("enter %d  scores :" % n).split(" ")))  # 输入n个分数，并转换为浮点数列表
if 1 <=n<= 50:  # 判断n是否在范围内
    sum = 0  # 初始化总和为0
    for i in s:  # 遍历分数列表
        sum = sum + i  # 计算总和
    ave = sum / n  # 计算平均分
    print('Sum=%.1f, Ave=%.1f' % (sum, ave))  # 输出总和和平均分
    A = B = 0  # 初始化通过和不通过的个数为0
    a = []  # 初始化通过分数列表
    b = []  # 初始化不通过分数列表
    for i in s:  # 遍历分数列表
        if i >= ave:  # 判断是否大于等于平均分
            A = A+1  # 通过个数加1
            a = a+[i]  # 将分数添加到通过分数列表中
        else:
            B = B + 1  # 不通过个数加1
            b = b+[i]  # 将分数添加到不通过分数列表中
    print('A: %d,%.1f%%  B: %d,%.1f%%' % (A, A/n*100, B, B/n*100))  # 输出通过和不通过的人数及占比
    Min = min(a)  # 计算通过分数列表的最小值
    Max = max(b)  # 计算不通过分数列表的最大值
    print('MinA: %.1f,+%.1f  MaxB: %.1f,-%.1f' % (Min, Min-ave, Max, ave-Max))  # 输出通过分数最小值和不通过分数最大值与平均分的差值
else:
    print('error!\n')  # 输出错误信息




