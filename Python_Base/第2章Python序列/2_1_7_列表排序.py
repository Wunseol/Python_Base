# 使用列表对象的sort()方法进行原地排序，支持多种不同的排序方法。
aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
import random
random.shuffle(aList)
print(aList)
# [3, 4, 15, 11, 9, 17, 13, 6, 7, 5]
aList.sort()                            #默认是升序排序
print(aList)
# [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
aList.sort(reverse=True)              #降序排序
print(aList)
# [17, 15, 13, 11, 9, 7, 6, 5, 4, 3]


# 使用内置函数sorted()对列表进行排序并返回新列表。
print(aList)
# [9, 7, 6, 5, 4, 3, 17, 15, 13, 11]
print(sorted(aList))                            #升序排序
# [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
print(sorted(aList,reverse=True))             #降序排序
# [17, 15, 13, 11, 9, 7, 6, 5, 4, 3]


# 使用列表对象的reverse()方法将元素原地逆序。
aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
aList.reverse()
print(aList)
# [17, 15, 13, 11, 9, 7, 6, 5, 4, 3]


# 使用内置函数reversed()对列表元素进行逆序排列并返回迭代对象。
aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
newList = reversed(aList)         #返回reversed对象
print(list(newList))                     #把reversed对象转换成列表
# [17, 15, 13, 11, 9, 7, 6, 5, 4, 3]
newList = reversed(aList)         #重新创建reversed对象
for i in newList:
    print(i, end=' ')
# 17 15 13 11 9 7 6 5 4 3


