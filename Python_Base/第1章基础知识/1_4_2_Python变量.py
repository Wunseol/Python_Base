# Python属于强类型编程语言，Python解释器会根据赋值或运算来自动推断变量类型。Python还是一种动态类型语言，变量的类型也是可以随时变化的。
x = 3 # 创建整型变量
print(type(x)) # type(x)查看变量类型
# <class 'int'>
x = 'hello world'
print(type(x))
# <class 'str'>
x = [1,2,3]
print(type(x))
# <class 'list'>

# 如果变量出现在赋值运算符或复合赋值运算符（例如+=、*=等等）的左边则表示创建变量或修改变量的值，否则表示引用该变量的值。
x = 3
print(x**2)
# 9
x += 6 # 修改变量值
print(x) # 读取变量值并输出显示
# 9
x = [1,2,3] #创建列表对象
x[1] = 5    #修改列表元素值
print(x)    #输出显示整个列表
# [1, 5, 3]
print(x[2]) #输出显示列表指定元素
# 3

# 字符串和元组属于不可变序列，不能通过下标的方式来修改其中的元素值，试图修改元组中元素的值时会抛出异常。
x = (1,2,3)
print(x)
# (1, 2, 3)
# x[1] = 5 # 修改元组中元素值会报错
# TypeError: 'tuple' object does not support item assignment
# 字符串和元组属于不可变序列，不能通过下标的方式来修改其中的元素值，试图修改元组中元素的值时会抛出异常。

# 在Python中，允许多个变量指向同一个值，例如：
x = 3
print(id(x))
# 2116017520944
y = x
print(id(y))
# 2116017520944
y = x
print(id(y))
# 2116017520944
x += 6
print(id(x))
# 2116017521136
print(y)
# 3
print(id(y))
# 2116017520944

x = -6
y = -6
print(id(x)==id(y))
# False

# x = -5
# y = -5
# id(x) == id(y)
# # True

# x = 255
# y = 255
# id(x) == id(y)
# # True

# x = 256
# y = 256
# id(x) == id(y)
# # True

# x = 257
# y = 257
# id(x) == id(y)
# # False

# x = 3.0
# y = 3.0
# id(x) == id(y)
# # False

# x, y = 300000, 300000
# id(x) == id(y)
# # True

# x = [666666, 666666]
# y = (666666, 666666)
# id(x[0]) == id(x[1])
# # True

# id(y[0]) == id(y[1])
# # True

# id(x[0]) == id(y[0])
# # False
