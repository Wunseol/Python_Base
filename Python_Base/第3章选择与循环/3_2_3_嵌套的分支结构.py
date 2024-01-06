# if 表达式1:
#     语句块1
# elif 表达式2:
#     语句块2
# elif 表达式3:
#     语句块3
# else:
#     语句块4
# 其中，关键字elif是else if的缩写。

# 利用多分支选择结构将成绩从百分制变换到等级制。
# def func(score):
#     if score > 100:
#         return 'wrong score.must <= 100.'
#     elif score >= 90:
#         return 'A'
#     elif score >= 80:
#         return 'B'
#     elif score >= 70:
#         return 'C'
#     elif score >= 60:
#         return 'D'
#     elif score >= 0:
#         return 'E'
#     else:
#         return 'wrong score.must >0'	

# if 表达式1:
#     语句块1
#     if 表达式2:
#         语句块2
#     else:
#         语句块3
# else:
#     if 表达式4:
#         语句块4

# 注意：缩进必须要正确并且一致。


# 使用嵌套的选择结构实现百分制成绩到等级制的转换。
# def func(score):
#     degree = 'DCBAAE'
#     if score > 100 or score < 0:
#         return 'wrong score.must between 0 and 100.'
#     else:
#         index = (score - 60)//10
#         if index >= 0:
#             return degree[index]
#         else:
#             return degree[-1]




