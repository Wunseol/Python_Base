# 把列表中的所有数字都加5，得到新列表。（命令式编程）

x = list(range(10)) # 创建列表
print(x)

y = []  # 空列表

for num in x:   # 循环，遍历x中的每个元素
    y.append(num + 5)

print(y)

print([num+5 for num in x]) # 列表推导式

