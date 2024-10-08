# 读取用户输入的次数
n = int(input('读取用户输入的次数:'))

# 初始化一个空列表，用于存储用户输入的字符串
list1 = []

# 循环读取用户输入的字符串，并添加到列表中
for i in range(n):
    list1.append(input())

# 循环处理列表中的每个字符串
for i in range(n):
    # 将16进制字符串转换为10进制整数，再转换为8进制字符串
    result = oct(int(list1[i], 16))
    # 输出转换后的8进制字符串，忽略前缀"0o"
    print(result[2:])


