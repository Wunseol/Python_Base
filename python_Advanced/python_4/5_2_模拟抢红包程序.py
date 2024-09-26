import csv
import random
from unicodedata import name

fp = open("C:\VS Code\Python\python_Practice\python_4\student.csv",'r',encoding='utf-8')
reader=csv.reader(fp)

a=[]
for x in reader:
    a.append(x[3])

s_name=random.sample(a,5)

money = float(input("请输入金额："))
num = int(input("请输入人数："))

if(num<money):
    money_list = []
    red_packet = 0
    for i in range(1, num): # 分配
        red_packet = random.uniform( 0 , money)  # 随机取一个数
        money = money - red_packet # 剩下的金额
        money_list.append(red_packet) # 装入列表
    money_list.append(red_packet) # 最后循环剩下的金额
random.shuffle(money_list) # 打乱列表

for x in range(len(money_list)):   # 输出结果
    if(money_list[x]==max(money_list)):
        top=x
    
    print("第"+str(x + 1)+"个红包 "+s_name[x]+':%0.01f'%(money_list[x]) + '元')
print("运气王是："'第' + str(top + 1) + '个红包 ：'+s_name[top])