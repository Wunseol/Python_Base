# -*- coding: UTF-8 -*-

# 电力公司根据如下费率表进行收费：第一个300度（0到300度）以每度0.6元计，下一个 300度（301到600度）以每度0.5元计，再下一个 400度（601到1000度）以每度0.4元计，超过1000度的电量以每度0.3元计。
# （1）设计计费函数float fee(int x); 函数根据客户用电量（x）计算电费并返回；
# （2）从键盘上输入3个客户的用电量，通过调用fee函数分别计算出相应电费，并按示例格式输出（电费保留一位小数）。
# 运行示例：
# 输入：
# 123 2011 985
# 输出：
# fee(123)=73.8
# fee(2011)=793.3
# fee(985)=484.0

# x=list(map(int,input('Please enter three power consumption:').split( )))

# def fee(x):

#     for i in x:
#         if i<=300:
#             sum=i*0.6
#         elif i<=600:
#             sum=0.6*300+(i-300)*0.5
#         elif i<=1000:
#             sum=(0.6+0.5)*300+(i-600)*0.4
#         else:
#             sum=(0.6+0.5)*300+0.4*400+(i-1000)*0.3
#         print("fee(%d)=%.1f"%(i,sum))
# fee(x)


x=list(map(int,input('Please enter three power consumption:').split( )))
# 输入三个功率消耗并转换为整数列表

def fee(x):
    # 定义函数fee，参数为x（功率消耗列表）
    for i in x:
        # 遍历x中的每个元素
        if i<=300:
            # 如果功率消耗小于等于300
            sum=i*0.6
            # 计算并赋值sum为功率消耗乘以0.6
        elif i<=600:
            # 如果功率消耗小于等于600
            sum=0.6*300+(i-300)*0.5
            # 计算并赋值sum为300乘以0.6加上(功率消耗减去300)乘以0.5
        elif i<=1000:
            # 如果功率消耗小于等于1000
            sum=(0.6+0.5)*300+(i-600)*0.4
            # 计算并赋值sum为(0.6加0.5)乘以300加上(功率消耗减去600)乘以0.4
        else:
            # 否则
            sum=(0.6+0.5)*300+0.4*400+(i-1000)*0.3
            # 计算并赋值sum为(0.6加0.5)乘以300加上400乘以0.4加上(功率消耗减去1000)乘以0.3
        print("fee(%d)=%.1f"%(i,sum))
        # 打印输出格式化的字符串，包括功率消耗和计算结果
fee(x)
# 调用函数fee并传入x作为参数

