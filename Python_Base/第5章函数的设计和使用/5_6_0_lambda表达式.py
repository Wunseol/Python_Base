# lambda表达式可以用来声明匿名函数（也可以定义具名函数），也就是没有函数名字的临时使用的小函数，尤其适合需要一个函数作为另一个函数参数的场合。
# lambda表达式只可以包含一个表达式，该表达式可以任意复杂，其计算结果可以看作是函数的返回值。

f = lambda x, y, z: x+y+z        #可以给lambda表达式起名字
print(f(1,2,3))                         #像函数一样调用
# 6
g = lambda x, y=2, z=3: x+y+z    #参数默认值
print(g(1))
# 6
print(g(2, z=4, y=5))                   #关键参数
# 11

L = [(lambda x: x**2),                   #匿名函数
         (lambda x: x**3),
         (lambda x: x**4)]
print(L[0](2),L[1](2),L[2](2))           #调用lambda表达式
# 4 8 16
D = {'f1':(lambda:2+3), 'f2':(lambda:2*3), 'f3':(lambda:2**3)}
print(D['f1'](), D['f2'](), D['f3']())
# 5 6 8
L = [1,2,3,4,5]
print(list(map(lambda x: x+10, L)))      #lambda表达式作为函数参数
# [11, 12, 13, 14, 15]
print(L)
# [1, 2, 3, 4, 5]


def demo(n):
    return n*n

print(demo(5))
# 25
a_list = [1,2,3,4,5]
print(list(map(lambda x: demo(x), a_list)))  #在lambda表达式中调用函数
                                          #等价于list(map(demo, a_list))
# [1, 4, 9, 16, 25]


data = list(range(20))           #创建列表
print(data)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
import random
random.shuffle(data)             #打乱顺序
print(data)
# [4, 3, 11, 13, 12, 15, 9, 2, 10, 6, 19, 18, 14, 8, 0, 7, 5, 17, 1, 16]
data.sort(key=lambda x: x)       #和不指定规则效果一样
print(data)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


data.sort(key=lambda x: len(str(x))) #按转换成字符串以后的长度排序
print(data)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
data.sort(key=lambda x: len(str(x)), reverse=True)
                                         #降序排序
print(data)
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


data.sort(key=lambda x: len(str(x))) #按转换成字符串以后的长度排序
print(data)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
data.sort(key=lambda x: len(str(x)), reverse=True)
                                         #降序排序
print(data)
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

import random
x = [[random.randint(1,10) for j in range(5)] for i in range(5)]
                                    #包含5个子列表的列表
                                    #每个子列表中包含5个1到10之间的随机数
for item in x:
    print(item)	
# [5, 6, 8, 7, 4]
# [1, 5, 3, 9, 4]
# [9, 6, 10, 7, 6]
# [8, 2, 7, 1, 6]
# [1, 7, 5, 3, 5]


y = sorted(x, key=lambda item: (item[1], item[4]))           #按子列表中第2个元素升序、第5个元素升序排序
for item in y:
    print(item)	
# [8, 2, 7, 1, 6]
# [1, 5, 3, 9, 4]
# [5, 6, 8, 7, 4]
# [9, 6, 10, 7, 6]
# [1, 7, 5, 3, 5]


from random import sample      #sample()函数选择多个不重复的随机元素
data = [sample(range(100), 10) for i in range(5)]
for row in data:
    print(row)
# [72, 47, 87, 27, 75, 14, 0, 67, 16, 52]
# [28, 93, 74, 15, 52, 77, 87, 50, 79, 43]
# [32, 31, 25, 67, 63, 84, 27, 53, 79, 93]
# [22, 3, 56, 91, 75, 83, 51, 89, 14, 45]
# [90, 46, 29, 56, 72, 38, 88, 69, 50, 11]

for row in sorted(data):
    print(row)	
# [22, 3, 56, 91, 75, 83, 51, 89, 14, 45]
# [28, 93, 74, 15, 52, 77, 87, 50, 79, 43]
# [32, 31, 25, 67, 63, 84, 27, 53, 79, 93]
# [72, 47, 87, 27, 75, 14, 0, 67, 16, 52]
# [90, 46, 29, 56, 72, 38, 88, 69, 50, 11]


for row in sorted(data, key=lambda row:row[1]):
    print(row)                     #按每行第2个元素升序输出
# [22, 3, 56, 91, 75, 83, 51, 89, 14, 45]
# [32, 31, 25, 67, 63, 84, 27, 53, 79, 93]
# [90, 46, 29, 56, 72, 38, 88, 69, 50, 11]
# [72, 47, 87, 27, 75, 14, 0, 67, 16, 52]
# [28, 93, 74, 15, 52, 77, 87, 50, 79, 43]


from functools import reduce
reduce(lambda x,y:x*y, data[0])    #第一行所有数字相乘
# 0
reduce(lambda x,y:x*y, data[1])    #第二行所有数字相乘
# 171018396981432000
list(map(lambda row:row[0], data)) #获取每行第一个元素
# [72, 28, 32, 22, 90]
list(map(lambda row:row[data.index(row)], data))
                                       #获取对角线上的元素
# [72, 93, 25, 91, 72]
max(data, key=lambda row:row[-1]) #最后一个元素最大的行
# [32, 31, 25, 67, 63, 84, 27, 53, 79, 93]

for row in filter(lambda row:sum(row)%2==0, data):
    print(row)                        #所有元素之和为偶数的行
	
# [28, 93, 74, 15, 52, 77, 87, 50, 79, 43]
# [32, 31, 25, 67, 63, 84, 27, 53, 79, 93]
reduce(lambda x,y:[xx+yy for xx,yy in zip(x,y)], data)
                                      #每列元素求和
# [244, 220, 271, 256, 337, 296, 253, 328, 238, 244]
reduce(lambda x,y:list(map(lambda xx,yy:xx+yy, x, y)), data)
                                      #每列元素求和
# [244, 220, 271, 256, 337, 296, 253, 328, 238, 244]
list(reduce(lambda x,y:map(lambda xx,yy:xx+yy, x, y), data))
                                      #每列元素求和
# [244, 220, 271, 256, 337, 296, 253, 328, 238, 244]


# 使用lambda表达式时，要注意作用域带来的问题。
r = []
for x in range(10):
    r.append(lambda: x**2)
	
r[0]()
# 81
r[1]()
# 81
r = []
for x in range(10):
    r.append(lambda n=x: n**2)

r[0]()
# 0
r[1]()
# 1
r[2]()
# 4

