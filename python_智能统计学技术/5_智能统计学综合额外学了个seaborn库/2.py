import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv(r"C:\VS Code\Python\python_智能统计学技术\5_智能统计学综合额外学了个seaborn库\StudentsPerformance.csv")
data.head()
print(data)
# data.split(" ")

student = data.drop(['race/ethnicity', 'parental level of education'], axis=1)

student.head()

print(student)

# # 加载数据
# fp = np.load('Python\智能统计学技术\\2\\国民经济核算季度数据.npz', allow_pickle=True)

for k in data:
    print(k)

# 获取保存的数组
math = data['math score']
reading = data['reading score']
writing = data['writing score']

print('columns :\n', math)
print('values :\n', reading)
print('values :\n', writing)

sns.distplot(math)

# 创建画布
# fig = plt.figure(figsize=(8,8))  # 返回画布对象
# fig = plt.figure(figsiez=(50,50),dpi=80)
# 默认不支持中文，需要进行修改，修改完后，不支持符号
plt.rcParams['font.sans-serif'] = 'SimHei'
# 增加字体之后变得不支持符号，需要吸怪RC参数让其他继续支持符号
plt.rcParams['axes.unicode_minus'] = False
# 设置子图间距
plt.subplots_adjust(hspace=0.5)
# wspace = None， 子图之间的宽度间距 ------设置为（0,1]小数 ---子图宽度占比



# plt.figure(figsize=(10, 10))

# # plt.scatter(math[:, 0], math[:, 1], marker='o')  # 画散点图

# plt.xlabel('fen')
# plt.ylabel('fen')
# plt.ylim((0, 100))
# plt.xlim((0, 100))
# # plt.xticks(range(0, 70, 4), math[range(0, 70, 4), 1], rotation=45)  # 此时取得值都是第一季度的
# plt.title('2000-2017年季度生产总值散点图')
# plt.savefig('./2000-2017年季度生产总值散点图.png')  # 图片要先保存再显示
plt.show()  # 在当前设备显示图片


