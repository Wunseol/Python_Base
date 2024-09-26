import random
import csv

fob_j = open("C:\VS Code\Python\python_Practice\python_4\student1.csv","r")#用原来的student.csv

count=0

money = float(input("请输入金额："))
num = int(input("请输入红包数："))

if(num<money):
    money_list = []
    red_packet = 0
    for i in range(1, num): # 分配
        red_packet = random.uniform( 0 , money)  # 随机取一个数
        money = money - red_packet # 剩下的金额
        money_list.append(red_packet) # 装入列表
    money_list.append(red_packet) # 最后循环剩下的金额

    # round(money_list,2)
    a = [float("{:.2f}".format(i)) for i in money_list]
    for k in range(len(a)):
        if(a[k]==0):
            a[k]+=0.1
            count+=1
    count=count*0.1

    random.shuffle(a) # 打乱列表

    for x in range(len(a)):
        for t1 in fob_j:
            print(t1.split(",")[0])
            print(t1.split(",")[1],t1.split(",")[2],t1.split(",")[3])
            break
        if(a[x]==max(a)):
            a[x]=a[x]-count
            top=x
            # print(top)
        print('第' + str(x + 1) + '个红包：' + str(a[x]) + '元')
    print("\n")
    print("第%d个红包"%(top+1))
    print("是  高级特效\!/“运气王”\!/高级特效 ")
    print("\n")

else:
    print("分配的红包过多！！！")

fob_j.close()