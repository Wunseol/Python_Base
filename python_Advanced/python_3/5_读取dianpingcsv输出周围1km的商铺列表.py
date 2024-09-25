import csv
import math

fob_j = open("C:\VS Code\Python\python实习\python_3\dianping.csv","r",encoding="utf-8")
l = 1000
X1=121.651891
Y1=31.260447
reader=csv.reader(fob_j)

for row in reader:
    locate2=[]
    locate1=list[row[13]]
    print(locate1)
    locate2.append(locate1)

print(locate2)

# for i in locate1:
#     print(list[i])
#     # Y2=list[1]
#     d=math.acos[math.cos(Y1)*math.cos(Y2)*math.cos(X1-X2)+math.sin(Y1)*math.sin(Y2)]
fob_j.close()

