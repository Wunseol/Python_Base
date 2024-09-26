import requests

r =  requests.get("https://voice.baidu.com/newpneumonia/getv2?from=mola-virus&stage=publish&target=trend&isCaseIn=1&area=%E4%B8%8A%E6%B5%B7")

print(r.status_code)
r.encoding = 'utf-8'

print(r.text)

# writer.writerow(["日期","确诊","治愈","死亡","新增确诊","新增本土","新增无症状门"])
# for i in range(90):
#     writer.writerow([data["data"][0]["trend"]["updateDate"][i],
#                      tmpData[0]["data"][i],tmpData[1]["data"][i],
#                      tmpData[2]["data"][i],tmpData[3]["data"][i],
#                      tmpData[4]["data"][i],tmpData[3]["data"][i]])
# fob_j.close()
