# 几乎所有的Python合法表达式都可以作为条件表达式.
# 算术运算符：+、-、*、/、//、%、**
# 关系运算符：>、<、==、<=、>=、!=，可以连续使用，如
print(1<2<3)
# True
print(1<2>3)
# False
print(1<3>2)
# True
# 测试运算符：in、not in、is、is not
# 逻辑运算符：and、or、not，注意短路求值
# 位运算符：~、&、|、 ^、 <<、>>

# 在选择和循环结构中，条件表达式的值只要不是False、0（或0.0、0j等）、空值None、空列表、空元组、空集合、空字典、空字符串、空range对象或其他空迭代对象，Python解释器均认为与True等价。

if 3:              #使用整数作为条件表达式
    print(5)
# 5
a = [1, 2, 3]
if a:              #使用列表作为条件表达式
	print(a)
# [1, 2, 3]

a = []
if a:
	print(a)
else:
    print('empty')
# empty

i = s = 0
while i <= 10:              #使用关系表达式作为条件表达式
    s += i
    i += 1
print(s)
# 55

i = s = 0
while True:                 #使用常量True作为条件表达式
    s += i
    i += 1
    if i > 10:
        break   
print(s)
# 55

s = 0
for i in range(0, 11, 1):   #遍历迭代对象中的所有元素
    s += i
print(s)
# 55

# 逻辑运算符and和or以及关系运算符具有惰性求值特点，只计算必须计算的表达式。
# 以“and”为例，对于表达式“表达式1 and 表达式2”而言，如果“表达式1”的值为“False”或其他等价值时，不论“表达式2”的值是什么，整个表达式的值都是“False”，此时“表达式2”的值无论是什么都不影响整个表达式的值，因此将不会被计算，从而减少不必要的计算和判断。
# 在设计条件表达式时，如果能够大概预测不同条件失败的概率，并将多个条件根据“and”和“or”运算的短路求值特性来组织先后顺序，可以大幅度提高程序运行效率。
# 在Python中，条件表达式中不允许使用赋值运算符“=”。
# if a=3:
# SyntaxError: invalid syntax
# if (a=3) and (b=4):	
# SyntaxError: invalid syntax


