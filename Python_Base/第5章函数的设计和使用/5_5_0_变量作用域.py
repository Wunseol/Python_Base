# 变量起作用的代码范围称为变量的作用域，不同作用域内变量名可以相同，互不影响。
# 在函数内部定义的普通变量只在函数内部起作用，称为局部变量。当函数执行结束后，局部变量自动删除，不再可以使用。
# 局部变量的引用比全局变量速度快。
# 全局变量会增加函数之间的隐式耦合。

# 全局变量可以通过关键字global来定义。这分为两种情况：
# 一个变量已在函数外定义，如果在函数内需要为这个变量赋值，并要将这个赋值结果反映到函数外，可以在函数内使用global将其声明为全局变量。
# 如果一个变量在函数外没有定义，在函数内部也可以直接将一个变量定义为全局变量，该函数执行后，将增加一个新的全局变量。

# 也可以这么理解：
# 在函数内只引用某个变量的值而没有为其赋新值，如果这样的操作可以执行，那么该变量为（隐式的）全局变量；
# 如果在函数内任意位置有为变量赋新值的操作，该变量即被认为是（隐式的）局部变量，除非在函数内显式地用关键字global进行声明。

def demo():
    global x
    x = 3
    y = 4
    print(x,y)

x = 5
print(demo())
# 3  4
print(x)
# 3
# print(y)
# NameError: name 'y' is not defined

del x
# print(x)
# NameError: name 'x' is not defined
print(demo())
# 3  4
print(x)
# 3
# print(y)
# NameError: name 'y' is not defined


# 注意：在某个作用域内任意位置只要有为变量赋值的操作，该变量在这个作用域内就是局部变量，除非使用global进行了声明。
x = 3
def f():
    print(x)           #本意是先输出全局变量x的值，但是不允许这样做
    x = 5              #有赋值操作，因此在整个作用域内x都是局部变量
    print(x)

# f()
# Traceback (most recent call last):
#   File "<pyshell#10>", line 1, in <module>
#     f()
#   File "<pyshell#9>", line 2, in f
#     print(x)
# UnboundLocalError: local variable 'x' referenced before assignment


# 如果局部变量与全局变量具有相同的名字，那么该局部变量会在自己的作用域内隐藏同名的全局变量。

def demo():
    x = 3         #创建了局部变量，并自动隐藏了同名的全局变量	
x = 5
print(x)
# 5
demo()
print(x)             #函数执行不影响外面全局变量的值
# 5

