# 使用=将一个字典赋值给一个变量
a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
print(a_dict)
# {'database': 'mysql', 'server': 'db.diveintopython3.org'}
x = {}                     #空字典
print(x)
# {}


# 使用dict利用已有数据创建字典：
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
dictionary = dict(zip(keys, values))
print(dictionary)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
x = dict() #空字典
print(x)
# {}

# 使用dict根据给定的键、值创建字典
d = dict(name='Dong', age=37)
print(d)
# {'name': 'Dong', 'age': 37}

# 以给定内容为键，创建值为空的字典
adict = dict.fromkeys(['name', 'age', 'sex'])
print(adict)
# {'name': None, 'age': None, 'sex': None}
# 可以使用del删除整个字典

