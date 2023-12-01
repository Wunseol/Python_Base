# +运算符除了用于算术加法以外，还可以用于列表、元组、字符串的连接，但不支持不同类型的对象之间相加或连接。
print([1, 2, 3] + [4, 5, 6])         #连接两个列表
# [1, 2, 3, 4, 5, 6]
print((1, 2, 3) + (4,))               #连接两个元组
# (1, 2, 3, 4)
print('abcd' + '1234')               #连接两个字符串
# 'abcd1234'
# print('A' + 1)                           #不支持字符与数字相加，抛出异常
# TypeError: Can't convert 'int' object to str implicitly
print(True + 3)                        #Python内部把True当作1处理
# 4
print(False + 3)                      #把False当作0处理
# 3


# *运算符不仅可以用于数值乘法，还可以用于列表、字符串、元组等类型，当列表、字符串或元组等类型变量与整数进行“*”运算时，表示对内容进行重复并返回重复后的新对象。
print(2.0 * 3)                     #浮点数与整数相乘
# 6.0
print((3+4j) * 2)                  #复数与整数相乘
# (6+8j)
print((3+4j) * (3-4j))             #复数与复数相乘
# (25+0j)
print("a" * 10)                    #字符串重复
# 'aaaaaaaaaa'
print([1,2,3] * 3)                 #列表重复
# [1, 2, 3, 1, 2, 3, 1, 2, 3]
print((1,2,3) * 3)                 #元组重复
# (1, 2, 3, 1, 2, 3, 1, 2, 3)


# Python中的除法有两种，“/”和“//”分别表示除法和整除运算。
print(3 / 5)
# 0.6
print(3 // 5)
# 0
print(3.0 / 5)
# 0.6
print(3.0 // 5)
# 0.0
print(13 // 10)
# 1s
print(-13 // 10)
# -2


# %运算符除去可以用于字符串格式化之外，还可以对整数和浮点数计算余数。但是由于浮点数的精确度影响，计算结果可能略有误差。
print(3.1 % 2)
# 1.1
print(6.3 % 2.1)
# 2.0999999999999996
print(6 % 2)
# 0
print(-17 % 4)                  #余数与%右侧的运算数符号一致，(-17-(3))能被4整除
# 3
print(17 % -4)                  #(17-(-3))能被(-4)整除
# -3
print(5.7 % 4.8)
# 0.9000000000000004


# 关系运算符可以连用，一般用于同类型对象之间值的大小比较，或者测试集合之间的包含关系。
print(1 < 3 < 5)                       #等价于1 < 3 and 3 < 5
# True
print('Hello' > 'world')               
#比较字符串中字符大小，比较它们的Unicode值，Unicode值较低的字符被认为较小。
# False
print([1, 2, 3] < [1, 2, 4])           #比较列表大小
# True
# print('Hello' > 3)                     #字符串和数字不能比较
# TypeError: unorderable types: str() > int()
print({1, 2, 3} < {1, 2, 3, 4})        #测试是否子集
# True


# 成员测试运算符in用于成员测试，即测试一个对象是否为另一个对象的元素。
print(3 in [1, 2, 3])       #测试3是否存在于列表[1, 2, 3]中
# True
print(5 in range(1, 10, 1)) #range()是用来生成指定范围数字的内置函数
# True
print('abc' in 'abcdefg')   #子字符串测试
# True
for i in (3, 5, 7):  #循环，成员遍历
    print(i, end='\t')   #注意，这里打两个回车才会执行
# 3	 5	7	
print()


# 同一性测试运算符（identity comparison）is用来测试两个对象是否是同一个，如果是则返回True，否则返回False。如果两个对象是同一个，二者具有相同的内存地址。
print(3 is 3)
# True
x = [300, 300, 300]
print(x[0] is x[1])        #基于值的内存管理，同一个值在内存中只有一份
# True
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)              #上面形式创建的x和y不是同一个列表对象
# False


# 位运算符只能用于整数，其内部执行过程为：首先将整数转换为二进制数，然后右对齐，必要的时候左侧补0，按位进行运算，最后再把计算结果转换为十进制数字返回。
print(3 << 2)    #把3左移2位
# 12
print(3 & 7)     #位与运算
# 3
print(3 | 8)     #位或运算
# 11
print(3 ^ 5)     #位异或运算
# 6


# 集合的交集、并集、对称差集等运算借助于位运算符来实现，而差集则使用减号运算符实现（注意，并集运算符不是加号）。
print({1, 2, 3} | {3, 4, 5})         #并集，自动去除重复元素
# {1, 2, 3, 4, 5}
print({1, 2, 3} & {3, 4, 5})         #交集
# {3}
print({1, 2, 3} ^ {3, 4, 5})         #对称差集
# {1, 2, 4, 5}
print({1, 2, 3} - {3, 4, 5})         #差集
# {1, 2}


# and和or具有惰性求值特点，只计算必须计算的表达式。
# print(3>5 and a>3)          #注意，此时并没有定义变量a
# # False
# print(3>5 or a>3)           #3>5的值为False，所以需要计算后面表达式
# # NameError: name 'a' is not defined
# print(3<5 or a>3)           #3<5的值为True，不需要计算后面表达式
# True
print(3 and 5)              #最后一个计算的表达式的值作为整个表达式的值
# 5
print(3 and 5>2)
# True
print(3 not in [1, 2, 3])   #逻辑非运算not
# False
print(3 is not 5)           #not的计算结果只能是True或False之一
# True


# 逗号并不是运算符，只是一个普通分隔符。
print('a' in 'b', 'a')
# (False, 'a')
print('a' in ('b', 'a'))
# True
x = 3, 5
print(x)
# (3, 5)
print(3 == 3, 5)
# (True, 5)
x = 3+5, 7
print(x)
# (8, 7)


# Python不支持++和--运算符，只是两个连续的加号和减号。
i = 3
print(++i)                       #正正得正
# 3
print(+(+3))                     #与++i等价
# 3
# print(i++)                       #Python不支持++运算符，语法错误
# SyntaxError: invalid syntax
print(--i)                       #负负得正
# 3
print(-(-i))                     #与--i等价
# 3


# 在Python中，单个任何类型的对象或常数属于合法表达式，使用运算符连接的变量和常量以及函数调用的任意组合也属于合法的表达式。
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
# [1, 2, 3, 4, 5, 6]
d = list(map(str, c))
print(d)
# ['1', '2', '3', '4', '5', '6']
print('Hello' + ' ' + 'world')
# 'Hello world'
print('welcome ' * 3)
# 'welcome welcome welcome '
print(('welcome,'*3).rstrip(',')+'!')
# 'welcome,welcome,welcome!'