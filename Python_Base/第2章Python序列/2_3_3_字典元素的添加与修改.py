# 当以指定键为下标为字典赋值时：1）若键存在，则可以修改该键的值；2）若不存在，则表示添加一个键、值对。
aDict={'name':'Dong', 'sex':'male', 'age':37}
aDict['age'] = 38                 #修改元素值
print(aDict)
# {'age': 38, 'name': 'Dong', 'sex': 'male'}
aDict['address'] = 'SDIBT'        #增加新元素
print(aDict)
# {'age': 38, 'address': 'SDIBT', 'name': 'Dong', 'sex': 'male'}

# 使用字典对象的update()方法将另一个字典的键、值对添加到当前字典对象。
print(aDict)
# {'age': 37, 'score': [98, 97], 'name': 'Dong', 'sex': 'male'}
print(aDict.items())
# dict_items([('age', 37), ('score', [98, 97]), ('name', 'Dong'), ('sex', 'male')])
aDict.update({'a':'a','b':'b'})
print(aDict)
# {'a': 'a', 'score': [98, 97], 'name': 'Dong', 'age': 37, 'b': 'b', 'sex': 'male'}

# 使用del删除字典中指定键的元素
# 使用字典对象的clear()方法来删除字典中所有元素
# 使用字典对象的pop()方法删除并返回指定键的元素
# 使用字典对象的popitem()方法删除并返回字典中的一个元素

# 2.3.6  字典推导式
s = {x:x.strip() for x in ('  he  ', 'she    ', '    I')}
print(s)
# {'  he  ': 'he', '    I': 'I', 'she    ': 'she'}
for k, v in s.items():
    print(k, ':', v)
#   he   : he
#     I : I
# she     : she 
print({i:str(i) for i in range(1, 5)})
# {1: '1', 2: '2', 3: '3', 4: '4'}
x = ['A', 'B', 'C', 'D']
y = ['a', 'b', 'b', 'd']
print({i:j for i,j in zip(x,y)})
# {'A': 'a', 'C': 'b', 'B': 'b', 'D': 'd'}
