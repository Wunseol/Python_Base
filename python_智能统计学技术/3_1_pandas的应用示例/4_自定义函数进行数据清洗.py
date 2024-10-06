# 导入pandas库，用于数据处理和分析
import pandas as pd
# 导入numpy库，用于数值计算
import numpy as np

# """
# 数据去重和缺失值中位数填补函数
# 参数:
#     - data (pandas.DataFrame): 需要进行数据清洗的数据集
# 返回:
#     - cleaned_data (pandas.DataFrame): 清洗后的数据集
# """

def data_cleaning(data):

    # 去重
    cleaned_data = data.drop_duplicates()

    # 缺失值中位数填补
    median_values = cleaned_data.median()
    cleaned_data.fillna(median_values, inplace=True)

    return cleaned_data

# 示例数据
data = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, np.nan, 30, 40, np.nan],
    'C': [1.1, 2.2, 3.3, np.nan, 5.5]
})

print("原始数据：")
print(data)

# 调用自定义函数进行数据清洗
cleaned_data = data_cleaning(data)

print("清洗后的数据：")
print(cleaned_data)


# 该函数实现以下功能：

# 接受一个Pandas DataFrame data 作为输入。
# 去除数据中的重复行。
# 使用每列的中位数填充缺失值（NaN）。
# 返回处理后的清洗数据。



