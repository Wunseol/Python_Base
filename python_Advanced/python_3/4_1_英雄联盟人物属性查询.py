import csv

fob_j = open("C:\VS Code\Python\python实习\python_3\lol.csv","r", encoding="utf-8")
reader = csv. reader(fob_j)
name = input("请输入英雄名字:")

print("人物属性如下：")

a = 1
for t1 in reader:
    if t1[10] == name:
        a = 0
        for i in range(len(t1)):
            print(t1[i])
        break
if a:
    print("error!")