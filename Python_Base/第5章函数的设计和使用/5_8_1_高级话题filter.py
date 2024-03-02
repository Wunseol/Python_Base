# 内置函数filter将一个函数作用到一个序列上，返回该序列中使得该函数返回值为True的那些元素组成的filter对象。可以使⽤list()函数将其转化为列表，这个列表包含过滤器对象中返回的所有的项。
# filter()函数的基本语法是：
#    filter(function,iterable)

def is_odd(n):
    return n % 2 == 1
 
tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)

# 输出结果：[1, 3, 5, 7, 9] 

# 用None过滤掉布尔值是False的对象：

# 将None作为filter()的第一个参数，让迭代器过滤掉Python中布尔值是False的对象

init_tanks = [11, False, 18, 21, "", 12, 34, 0, [], {}]
filtered_tanks = filter(None, init_tanks)
print(list(filtered_tanks))

# 输出：[11, 18, 21, 12, 34]






