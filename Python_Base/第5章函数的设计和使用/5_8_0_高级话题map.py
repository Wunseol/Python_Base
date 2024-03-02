# 内置函数map()可以将一个函数作用到一个或多个序列或迭代器对象上，返回可迭代的map对象。
list(map(str,range(5)))
# ['0', '1', '2', '3', '4']
def add5(v):
    return v+5

list(map(add5,range(10)))
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def add(x, y):return x+y
list(map(add, range(5), range(5)))
# [0, 2, 4, 6, 8]


