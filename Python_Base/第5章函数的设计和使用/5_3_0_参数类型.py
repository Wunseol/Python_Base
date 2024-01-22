# 在Python中，函数参数有很多种：可以为普通参数、默认值参数、关键参数、可变长度参数等等。
# Python在定义函数时不需要指定形参的类型，完全由调用者传递的实参类型以及Python解释器的理解和推断来决定。
# 位置参数（positional arguments）是比较常用的形式，调用函数时实参和形参的顺序必须严格一致，并且实参和形参的数量必须相同。
def demo(a, b, c):
    print(a, b, c)
print(demo(3, 4, 5))                   #按位置传递参数
# 3 4 5
print(demo(3, 5, 4))
# 3 5 4
print(demo(1, 2, 3, 4))                #实参与形参数量必须相同
# TypeError: demo() takes 3 positional arguments but 4 were given
