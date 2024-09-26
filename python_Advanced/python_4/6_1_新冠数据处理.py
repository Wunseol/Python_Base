from audioop import add
import csv
addrSet=set()
fobj=open("C:\VS Code\Python\python_Practice\python_3\covid.csv","r",encoding="utf-8")
reader=csv.reader(fobj)

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
    
print("%d\n"%(len(addrSet)))
print("地址明细为：")
for addr in addrSet:
    print(addr[3:1])
cate_l1=sorted(cate_l1.items(),key=lambda k:k[1])
for i in range(len(cate_l1)-1,-1,-1):
    print(cate_l1[i][0],cate_l1[i][1])
fobj.close()