import csv
fobj = open("C:\VS Code\Python\python实习\python_3\lol.csv","r", encoding="utf-8")
reader = csv. reader(fobj)
name = input("请输入英雄名字:")
print("人物属性如下：")
flag = 1
f = False
for t in reader:
    if flag:
        top = t
        flag = 0
    else:
        if t[10] == name:
            f = True
            for i in range(len(top)):
                print(top[i].lstrip("'"), ":", t[i].lstrip("'"))
            break
if not f:
    print("Not found!")