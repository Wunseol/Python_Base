# 内置函数不需要导入任何模块即可使用
# 执行下面的命令可以列出所有内置函数
print(dir(__builtins__))


# abs(x) # 返回数字x的绝对值或复数x的模
# bin(x) # 把整数x转换为二进制串表示形式
# 内置函数bin()、oct()、hex()用来将整数转换为二进制、八进制和十六进制形式，这三个函数都要求参数必须为整数。
print("内置函数bin()、oct()、hex()用来将整数转换为二进制、八进制和十六进制形式，这三个函数都要求参数必须为整数。")
print(bin(555))                      # 把数字转换为二进制串
# '0b1000101011'
print(oct(555))                      # 转换为八进制串
# '0o1053'
print(hex(555))                      # 转换为十六进制串
# '0x22b'

# exit() # 退出当前解释器环境
# float(x) # 把整数或字符串x转换为浮点数并返回

# int(x[, d]) # 返回实数（float）、分数（Fraction）或高精度实数（Decimal）x的整数部分，或把d进制的字符串x转换为十进制并返回，d默认为十进制
# 内置函数int()用来把实数转换为整数，或把数字字符串按指定进制转换为十进制数。
print(int(3.5))
# 3
print(int(-3.5))
# -3
print(int('101', 2))             # 二进制
# 5
print(int('101', 16))            # 十六进制
# 257


# ord()和chr()是一对功能相反的函数，ord()用来返回单个字符的序数或Unicode码，而chr()则用来返回某序数对应的字符，str()则直接将其任意类型参数转换为字符串。
print("ord()和chr()是一对功能相反的函数，ord()用来返回单个字符的序数或Unicode码，而chr()则用来返回某序数对应的字符，str()则直接将其任意类型参数转换为字符串。")
print(ord('a')) 
97   
print(chr(ord('A')+1))           
# 'B'                
print(str(1234))
# '1234'                                
print(str((1,2,3))) 
# '(1, 2, 3)'     
print(chr(65))
# 'A'
print(str(1))
# '1'
print(str([1,2,3]))
# '[1, 2, 3]'
print(str({1,2,3}))
# '{1, 2, 3}'


# max()、min()、sum()这三个内置函数分别用于计算列表、元组或其他可迭代对象中所有元素最大值、最小值以及所有元素之和，sum()要求元素支持加法运算，max()和min()则要求序列或可迭代对象中的元素之间可比较大小。
import random
a = [random.randint(1,100) for i in range(10)]   #列表推导式
print(a)
# [72, 26, 80, 65, 34, 86, 19, 74, 52, 40]
print(max(a), min(a), sum(a))
# 86 19 548
print(sum(a)/len(a))
# 54.8


# 内置函数max()和min()的key参数可以用来指定比较规则。
# key关键字的作用是：对每个元素先使用key指定的function来处理，然后再比较、返回预期的元素。
# key参数的值也可以使用自定义函数。
x = ['21', '1234', '9']
print(max(x))
# '9'
print(max(x, key=len))
# '1234'
print(max(x, key=int))
# '1234'


from random import randrange
x = [[randrange(1,100) for i in range(10)] for j in range(5)]
for item in x:  
    print(item)
	
# [15, 50, 38, 53, 58, 13, 22, 54, 7, 45]
# [45, 63, 58, 89, 85, 91, 77, 45, 53, 50]
# [80, 10, 46, 16, 71, 73, 13, 68, 94, 50]
# [66, 4, 49, 67, 26, 58, 52, 46, 69, 99]
# [35, 57, 63, 35, 71, 18, 86, 2, 16, 87]
print(max(x, key=sum))       #求所有元素之和最大的子列表
# [45, 63, 58, 89, 85, 91, 77, 45, 53, 50]


# 内置函数sum()
print(sum([1,2,3,4]))
# 10
print(sum([[1], [2], [3], [4]], []))
# [1, 2, 3, 4]


