import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# 第三题

# 第(1)问
mtcars = pd.read_csv(r'C:\VS Code\Python\python_智能统计学技术\3_1_pandas的应用示例\mtcars.csv')
print('mtcars的维度为:',mtcars.ndim)
print('mtcars的大小为:',mtcars.shape)

# 第(2)问
print('mtcars的描述性统计为:',mtcars.describe())

# 第(3)问
data = mtcars.loc[:,['cyl','carb','mpg','hp']]
mpgHp = data.groupby(['cyl','carb']).mean()
print('不同cyl(汽缸数),carb(化油器)对应的mpg(油耗)和hp(马力)的均值为：',mpgHp)

# 第四题

def mode_and_median(train):
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    # list5=[]
    # list6=[]
    # list7=[]
    # list8=[]
    # list9=[]
    # list10=[]
    # list11=[]
    # list12=[]
    for col in train.columns:#对每一列数据进行循环
        # print(col)
        dir = train[col].drop_duplicates()#单独列数据进行去重，大于10个的直接跳过
        if dir.size>30:
#             print("列{}为数值型数据,中位数为{}".format(col,dir.median()))
            list1.append(col)
            list2.append(dir.median())
 
        if dir.size<10:#对去重后数据进行保存，储存则数据在整一列数据中对数据进行匹配
            # print(dir)
            c = Counter()
            for ch in train[col]:
                c[ch] = c[ch] + 1
            list3.append(col)
            list4.append(c.most_common(1))
#             print("列{}为类别型数据,众数值为{}".format(col,c.most_common(1)))
    df1 = pd.DataFrame([list1,list2],index = ["列名", "中位数"])
    df2 = pd.DataFrame([list3,list4],index = ["列名", "众数"])
    df3 = pd.concat([df1,df2])
    return df3.T

# mode_and_median(train)

# #查看当前数据的缺失值
# total = all_data.isnull().sum().sort_values(ascending = False)
# percent = (all_data.isnull().sum()/all_data.isnull().count()).sort_values(ascending = False)
# missing_data = pd.concat([total,percent],axis = 1,keys = ['Total','Percent'])
# missing_data.head(30)

# features['Electrical'] = features['Electrical'].fillna("SBrkr")#类别型
# features['GarageArea'] = features['GarageArea'].fillna("548")#数值型

