import pandas as pd

# (1)查看mtcars数据集的维度、大小等信息；
# 从指定路径读取mtcars数据集
mtcars = pd.read_csv(r'C:\VS Code\Python\python_智能统计学技术\3_1_pandas的应用示例\mtcars.csv')
# 打印数据集的维度
print('mtcars的维度为:', mtcars.ndim)
# 打印数据集的大小
print('mtcars的大小为:', mtcars.shape)


# (2)使用describe方法对整个mtcars数据集进行描述性统计；
# 对数据集进行描述性统计，并打印结果
print('mtcars的描述性统计为:\n', mtcars.describe())


# (3)计算不同cyl（汽缸数）、carb（化油器）对应的mpg（油耗）和hp（马力）的均值。
# 从数据集中选择cyl, carb, mpg, hp这几列
data = mtcars.loc[:, ['cyl', 'carb', 'mpg', 'hp']]
# 按cyl和carb列进行分组，并计算mpg和hp的均值
mpgHp = data.groupby(['cyl', 'carb']).mean()
# 打印不同cyl和carb对应的mpg和hp的均值
print('不同cyl(汽缸数),carb(化油器)对应的mpg(油耗)和hp(马力)的均值为：\n', mpgHp)

