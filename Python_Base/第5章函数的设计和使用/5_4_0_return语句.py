# return语句用来从一个函数中返回一个值，同时结束函数。
# 对于以下情况，Python将认为该函数以return None结束，返回空值：
# 函数没有return语句；
# 函数有return语句但是没有执行到；
# 函数有return也执行到了，但是没有返回任何值。

# 在调用函数或对象方法时，一定要注意有没有返回值。
a_list = [1, 2, 3, 4, 9, 5, 7]
print(sorted(a_list))
# [1, 2, 3, 4, 5, 7, 9]
print(a_list)
# [1, 2, 3, 4, 9, 5, 7]
print(a_list.sort())
# None
print(a_list)
# [1, 2, 3, 4, 5, 7, 9]


