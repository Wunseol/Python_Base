fob_j = open("C:\VS Code\Python\python_Practice\python_3\covid.txt", "r", encoding="utf-8")
addrSet=set()
a=[]

for t1 in fob_j:
    a.append(t1.split("，")[3].lstrip("居住于"))

for i in a:
    for x in a:
        if i==x:
            a.remove(i)
            
print("地址数%d"%len(a))
print("地址明细为：")
for j in a:
    print(j)

fob_j.close()

import csv
addrSet=set()
fob_j=open("C:\VS Code\Python\python_Practice\python_3\covid.csv","r",encoding="utf-8")
reader=csv.reader(fob_j)

cate_l1={}
for t in reader:
    m=t[3]
    if(m[3:7]=='浦东新区'):
        s='浦东新区'
    else:
        s=m[3:6]
    if s not in cate_l1:
        cate_l1[s]=1
    else:
        cate_l1[s]+=1
    addrSet.add(t[3])
print("每个区的感染人数排序：")
cate_l1=sorted(cate_l1.items(),key=lambda k:k[1])
for i in range(len(cate_l1)-1,-1,-1):
    print(cate_l1[i][0],cate_l1[i][1])

fob_j.close()