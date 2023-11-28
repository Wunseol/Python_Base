# 用Python进行程序设计，输入是通过input( )函数来实现的，input( )的一般格式为：
x = input('提示：')

# 在Python 3.x中，input()函数用来接收用户的键盘输入，不论用户输入数据时使用什么界定符，input()函数的返回结果都是字符串，需要将其转换为相应的类型再处理。
x = input('Please input:')
# Please input:3
print(type(x))
print(x)
# <class 'str'>
x = input('Please input:')
# Please input:'1'
print(type(x))
print(x)
# <class 'str'>
x = input('Please input:')
# Please input:[1,2,3]
print(type(x))
print(x)
# <class 'str'>


# Python 3.x中使用print()函数进行输出。
print(3, 5, 7)
# 3 5 7
print(3, 5, 7, sep=',')    #指定分隔符
# 3,5,7
print(3, 5, 7, sep=':')
# 3:5:7
for i in range(10,20):
    print(i, end=' ')          #不换行


# 试试下面的代码在命令提示符环境会有什么样的运行效果：
from time import sleep
for i in range(101):
    print(i, '%', end='\r')
    sleep(0.05)
