# -*- coding: UTF-8 -*-
# 程序从键盘输入8个学生计算机二级考试的成绩（成绩可能有小数），统计并输出成绩合格的学生的人数。程序对有小数的成绩应也能够正确处理。
# (提交清单：python程序代码；运行结果截屏；伪代码解释说明（流程图）；两分钟以内的视频：详细解释代码实现思路）

# x = list(map(float,input('Please enter the grades of 8 classmates:').split( )))
x = list(map(float, input('请输入8位同学的成绩：').split()))  # 将输入的字符串按空格分割为列表，并将每个字符串转为浮点数类型，最后转为列表
sum=0
for i in x:
    if i>=60:
        sum+=1
print("The number of pass is:%d" %sum)
