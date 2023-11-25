# 把列表中的所有数字都加5，得到新列表。（函数式编程）

x = list(range(10))
print(x)

def add5(num): # 自定义函数，接收一个数字，加5后返回
    return num+5

print(list(map(add5, x))) # 把函数add5映射到x中的每个元素

print(list(map(lambda num: num+5, x))) # lambda表达式，等价于函数add5

