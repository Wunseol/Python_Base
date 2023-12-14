aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
aList = aList + [7]
print(aList)
# 使用下标直接访问列表元素，如果指定下标不存在，则抛出异常。
print(aList[3])
# 6
aList[3] = 5.5
print(aList)
# [3, 4, 5, 5.5, 7, 9, 11, 13, 15, 17]

# aList[15]
# Traceback (most recent call last):
#   File "<pyshell#34>", line 1, in <module>
#     aList[15]
# IndexError: list index out of range


# 使用列表对象的index()方法获取指定元素首次出现的下标，若列表对象中不存在指定元素，则抛出异常。
print(aList)
# [3, 4, 5, 5.5, 7, 9, 11, 13, 15, 17]
print(aList.index(7))
# 4

# aList.index(100)
# Traceback (most recent call last):
#   File "<pyshell#36>", line 1, in <module>
#     aList.index(100)
# ValueError: 100 is not in list

# 使用列表对象的count()方法统计指定元素在列表对象中出现的次数。
print(aList)
# [3, 4, 5, 5.5, 7, 9, 11, 13, 15, 17]
print(aList.count(7))
# 1
print(aList.count(0))
# 0
print(aList.count(8))
# 0

