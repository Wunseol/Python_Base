# 例3-4  计算1+2+3+…+100 的值。
s = 0
for i in range(1,101):
    s = s + i
print('1+2+3+…+100 = ', s)
print('1+2+3+…+100 = ', sum(range(1,101)))


# 例3-5  输出序列中的元素。
a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
for i, v in enumerate(a_list):
    print('列表的第', i+1, '个元素是：', v)

# 例3-6  求1~100之间能被7整除，但不能同时被5整除的所有整数 。
for i in range(1,101):
    if i%7 == 0 and i%5 != 0:
        print(i)

# for num in range(7, 101, 7):
#     if num%5 != 0:
#         print(num)

# 例3-7  输出所有3位“水仙花数”。所谓n位水仙花数是指1个n位的十进制数，其各位数字的n次方之和等于该数本身。例如：153是水仙花数，因为153 = 13 + 53 + 33 。

# 方法一：
for i in range(100, 1000):
    bai, shi, ge = map(int, str(i))
    if ge**3 + shi**3 + bai**3 == i:
        print(i)

# 例3-8  统计考试成绩中优、良、中、及格、不及格的人数。
# 方法一:
scores = [89,70,49,87,92,84,73,71,78,81,90,37,
          77,82,81,79,80,82,75,90,54,80,70,68,61]
groups = {'优秀':0, '良':0, '中':0, '及格':0, '不及格':0}
for score in scores:
    if score>=90:
        groups['优秀'] = groups['优秀']+1
    elif score>=80:
        groups['良'] = groups['良']+1
    elif score>=70:
        groups['中'] = groups['中']+1
    elif score>=60:
        groups['及格'] = groups['及格']+1
    else:
        groups['不及格'] = groups['不及格']+1
print(groups)

# 例3-9  打印九九乘法表。
#ljust() 方法返回一个原字符串左对齐，并使用指定字符填充至指定长度的新字符串，默认的填充字符为空格。如果指定的长度小于原字符串的长度则返回原字符串。
for i in range(1,10):
    for j in range(1,i+1):
        print('{0}*{1}={2}'.format(i,j,i*j).ljust(6), end=' ')
    print()

# 例3-10  求200以内能被17整除的最大正整数。
for i in range(200,0,-1):
    if i%17 == 0:
        print(i)
        break

# 例3-11  判断一个数是否为素数。
import math
n = input('Input an integer:')
n = int(n)
m = math.ceil(math.sqrt(n)+1)
for i in range(2, m):
    if n%i == 0 and i<n:
        print('No')
        break
else:
    print('Yes')

# 例3-12  鸡兔同笼问题。假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只。
for ji in range(0, 31):
    if 2*ji + (30-ji)*4 == 90:
        print('ji:', ji, ' tu:', 30-ji)
        break

# 例3-13  编写程序，输出由1、2、3、4这四个数字组成的每位数都不相同的所有三位数。
digits = (1, 2, 3, 4)
for i in digits:
    for j in digits:
        for k in digits:
            if i!=j and j!=k and i!=k:
                print(i*100+j*10+k)


# 从代码优化的角度来讲，上面这段代码并不是很好，其中有些判断完全可以在外层循环来做，从而提高运行效率。
# digits = (1, 2, 3, 4)
# for i in digits:
#     for j in digits:
#         if j==i:
#             continue
#         for k in digits:
#             if k==i or k==j:
#                 continue
#             print(i*100+j*10+k)

# 当然，还可以进一步优化。
# digits = (1, 2, 3, 4)
# for i in digits:
#     ii = i*100
#     for j in digits:
#         if j == i:
#             continue
#         jj = j * 10
#         for k in digits:
#             if k!=i and k!=j:
#                 print(ii + jj + k)

# 也可以使用集合实现同样功能。
# digits = {1, 2, 3, 4}
# for i in digits:
#     ii = i*100
#     for j in digits-{i}:
#         jj = j * 10
#         for k in digits-{i,j}:
#             print(ii + jj + k)

