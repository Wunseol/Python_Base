# len(列表)：返回列表中的元素个数，同样适用于元组、字典、集合、字符串等。
# max(列表)、 min(列表)：返回列表中的最大或最小元素，同样适用于元组、字典、集合、range对象等。
# sum(列表)：对列表的元素进行求和运算，对非数值型列表运算需要指定start参数，同样适用于元组、range。
print(sum(range(1, 11)))      #sum()函数的start参数默认为0
# 55
print(sum(range(1, 11), 5))   #指定start参数为5，等价于5+sum(range(1,11))
# 60

# zip()函数返回可迭代的zip对象。

aList = [1, 2, 3]
bList = [4, 5, 6]
cList = zip(aList, bList)                 #返回zip对象
print(cList)
# <zip object at 0x0000000003728908>
print(list(cList))                       #把zip对象转换成列表
# [(1, 4), (2, 5), (3, 6)]


# enumerate(列表):枚举列表元素，返回枚举对象，其中每个元素为包含下标和值的元组。该函数对元组、字符串同样有效。
for item in enumerate('abcdef'):
    print(item)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# (5, 'f')

