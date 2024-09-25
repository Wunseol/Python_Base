import csv

fob_j = open(r"B:\VS Code\Python\python_Practice\python_3\covid.txt","r",encoding="utf-8")

for t1 in fob_j:
    print(t1.split("，")[1],t1.split("，")[2],t1.split("，")[3].lstrip("居住于"))

fob_j.close()


fob_j2 = open(r"B:\VS Code\Python\python_Practice\python_3\covid.csv","r",encoding="utf-8")

fob_j3 = open(r"B:\VS Code\Python\python_Practice\python_3\testWrite.csv","w",encoding="utf-8")
writer = csv.writer(fob_j3)

# writer.writerow(["hello","你好"])

for t2 in fob_j2:
    
    print(t2.split(",")[1],t2.split(",")[2],t2.split(",")[3].lstrip("居住于"))
    data=t2.split(",")[1],t2.split(",")[2],t2.split(",")[3].lstrip("居住于")
    writer.writerow(data)

    # print(t2.split(",")[1])
    # a=t2.split(",")[1]
    # writer.writerow(a)
    # print(t2.split(",")[2])
    # b=t2.split(",")[2]
    # writer.writerow(b)
    # print(t2.split(",")[3].lstrip("居住于"))
    # c=t2.split(",")[3].lstrip("居住于")
    # writer.writerow(c)
    # print(a,b,c)

fob_j2.close()
fob_j3.close()