# 内置函数type()和isinstance()可以判断数据类型。
print(type([3]))                             #查看[3]的类型
# <class 'list'>
print(type({3}) in (list, tuple, dict))      #判断{3}是否为list,tuple
                                          #或dict类型的实例
# False
print(isinstance(3, int))                    #判断3是否为int类型的实例
# True
print(isinstance(3j, (int, float, complex))) #判断3j是否为int,float
                                          #或complex类型
# True


# sorted()对列表、元组、字典、集合或其他可迭代对象进行排序并返回新列表。
import random
data = random.choices(range(50), k=11)
print(data)
# [18, 38, 35, 5, 13, 48, 13, 2, 19, 47, 3]
print(sorted(data))
# [2, 3, 5, 13, 13, 18, 19, 35, 38, 47, 48]
print(sorted(data)[len(data)//2])  #中位数
# 18


# reversed()对可迭代对象（生成器对象和具有惰性求值特性的zip、map、filter、enumerate等类似对象除外）进行翻转（首尾交换）并返回可迭代的reversed对象。
x = ['aaaa', 'bc', 'd', 'b', 'ba']
print(reversed(x))                 #逆序，返回reversed对象
# <list_reverseiterator object at 0x0000000002E6C3C8>
print(list(reversed(x)))           #reversed对象是可迭代的
# ['ba', 'b', 'd', 'bc', 'aaaa']


# range()语法格式为range([start,] end [, step] )，返回具有惰性求值特点的range对象，其中包含左闭右开区间[start,end)内以step为步长的整数。参数start默认为0，step默认为1。
print(range(5))                  #start默认为0，step默认为1
# range(0, 5)
print(list([0, 1, 2, 3, 4]))
# [0, 1, 2, 3, 4]
print(list(range(1, 10, 2)))     #指定起始值和步长
# [1, 3, 5, 7, 9]
print(list(range(9, 0, -2)))     #步长为负数时，start应比end大
# [9, 7, 5, 3, 1]


# enumerate()函数用来枚举可迭代对象中的元素，返回可迭代的enumerate对象，其中每个元素都是包含索引和值的元组。
print(list(enumerate('abcd')))                        #枚举字符串中的元素
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
print(list(enumerate(['Python', 'Great'])))          #枚举列表中的元素
# [(0, 'Python'), (1, 'Great')]
print(list(enumerate({'a':97, 'b':98, 'c':99}.items()))) #枚举字典中的元素
# [(0, ('a', 97)), (1, ('b', 98)), (2, ('c', 99))]
for index, value in enumerate(range(10, 15)):  #枚举range对象中的元素
    print((index, value), end=' ')
# (0, 10) (1, 11) (2, 12) (3, 13) (4, 14) 



# 内置函数map()把一个函数func依次映射到序列或迭代器对象的每个元素上，并返回一个可迭代的map对象作为结果，map对象中每个元素是原序列中元素经过函数func处理后的结果。
print(list(map(str, range(5))))  #把列表中元素转换为字符串
# ['0', '1', '2', '3', '4']
def add5(v):              #单参数函数
    return v+5

print(list(map(add5, range(10))))#把单参数函数映射到一个序列的所有元素
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
def add(x, y):            #可以接收2个参数的函数
    return x+y

print(list(map(add, range(5), range(5,10))))
                              #把双参数函数映射到两个序列上
# [5, 7, 9, 11, 13]


import random
x = random.randint(1, 1e30)     #生成指定范围内的随机整数
print(x)
# 839746558215897242220046223150
print(list(map(int, str(x))))          #提取大整数每位上的数字
# [8, 3, 9, 7, 4, 6, 5, 5, 8, 2, 1, 5, 8, 9, 7, 2, 4, 2, 2, 2, 0, 0, 4, 6, 2, 2, 3, 1, 5, 0]


# 标准库functools中的函数reduce()可以将一个接收2个参数的函数以迭代累积的方式从左到右依次作用到一个序列或迭代器对象的所有元素上，并且允许指定一个初始值。
from functools import reduce
seq = list(range(1, 10))
print(reduce(lambda x, y: x+y, seq))
# 45



# 内置函数filter()将一个单参数函数作用到一个序列上，返回该序列中使得该函数返回值为True的那些元素组成的filter对象，如果指定函数为None，则返回序列中等价于True的元素。
seq = ['foo', 'x41', '?!', '***']
def func(x):
    return x.isalnum()                  #测试是否为字母或数字

print(filter(func, seq))                   #返回filter对象
# <filter object at 0x000000000305D898>
print(list(filter(func, seq)))             #把filter对象转换为列表
# ['foo', 'x41']
print(list(filter(str.isalnum, seq)))      #等价的用法
# ['foo', 'x41']

data = list(range(20))
print(data)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
filterObject = filter(lambda x:x%2==1, data)
                                 #过滤，只留下所有奇数
print(filterObject)
# <filter object at 0x000001D602B85828>
print(3 in filterObject)            #3以及3之前的元素都访问过了
# True
print(list(filterObject))           #现在所有元素都访问过了
# [5, 7, 9, 11, 13, 15, 17, 19]
print(list(filterObject))           #filterObject中不再包含任何元素
# []


# len(obj) # 返回对象obj包含的元素个数，适用于列表、元组、集合、字典、字符串以及range对象和其他可迭代对象

# list([x])、set([x])、tuple([x])、dict([x]) # 把对象x转换为列表、集合、元组或字典并返回，或生成空列表、空集合、空元组、空字典

# print(value, ..., sep=' ', end='\n', file = sys. stdout, flush=False) # 基本输出函数

# quit() # 退出当前解释器环境

# range([start,] end [, step] ) # 返回range对象，其中包含左闭右开区间[start,end)内以step为步长的整数

# sorted(iterable, key=None, reverse=False) # 返回排序后的列表，其中iterable表示要排序的序列或迭代对象，key用来指定排序规则或依据，reverse用来指定升序或降序。该函数不改变iterable内任何元素的顺序

# str(obj) # 把对象obj直接转换为字符串

# type(obj) # 返回对象obj的类型

# zip(seq1 [, seq2 [...]]) # 返回zip对象，其中元素为(seq1[i], seq2[i], ...)形式的元组，最终结果中包含的元素个数取决于所有参数序列或可迭代对象中最短的那个
# zip()函数用来把多个可迭代对象中的元素压缩到一起，返回一个可迭代的zip对象，其中每个元素都是包含原来的多个可迭代对象对应位置上元素的元组，如同拉拉链一样。

print(list(zip('abcd', [1, 2, 3])))  #压缩字符串和列表，元素个数与最短的列表一致
# [('a', 1), ('b', 2), ('c', 3)]
print(list(zip('123', 'abc', ',.!')))           #压缩3个序列
# [('1', 'a', ','), ('2', 'b', '.'), ('3', 'c', '!')]
x = zip('abcd', '1234')
print(list(x))
# [('a', '1'), ('b', '2'), ('c', '3'), ('d', '4')]


# map、filter、enumerate、zip等对象不仅具有惰性求值的特点，还有另外一个特点：访问过的元素不可再次访问。
x = map(str, range(10))
print(list(x))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(list(x))
# []
x = map(str, range(10))
print('2' in x)
# True
print('2' in x)
# False
print('8' in x)
# False



x = ['21', '1234', '9']

# print(x[0])
# print(x[1])
# print(x[2])


print(max(x))
# >>9
print(max(x, key = len))
# >>1234
print(max(x, key = int))
# >>1234

# 判断字符串大小
str1 = '1234'
str2 = '9'

if str1 > str2:
    print(f"{str1} 大于 {str2}")
elif str1 < str2:
    print(f"{str1} 小于 {str2}")
else:
    print(f"{str1} 等于 {str2}")

