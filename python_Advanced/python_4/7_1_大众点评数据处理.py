import csv
fobj=open("C:\VS Code\Python\python_Practice\python_3\dianping.csv","r", encoding="utf-8")
fobj. readline()
reader=csv. reader(fobj)
n={}

for t in reader:
    m = t[4]
    if m not in n:
        n[m] = 1
    else:
        n[m] += 1
n = sorted(n.items(), key=lambda k: k[1])
for i in range(len(n)-1, -1, -1):
    print(n[i][0],n[i][1])


fobj=open("C:\VS Code\Python\python_Practice\python_3\dianping.csv","r", encoding="utf-8")
fobj. readline()
reader=csv. reader(fobj)
fobj2=open("C:\VS Code\Python\python_Practice\python_3\SSPU1000.csv","w", encoding="utf-8")
writer=csv. writer(fobj2)
for t in reader:
    name, address,cate1,cate2, location= t[1],t[2],t[3],t[4],t[13]
    if t[-2]=="":
        continue
    lal=location. split(",")
    space =((100000*(float(lal[0])-121.651891))**2+(100000*(float(lal[1])-31.260447))**2 )** 0.5
    if space<1000:
        print(name, address,"%d米"%(space))
        writer. writerow([name, address,"%d米"%(space)])
fobj. close()
fobj2. close()


fobj=open("C:\VS Code\Python\python_Practice\python_3\dianping.csv","r", encoding="utf-8")
fobj. readline()
reader = csv. reader(fobj)
n = {}
c = 0
for t in reader:
    if t[-2] == "":
        continue
    lal = t[13].split(",")
    space = ((100000 * (float(lal[0]) - 121.651891)) ** 2 + (100000 * (float(lal[1]) - 31.260447)) ** 2) ** 0.5
    if space < 1000:
        if t[3]=="美食":
            m = t[4]
            if m not in n:
                n[m] = 1
            else:
                n[m] += 1
            c=c+1
n = sorted(n.items(), key=lambda k: k[1])
for i in range(len(n) - 1, -1, -1):
    print("%s %.2f %%" % (n[i][0], n[i][1]/c*100))

