import csv

fob_j = open("C:\VS Code\Python\python实习\python_3\lol.csv","r",encoding="utf-8")


reader=csv.reader(fob_j)
column= [row[1] for row in reader]
print(column)

fob_j.close()

