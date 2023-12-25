# 以键作为下标可以读取字典元素，若键不存在则抛出异常
aDict = {'name':'Dong', 'sex':'male', 'age':37}
print(aDict['name'])
# 'Dong'

# aDict['tel']                     #键不存在，抛出异常
# Traceback (most recent call last):
#   File "<pyshell#53>", line 1, in <module>
#     aDict['tel']
# KeyError: 'tel'


# 使用字典对象的get()方法获取指定键对应的值，并且可以在键不存在的时候返回指定值。
print(aDict.get('address'))
# None
print(aDict.get('address', 'SDIBT'))
# SDIBT

# 使用字典对象的items()方法可以返回字典的元素。
# 使用字典对象的keys()方法可以返回字典的“键”。
# 使用字典对象的values()方法可以返回字典的“值”。

aDict={'name':'Dong', 'sex':'male', 'age':37}
for item in aDict.items():     #输出字典中所有元素
    print(item)
# ('age', 37)
# ('name', 'Dong')
# ('sex', 'male')
for key in aDict:              #不加特殊说明，默认输出“键”
    print(key)
# age
# name
# sex

for key, value in aDict.items():       #序列解包用法
    print(key, value)
# age 37
# name Dong
# sex male
print(aDict.keys())                           #返回所有“键”
# dict_keys(['name', 'sex', 'age'])
print(aDict.values())                         #返回所有“值”
# dict_values(['Dong', 'male', 37])


