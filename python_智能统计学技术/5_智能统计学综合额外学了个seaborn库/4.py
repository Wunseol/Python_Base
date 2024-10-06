import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# %matplotlib inline

#导数数据集'titanic'
# 读取本地 CSV 文件
file_path = r"C:\VS Code\Python\python_智能统计学技术\5_智能统计学综合额外学了个seaborn库\StudentsPerformance.csv"
titanic = pd.read_csv(file_path)
# titanic=sns.load_dataset(r'C:\VS Code\Python\python_智能统计学技术\5_智能统计学综合额外学了个seaborn库\titanic.csv')

#查看数据集的随机10行数据，用sample方法
titanic.sample(10)

#去除'age'中的缺失值，distplot不能处理缺失数据
age1=titanic['age'].dropna()

sns.distplot(age1)

