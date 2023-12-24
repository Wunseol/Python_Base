# 列表推导式使用非常简洁的方式来快速生成满足特定需求的列表，代码具有非常强的可读性。
# 列表推导式语法形式为：
# [expression for expr1 in sequence1 if condition1
#             for expr2 in sequence2 if condition2
#             for expr3 in sequence3 if condition3
#             ...
#             for exprN in sequenceN if conditionN]

# 列表推导式在内部实际上是一个循环结构，只是形式更加简洁，例如：
aList = [x*x for x in range(10)]
# 相当于
aList = []
for x in range(10):
	aList.append(x*x)


# 已知有一个包含一些同学成绩的字典，计算成绩的最高分、最低分、平均分，并查找所有最高分同学。

scores = {"Zhang San": 45, "Li Si": 78, "Wang Wu": 40,
              "Zhou Liu": 96,"Zhao Qi": 65, "Sun Ba": 90,
              "Zheng Jiu": 78, "Wu Shi": 99,"Dong Shiyi": 60}
highest = max(scores.values())
lowest = min(scores.values())
average = sum(scores.values())*1.0/len(scores)
print(highest, lowest, average)
# 99  40  72.33333333333333
highestPerson = [name for name, score in scores.items() if score == highest]
print(highestPerson)
# ['Wu Shi']

# 在列表推导式中使用多个循环，实现多序列元素的任意组合
print([(x, y) for x in range(3) for y in range(3)])
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]



