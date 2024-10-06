import pandas as pd

# (1)使用ndim，shape等属性分别查看数据表的维度、大小等信息.

# 修改解码方式为UTF-16LE：
# df = pd.read_csv("C:\VS Code\Python\智能统计学技术\\3\Training_Master.csv",sep="|",encoding="utf-16LE",header=None,na_values='null',dtype=str)  

data = pd.read_csv(r"C:\VS Code\Python\python_智能统计学技术\3_1_pandas的应用示例\Training_Master.csv",encoding="ISO-8859-1")
 
# print(data)#输出数据以查看是否导入成功.
 
# 这个sb编码搞了好久

# data = data.decode('ISO-8859-1','ignore'),encoding="ISO-8859-1"
# data = data.decode(encoding='UTF-8','ignore')
 
#查看主表信息的维度
print("Training_Master主表信息的维度为:",data.ndim)
#查看主表信息的大小
print("Training_Master主表信息的大小为:",data.shape)
#查看出表信息的占用内存信息

# print("Training_Master主表信息的占用内存信息是:\n",data.memory_usage())

# (2)使用describe方法进行描述性统计,并剔除值相同或全为空的列.

#使用describe方法进行描述性统计
a_describe = data.describe()
print("使用describe方法进行描述性统计:\n",a_describe)
print("-------------分割线------------")
#剔除值相同或全为空的列

# 剔除数据前
# print(data)

##定义剔除方法
bef = data.shape
print("剔除数据前主表的形状：",bef)
def Del_The_Same_And_Null(data):
    The_Null=data.describe().loc["count"]==0
    for i in range(0,len(The_Null)):
        if The_Null[i]:
            data.drop(labels=The_Null.index[i],axis=1,inplace=True)
    THe_Std=data.describe().loc["std"]==0
    for j in range(0,len(THe_Std)):
        if THe_Std[j]:
            data.drop(labels=THe_Std.index[j],axis=1,inplace=True)
    fin = data.shape
    print("剔除数据后主表的形状：",fin)
#执行剔除方法

Del_The_Same_And_Null(data)

# 剔除数据后
# print(data)

