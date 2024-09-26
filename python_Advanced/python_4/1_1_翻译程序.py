import requests
import time
import hashlib
q=input("请输入您要查询的单词")
m =hashlib.md5()
appid = "20220915001343823"
key = "fEyA00dPeyqN3bzBjqL7"
salt = int(time. time())
signText = "%s%s%s%s"%(appid,q,salt, key)
m.update(signText.encode("utf-8"))
sign = m.hexdigest()
url = "https://dict.youdao.com/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q=python"

response = requests. get(url)
data = response.json()
print(data)
