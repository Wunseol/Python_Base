# 使用“=”将一个元组赋值给变量
a_tuple = ('a', 'b', 'mpilgrim', 'z', 'example')
print(a_tuple)
# ('a', 'b', 'mpilgrim', 'z', 'example')
a = (3)
print(a)
# 3
a = (3,)             #包含一个元素的元组，最后必须多写个逗号
print(a)
# (3,)
a = 3,               #也可以这样创建元组
print(a)
# (3,)
x = ()               #空元组

# 使用tuple函数将其他序列转换为元组
aList=[-1, -4, 6, 7.5, -2.3, 9, -11]
print(tuple('abcdefg'))                    #把字符串转换为元组
# ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(aList)
# [-1, -4, 6, 7.5, -2.3, 9, -11]
print(tuple(aList))                        #把列表转换为元组
# (-1, -4, 6, 7.5, -2.3, 9, -11)
s = tuple()                         #空元组
print(s)
# ()
# 使用del可以删除元组对象，不能删除元组中的元素
