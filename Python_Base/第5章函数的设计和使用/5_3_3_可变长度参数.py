# 可变长度参数主要有两种形式：在参数名前加1个星号*或2个星号**。
# *parameter用来接收多个位置实参并将其放在元组中。
# **parameter接收多个关键参数并存放到字典中。
# *parameter的用法

def demo(*p):
    print(p)

print(demo(1,2,3))
# (1, 2, 3)
print(demo(1,2))
# (1, 2)
print(demo(1,2,3,4,5,6,7))
# (1, 2, 3, 4, 5, 6, 7)

# **parameter的用法

def demo(**p):
    for item in p.items():
        print(item)

print(demo(x=1,y=2,z=3))
# ('x', 1)
# ('y', 2)
# ('z', 3)


# 几种不同类型的参数可以混合使用，但是不建议这样做。
def func_4(a, b, c=4, *aa, **bb):
    print(a,b,c)
    print(aa)
    print(bb)

func_4(1,2,3,4,5,6,7,8,9,xx='1',yy='2',zz=3)
# 1 2 3
# (4, 5, 6, 7, 8, 9)
# {'xx': '1', 'yy': '2', 'zz': 3}
func_4(1,2,3,4,5,6,7,xx='1',yy='2',zz=3)
# 1 2 3
# (4, 5, 6, 7)
# {'xx': '1', 'yy': '2', 'zz': 3}
