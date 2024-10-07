import numpy as np
from naiveBayes import naiveBayes

f = open(r'C:\Users\coc\Desktop\Pattern_Recognition\navie_bayes\watermelon.csv',encoding='utf-8')
raw_datas = f.read()
# print(raw_datas)
f.close()
datas = [[]]
for data in raw_datas.split('\n'):
    datas.append(data.split(','))
attr_name = ['⾊泽', '根蒂', '敲声', '纹理', '脐部', '触感', '密度', '含糖量', 'label']
datas[0] = attr_name
datas = np.array(datas)
# print("test datas:")
# print(datas)
test_X = np.array([['浅⽩','蜷缩','浊响','模糊','平坦','软粘','0.343','0.099'],
['青绿','蜷缩','浊响','清晰','凹陷','硬滑','0.697','0.460']])
# 指定属性类型
attr_type = [1, 1, 1, 1, 1, 1, 0, 0]
# 查表式拟合预测
nbClassfier = naiveBayes()
# print("111111111111111111",nbClassfier)
# print("------------------------------------------------------------1")
nbClassfier.fit(datas, attr_type)
# print("1111111111111111",nbClassfier)
# print("------------------------------------------------------------2")
predict_y = nbClassfier.predict(test_X, L=True, N=2)
# print("------------------------------------------------------------3")
print(predict_y)
# print("------------------------------------------------------------")
# 懒惰学习
lazy_predict_y = nbClassfier.lazy_predict(datas, test_X, attr_type, True, N=2)
# print("------------------------------------------------------------")
print(lazy_predict_y)
# print("------------------------------------------------------------")