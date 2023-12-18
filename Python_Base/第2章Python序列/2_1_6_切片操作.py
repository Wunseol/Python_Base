# 切片适用于列表、元组、字符串、range对象等类型，但作用于列表时功能最强大。可以使用切片来截取列表中的任何部分，得到一个新列表，也可以通过切片来修改和删除列表中部分元素，甚至可以通过切片操作为列表对象增加元素。
# 切片使用2个冒号分隔的3个数字来完成：
# 第一个数字表示切片开始位置（默认为0）。
# 第二个数字表示切片截止（但不包含）位置（默认为列表长度）。
# 第三个数字表示切片的步长（默认为1），当步长省略时可以顺便省略最后一个冒号。
# 切片操作不会因为下标越界而抛出异常，而是简单地在列表尾部截断或者返回一个空列表，代码具有更强的健壮性。
aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
print(aList[0:100:1])                       #前100个元素，自动截断
# [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
print(aList[::])                            #返回包含所有元素的新列表
# [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
print(aList[::-1])                          #逆序的所有元素
# [17, 15, 13, 11, 9, 7, 6, 5, 4, 3]
print(aList[::2])                           #偶数位置，隔一个取一个
# [3, 5, 7, 11, 15]
print(aList[1::2])                          #奇数位置，隔一个取一个
# [4, 6, 9, 13, 17]
print(aList[3::])                           #从下标3开始的所有元素
# [6, 7, 9, 11, 13, 15, 17]
print(aList[3:6])                           #下标在[3, 6)之间的所有元素
# [6, 7, 9]
print(aList[100:])                          #下标100之后的所有元素，自动截断
# []
# print(aList[100])                           #直接使用下标访问会发生越界
# IndexError: list index out of range

# 可以使用切片来原地修改列表内容
aList = [3, 5, 7]
aList[len(aList):] = [9]      #在尾部追加元素
print(aList)
# [3, 5, 7, 9]
aList[:3] = [1, 2, 3]         #替换前3个元素
print(aList)
# [1, 2, 3, 9]
aList[:3] = []                #删除前3个元素
print(aList)
# [9]
aList = list(range(10))
print(aList)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
aList[::2] = [0]*5            #替换偶数位置上的元素
print(aList)
# [0, 1, 0, 3, 0, 5, 0, 7, 0, 9]
# print(aList[::2] = [0]*3)            #切片不连续，两侧元素个数必须一样多
# ValueError: attempt to assign sequence of size 3 to extended slice of size 5

# 使用del与切片结合来删除列表元素
aList = [3,5,7,9,11]
del aList[:3]                          #删除前3个元素
print(aList)
# [9, 11]

aList = [3,5,7,9,11]
del aList[::2]                         #删除偶数位置上的元素
print(aList)
# [5, 9]

# 切片返回的是浅复制。所谓浅复制，是指生成一个新的列表，并且把原列表中所选元素的引用都复制到新列表中。如果原列表中只包含整数、实数、复数等基本类型或元组、字符串这样的不可变类型的数据，一般是没有问题的。
aList = [3, 5, 7]
bList = aList[::]                 #切片，浅复制
print(aList == bList)                    #两个列表的元素完全一样
# True
print(aList is bList)                    #但不是同一个对象
# False
print(id(aList) == id(bList))            #内存地址不一样
# False
bList[1] = 8                      #修改其中一个不会影响另一个
print(bList)
# [3, 8, 7]
print(aList)
# [3, 5, 7]

# 如果原列表中包含列表之类的可变数据类型，由于浅复制时只是把子列表的引用复制到新列表中，这样的话修改任何一个都会影响另外一个。
aList = [3, 5, 7]
bList = aList[:]           #切片，浅复制
print(aList == bList)             #切片刚完成的瞬间，bList和aList中包含同样的元素引用
# True
bList[1] = 8               #列表中只包含可哈希对象，修改bList时不影响aList
print(bList)
# [3, 8, 7]
print(aList)
# [3, 5, 7]
aList = [3, [5], 7]        #列表aList中包含可变的列表对象
bList = aList[:]           #切片
bList[1].append(6)         #调用子列表的append()方法，这个方法是原地操作的
print(bList)
# [3, [5, 6], 7]
print(aList)                      #aList受到影响
# [3, [5, 6], 7]

# 标准库copy中的deepcopy()函数实现深复制。所谓深复制，是指对原列表中的元素进行递归，把所有的值都复制到新列表中，对嵌套的子列表不再是复制引用。新列表和原列表是互相独立，修改任何一个都不会影响另外一个。
aList = [3, [5], 7]
import copy
bList = copy.deepcopy(aList) #深赋值，递归复制，直到遇到可哈希对象
                           #aList和bList完全独立，互相不影响
print(aList == bList)
# True
print(aList is bList)
# False
bList[1].append(6)         #修改bList不会影响aList
print(bList)
# [3, [5, 6], 7]
print(aList)
# [3, [5], 7]


