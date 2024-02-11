# 传递参数时，可以通过在实参序列前加一个星号将其解包，然后传递给多个单变量形参。
def demo(a, b, c):
    print(a+b+c)

seq = [1, 2, 3]
print(demo(*seq))
# 6
tup = (1, 2, 3)
print(demo(*tup))
# 6

dic = {1:'a', 2:'b', 3:'c'}
print(demo(*dic))
# 6
Set = {1, 2, 3}
print(demo(*Set))
# 6
print(demo(*dic.values()))
# abc

# 如果函数实参是字典，可以在前面加两个星号进行解包，等价于关键参数。
def demo(a, b, c):
    print(a+b+c)

dic = {'a':1, 'b':2, 'c':3}
print(demo(**dic))
# 6
print(demo(a=1, b=2, c=3))
# 6
print(demo(*dic.values()))
# 6


# 注意：调用函数时对实参序列使用一个星号*进行解包后的实参将会被当做普通位置参数对待，并且会在关键参数和使用两个星号**进行序列解包的参数之前进行处理。
def demo(a, b, c):            #定义函数
    print(a, b, c)	

demo(*(1, 2, 3))              #调用，序列解包
# 1 2 3
demo(1, *(2, 3))              #位置参数和序列解包同时使用
# 1 2 3
demo(1, *(2,), 3)
# 1 2 3

# demo(a=1, *(2, 3))         #序列解包相当于位置参数，优先处理
# Traceback (most recent call last):
#   File "<pyshell#26>", line 1, in <module>
#     demo(a=1, *(2, 3))
# TypeError: demo() got multiple values for argument 'a'

# demo(b=1, *(2, 3))
# Traceback (most recent call last):
#   File "<pyshell#27>", line 1, in <module>
#     demo(b=1, *(2, 3))
# TypeError: demo() got multiple values for argument 'b'
demo(c=1, *(2, 3))
# 2 3 1


# demo(**{'a':1, 'b':2}, *(3,)) #序列解包不能在关键参数解包之后
# SyntaxError: iterable argument unpacking follows keyword argument unpacking

# demo(*(3,), **{'a':1, 'b':2})
# Traceback (most recent call last):
#   File "<pyshell#30>", line 1, in <module>
#     demo(*(3,), **{'a':1, 'b':2})
# TypeError: demo() got multiple values for argument 'a'
print(demo(*(3,), **{'c':1, 'b':2}))
# 3 2 1
