# 例5-1  编写函数计算圆的面积。
from math import pi as PI

def CircleArea(r):
    if isinstance(r, (int,float)) and r>0: # 确保半径为大于0的数值
        return PI*r*r
    else:
        print('You must give me an integer or float as radius.')

print(CircleArea(3))


# 例5-2  编写函数，接收任意多个实数，返回一个元组，其中第一个元素为所有参数的平均值，其他元素为所有参数中大于平均值的实数。
def demo(*para):
    avg = sum(para)/len(para)
    g = [i for i in para if i>avg]
    return (avg,)+tuple(g)

print(demo(1,2,3,4))


def demo(*para):
    avg = sum(para)/len(para)
    g = filter(lambda num: num>avg, para)
    return (avg,)+tuple(g)


# 例5-3  编写函数，接收字符串参数，返回一个元组，其中第一个元素为大写字母个数，第二个元素为小写字母个数。
def demo(s):
    result = [0, 0]
    for ch in s:
        if 'a'<=ch<='z':
            result[1] += 1
        elif 'A'<=ch<='Z':
            result[0] += 1
    return tuple(result)

print(demo('aaaabbbbC'))



# 例5-4  编写函数，接收包含20个整数的列表lst和一个整数k作为参数，返回新列表。处理规则为：将列表lst中下标k（不包括k）之前的元素逆序，下标k（包括k）之后的元素逆序，然后将整个列表lst中的所有元素再逆序。
def demo(lst,k):
    x = lst[:]
    x[:k] = reversed(x[:k])
    x[k:] = reversed(x[k:])
    x.reverse()
    return x

lst = list(range(1,21))
print(demo(lst,5))


# 例5-6  编写函数，接收一个包含若干整数的列表参数lst，返回一个元组，其中第一个元素为列表lst中的最小值，其余元素为最小值在列表lst中的下标。
import random
def demo(lst):
    m = min(lst)
    result = (m,)+tuple((index for index,value in enumerate(lst)
                         if value==m))
    return result

x = [random.randint(1,20) for i in range(50)]
print(x)
print(demo(x))


# 例5-7  编写函数，接收一个整数t为参数，打印杨辉三角前t行。
# 解法一
def demo(t):
    print([1])
    print([1,1])
    line = [1,1]
    for i in range(2,t):
        r = []
        for j in range(0,len(line)-1):
            r.append(line[j]+line[j+1])
        line = [1]+r+[1]
        print(line)

demo(10)


# 例5-8  编写函数，接收一个正偶数为参数，输出两个素数，并且这两个素数之和等于原来的正偶数。如果存在多组符合条件的素数，则全部输出。
def IsPrime(n):
    m = int(n**0.5)+1
    for i in range(2, m):
        if n%i==0:
            return False
    return True
def demo(n):
    if isinstance(n,int) and n>0 and n%2==0:
        for i in range(3, n//2+1, 2):
            if IsPrime(i) and IsPrime(n-i):
                print(i, '+', n-i, '=', n)

demo(60)


# 例5-11  编写函数，计算字符串匹配的准确率。以打字练习程序为例，假设origin为原始内容，userInput为用户输入的内容，下面的代码用来测试用户输入的准确率。






