# 例3-1  面试资格确认。
age = 24
subject = "计算机"
college = "非重点"
if (age > 25 and subject=="电子信息工程") or \
   (college=="重点" and subject=="电子信息工程") or\
   (age<=28 and subject=="计算机"):
    print("恭喜，你已获得我公司的面试机会!")
else:
    print("抱歉，你未达到面试要求")

# 例3-2  用户输入若干个分数，求所有分数的平均分。每输入一个分数后询问是否继续输入下一个分数，回答“yes”就继续输入下一个分数，回答“no”就停止输入分数。
numbers = []                              #使用列表存放临时数据
while True:
    x = input('请输入一个成绩：')
    try:                                  #异常处理结构
        numbers.append(float(x))
    except:
        print('不是合法成绩')
    while True:
        flag = input('继续输入吗？（yes/no）').lower()
        if flag not in ('yes', 'no'):     #限定用户输入内容必须为yes或no
            print('只能输入yes或no')
        else:
            break
    if flag=='no':
        break

print(sum(numbers)/len(numbers))


# 例3-3  编写程序，判断今天是今年的第几天。

import time

date = time.localtime()                         #获取当前日期时间
year, month, day = date[:3]
day_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if year%400==0 or (year%4==0 and year%100!=0):  #判断是否为闰年
    day_month[1] = 29

if month==1:
    print(day)
else:
    print(sum(day_month[:month-1])+day)

# 其中闰年判断可以直接使用calendar模块的方法。

import calendar
print(calendar.isleap(2016))
# True
print(calendar.isleap(2015))
# False

# 或者使用下面的方法直接计算今天是今年的第几天
import datetime
print(datetime.date.today().timetuple().tm_yday)
# 309
print(datetime.date(2019,11,5).timetuple().tm_yday)
# 309




