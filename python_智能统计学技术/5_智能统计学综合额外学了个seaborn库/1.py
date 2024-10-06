import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Seaborn 是基于 Python 且非常受欢迎的图形可视化库，在 Matplotlib 的基础上，进行了更高级的封装，使得作图更加方便快捷。
# 即便是没有什么基础的人，也能通过极简的代码，做出具有分析价值而又十分美观的图形。
# Seaborn 可以实现 Python 环境下的绝大部分探索性分析的任务，图形化的表达帮助你对数据进行分析，而且对 Python 的其他库（比如 Numpy/Pandas/Scipy）有很好的支持。

# import important libaries
# import the dataset

data = pd.read_csv(r"C:\VS Code\Python\python_智能统计学技术\5_智能统计学综合额外学了个seaborn库\StudentsPerformance.csv")
data.head()

# print(data)
# data.split(" ")

student = data.drop(['gender','race/ethnicity', 'test preparation course','lunch','parental level of education'], axis=1)

# student = data.drop(['race/ethnicity','parental level of education'], axis=1)

student.head()

# print(student)

corelation = student.corr()


# # 图一
sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns,annot=True)

# # 图二
sns.pairplot(student)

# # 图三
sns.displot(student)

# 图四
sns.barplot(student)

# # sns.relplot(x= 'math score', y= 'reading score', hue= 'gender', data= student)

# 图五
sns.displot(student['math score'])

# 图六
sns.displot(student['reading score'])

# 图七
sns.displot(student['writing score'])

# sns.displot(student['math score'], bins=10)

plt.show()  # 在当前设备显示图片










# corelation = student.corr()

# sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns,annot=True)
# sns.pairplot(student)

# sns.relplot(x= 'math score', y= 'reading score', hue= 'gender', data= student)

# sns.distplot(student['math score'])

# sns.distplot(student['reading score'])

# sns.distplot(student['writing score'])
# sns.distplot(student['math score'], bins=10)


# 问题记录

# c:\VS Code\Python\智能统计学技术\5\1.py:29: UserWarning: 

# `distplot` is a deprecated function and will be removed in seaborn v0.14.0.

# Please adapt your code to use either `displot` (a figure-level function with
# similar flexibility) or `histplot` (an axes-level function for histograms).

# For a guide to updating your code to use the new functions, please see
# https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

#   sns.distplot(student['math score'])
# c:\VS Code\Python\智能统计学技术\5\1.py:31: UserWarning: 

# `distplot` is a deprecated function and will be removed in seaborn v0.14.0.

# Please adapt your code to use either `displot` (a figure-level function with
# similar flexibility) or `histplot` (an axes-level function for histograms).

# For a guide to updating your code to use the new functions, please see
# https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

#   sns.distplot(student['reading score'])
# c:\VS Code\Python\智能统计学技术\5\1.py:33: UserWarning: 

# `distplot` is a deprecated function and will be removed in seaborn v0.14.0.

# Please adapt your code to use either `displot` (a figure-level function with
# similar flexibility) or `histplot` (an axes-level function for histograms).

# For a guide to updating your code to use the new functions, please see
# https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

#   sns.distplot(student['writing score'])
# c:\VS Code\Python\智能统计学技术\5\1.py:34: UserWarning:

# `distplot` is a deprecated function and will be removed in seaborn v0.14.0.

# Please adapt your code to use either `displot` (a figure-level function with
# similar flexibility) or `histplot` (an axes-level function for histograms).

# For a guide to updating your code to use the new functions, please see
# https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751

#   sns.distplot(student['math score'], bins=10)

