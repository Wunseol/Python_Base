# 直接将集合赋值给变量
a = {3, 5}
print(a)

# 使用set将其他类型数据转换为集合
a_set = set(range(8,14))
print(a_set)
# {8, 9, 10, 11, 12, 13}
b_set = set([0, 1, 2, 3, 0, 1, 2, 3, 7, 8])   #自动去除重复
print(b_set)
# {0, 1, 2, 3, 7, 8}
c_set = set()                                 #空集合
print(c_set)
# set()

# 当不再使用某个集合时，可以使用del命令删除整个集合。集合对象的pop()方法弹出并删除其中一个元素，remove()方法直接删除指定元素，clear()方法清空集合。
a = {1, 4, 2, 3}
print(a.pop())
# 1
print(a.pop())
# 2
print(a)
# {3, 4}
a.add(2)
print(a)
# {2, 3, 4}
a.remove(3)
print(a)
# {2, 4}

