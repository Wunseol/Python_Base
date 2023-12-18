aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
aList = aList + [7]

# 使用in关键字来判断一个值是否存在于列表中，返回结果为“True”或“False”。
print(aList)
# [3, 4, 5, 5.5, 7, 9, 11, 13, 15, 17]
print(3 in aList)
# True
print(18 in aList)
# False
bList = [[1], [2], [3]]
print(3 in bList)
# False

print(3 not in bList)
# True
print([3] in bList)
# True
aList = [3, 5, 7, 9, 11]
bList = ['a', 'b', 'c', 'd']
print((3, 'a') in zip(aList, bList))
# True
for a, b in zip(aList, bList):
    print(a, b)
# 3 a
# 5 b
# 7 c
# 9 d

