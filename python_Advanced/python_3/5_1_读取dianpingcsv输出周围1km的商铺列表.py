import csv
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