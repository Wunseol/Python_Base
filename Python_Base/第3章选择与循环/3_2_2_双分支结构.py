# if 表达式:
#     语句块1
# else:
#     语句块2


chTest = ['1', '2', '3', '4', '5']
if chTest:
    print(chTest)
else:
    print('Empty')
# ['1', '2', '3', '4', '5']

# Python还支持如下形式的表达式：
# value1 if condition else value2
# 当条件表达式condition的值与True等价时，表达式的值为value1，否则表达式的值为value2。在value1和value2中还可以使用复杂表达式，包括函数调用和基本输出语句。这个结构的表达式也具有惰性求值的特点。
a = 5
print(6) if a>3 else print(5)
# 6
print(6 if a>3 else 5)
# 6
b = 6 if a>13 else 9
print(b)
# 9

import math
import random
x = math.sqrt(9) if 2>3 else random.randint(1, 100)








