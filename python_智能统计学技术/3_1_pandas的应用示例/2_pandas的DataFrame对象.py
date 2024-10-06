# 导入pandas库，用于数据处理
import pandas as pd

# 创建一个DataFrame，其中包含定制的索引和列名
# 这对于后续的数据访问和操作是非常方便的
df1 = pd.DataFrame([[5, 2, 3], [4, 5, 6],[7,8,9]], index=['A','B','D'], columns=['C1','C2','C3'])

print(df1)

# 访问并打印DataFrame中特定行和列的值
# 这里演示了如何使用.loc操作符进行索引和列的名称访问
print(df1.loc['D','C2'])

