import requests
from bs4 import BeautifulSoup

print('请输入城市名称：')
cityname=input()
host = 'http://api.k780.com:88/?app=weather.future&weaid=%s'%cityname
url = host+'&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=xml'
# 官方网站：http://www.k780.com
# 说明：数据来自国家气象局天气网,每小时更新一次    
# 免费版有每小时点击次数的限制（免费版最多每小时72000次查询）

response = requests.get(url)
content = response.text
soup = BeautifulSoup(content,'lxml')

#日期
day = []
target=soup.find_all('days')
for each in target:
    day.append(each.text)
#星期
week=[]
target=soup.find_all('week')
for each in target:
    week.append(each.text)
#城市
city=[]
target=soup.find_all('citynm')
for each in target:
    city.append(each.text)
#温度
temperature=[]
target=soup.find_all('temperature')
for each in target:
    temperature.append(each.text)
#天气状况
weather=[]
target=soup.find_all('weather')
for each in target:
    weather.append(each.text)
#风向
wind=[]
target=soup.find_all('wind')
for each in target:
    wind.append(each.text)
#风力
winp=[]
target=soup.find_all('winp')
for each in target:
    winp.append(each.text)
length=len(day)
for i in range(length):
    print(day[i],week[i],city[i],temperature[i],weather[i],wind[i],winp[i])

