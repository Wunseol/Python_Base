# 交集、并集、差集、对称差集等运算
a_set = set([8, 9, 10, 11, 12, 13])
b_set = {0, 1, 2, 3, 7, 8}
print(a_set | b_set)                             #并集
# {0, 1, 2, 3, 7, 8, 9, 10, 11, 12, 13}
print(a_set & b_set)                             #交集
# {8}
print(a_set - b_set)
# {9, 10, 11, 12, 13}
print(a_set ^ b_set)                             #对称差集
# {0, 1, 2, 3, 7, 9, 10, 11, 12, 13}


# 集合包含关系测试
x = {1, 2, 3}
y = {1, 2, 5}
z = {1, 2, 3, 4}
print(x < y)                                #比较集合大小/包含关系
# False
print(x < z)                                #真子集
# True
print(y < z)
# False
print({1, 2, 3} <= {1, 2, 3})               #子集
# True



