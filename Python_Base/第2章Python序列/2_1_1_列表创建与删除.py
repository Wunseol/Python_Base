
# 使用“=”直接将一个列表赋值给变量即可创建列表对象

a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
a_list = []                            #创建空列表

# 也可以使用list()函数将元组、range对象、字符串或其他类型的可迭代对象类型的数据转换为列表。
a_list = list((3,5,7,9,11))
print(a_list)
# [3, 5, 7, 9, 11]
print(list(range(1,10,2)))
# [1, 3, 5, 7, 9]
print(list('hello world'))
# ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
x = list()                            #创建空列表

# 当不再使用时，使用del命令删除整个列表。
del a_list
print(a_list)
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     a_list
# NameError: name 'a_list' is not defined

