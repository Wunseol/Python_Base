# 调用带有默认值参数的函数时，可以不对默认值参数进行赋值，也可以为其赋值，具有很大的灵活性。

def say(message, times=1 ):
    print(message*times)
say('hello')
# hello
say('hello',3)
# hello hello hello
say('hi',7)
# hi hi hi hi hi hi hi

# # 注意：默认值参数必须出现在函数参数列表的最右端，任何一个默认值参数右边不能有非默认值参数。
# def func(a=3, b, c=5):    # 失败，带默认值的参数后面有不带默认值的参数
#     print(a, b, c)
	
# # SyntaxError: non-default argument follows default argument
# def func(a=3, b):         # 失败，带默认值的参数后面有不带默认值的参数
#     print(a, b)
	
# SyntaxError: non-default argument follows default argument
def func(a, b, c=5):      # 成功
    print(a, b, c)

