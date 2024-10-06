# 导入pandas库，用于数据操作和分析
import pandas as pd

# 创建一个Series对象，包含一组年龄数据，并用名字作为索引
s2 = pd.Series([25, 23, 42, 21, 23], index=['Jack', 'Lucy', 'Helen', 'Milky', 'Jasper'])

# 输出Series对象s2，展示各个人员的年龄，当你打印 s2 时，Pandas 会显示整个 Series 对象，包括索引、值以及数据类型
print(s2)

print(23 in s2)

print('Jack' in s2)

# 检查23这个年龄是否存在于s2 Series中，并打印结果
print(s2.isin([23]).any())


# 让我们详细分析一下两种方法的不同之处。

# 1. print(23 in s2)
# 这种方法会检查 23 是否存在于 s2 的值中。然而，s2 是一个带有索引的 pd.Series 对象，因此 23 in s2 实际上是在检查索引中是否存在 23，而不是值中是否存在 23。

# 2. print(s2.isin([23]).any())
# 这种方法会检查 23 是否存在于 s2 的值中，并返回一个布尔值。

# 解释原因
# 23 in s2：

# 这个表达式实际上是在检查 23 是否存在于 s2 的索引中，而不是值中。
# 因为 s2 的索引是 ['Jack', 'Lucy', 'Helen', 'Milky', 'Jasper']，所以 23 不在索引中，因此输出 False。
# s2.isin([23]).any()：

# 这个表达式检查 23 是否存在于 s2 的值中。
# s2.isin([23]) 返回一个布尔 Series，表示哪些值等于 23。
# any() 方法检查这个布尔 Series 中是否有任何 True 值。
# 因为 s2 的值中有两个 23，所以输出 True。





# 该Python脚本执行以下功能：

# 导入pandas库以操作数据。
# 使用给定的年龄数据创建名为s2的Series对象，并设置相应的名字作为索引。
# 打印s2，显示每个人的年龄。
# 检查年龄23是否在s2中，并打印检查结果（True或False）。


