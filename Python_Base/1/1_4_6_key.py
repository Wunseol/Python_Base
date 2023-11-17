

x = ['21', '1234', '9']

# print(x[0])
# print(x[1])
# print(x[2])


print(max(x))
# >>9
print(max(x, key = len))
# >>1234
print(max(x, key = int))
# >>1234

# 判断字符串大小
str1 = '1234'
str2 = '9'

if str1 > str2:
    print(f"{str1} 大于 {str2}")
elif str1 < str2:
    print(f"{str1} 小于 {str2}")
else:
    print(f"{str1} 等于 {str2}")





