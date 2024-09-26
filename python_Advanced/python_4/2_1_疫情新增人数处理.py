import requests
import csv
url="https://voice.baidu.com/newpneumonia/getv2?from=mola-virus&stage=publish&target=trend&isCaseIn=1&area=%E4%B8%8A%E6%B5%B7"
response = requests.get(url,data='data')
data = response.json()
tmpData = data["data"][0]["trend"]["list"]

fob_j = open("C:\VS Code\Python\python_Practice\python_4\covid2.csv","w",newline='')
writer = csv.writer(fob_j)
writer.writerow(["日期","确诊","治愈","死亡","新增确诊","新增本土","新增无症状门"])
for i in range(90):
    writer.writerow([data["data"][0]["trend"]["updateDate"][i],
                     tmpData[0]["data"][i],tmpData[1]["data"][i],
                     tmpData[2]["data"][i],tmpData[3]["data"][i],
                     tmpData[4]["data"][i],tmpData[3]["data"][i]])
fob_j.close()

f=open("C:\VS Code\Python\python_Practice\python_4\covid2.csv","r",newline='')
reader = csv.reader(f)
for row in reader:
    print(row)


# fob_j1 = open("C:\VS Code\Python\python_Practice\python_4\covid2.csv","r")
# reader=csv.reader(fob_j1)

# print(reader)
# fob_j1.close()