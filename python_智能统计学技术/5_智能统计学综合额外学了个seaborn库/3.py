import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib

# 读取本地 CSV 文件
file_path = r"C:\VS Code\Python\python_智能统计学技术\5_智能统计学综合额外学了个seaborn库\StudentsPerformance.csv"
StudentsPerformance = pd.read_csv(file_path)


# sns.relplot(
#     data=StudentsPerformance,
#     x="math score", y="reading score", col="writing score",
#     hue="smoker", style="smoker", size="size",
# )
# math = data['math score']
# reading = data['reading score']
# writing = data['writing score']
# matplotlib.pyplot.show()


# 使用 seaborn 进行绘图或其他操作
# 例如，绘制直方图
sns.histplot(StudentsPerformance['math score'])
plt.show()

