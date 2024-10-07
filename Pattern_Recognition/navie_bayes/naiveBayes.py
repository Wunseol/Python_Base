import numpy as np
class naiveBayes():
    """
    ⼀个朴素贝叶斯分类器
    attrs -- 存放属性的字典, 字典中，键为属性名，值为属性的取值，最后⼀个属性为标签属性
    attr_idx -- 属性列索引号
    my_dic -- 存放每个标签的样本数
    mxiy_dic -- 存放每个标签的条件下，每个属性的某个属性值所含的样本数
    m -- 训练样本总数量
    attr_type -- 属性类型列表，1表⽰离散属性，0表⽰连续属性
    """
    def __init__(self):
        self.attrs = None
        self.attr_idx = None
        self.my_dic = None
        self.mxiy_dic = None
        self.m = None
        self.attr_type = None
    def get_attrs(self, data, attr_type):
        """
        对数据集进⾏处理，得到属性与对应的属性取值
        args:
        data -- 输⼊的数据矩阵, shape=(samples+1, features+1), dtype='<U?', 其中，第⼀⾏为属性，最后⼀列为标签
        attr_type -- 属性离散或连续的标记列表，1为离散，0为连续
        returns:
        attrs -- 存放属性的字典, 字典中，键为属性名，值为属性的取值
        """
        attrs = {}
        attr_type.append(1)
        for i in range(data.shape[1]):
            if attr_type[i] == 1:
                attrs_values = sorted(set(data[1:, i]))
            else:
                attrs_values = []
            attrs[data[0][i]] = attrs_values
        self.attrs = attrs
    def fit(self, data, attr_type):
        """
        拟合数据，获得查询表
        args:
        data -- 输⼊的数据矩阵, shape=(samples+1, features+1), dtype='<U?', 其中，第⼀⾏为属性，最后⼀列为标签
        attr_type -- 属性离散或连续的标记列表，1为离散，0为连续
        """
        self.attr_type = attr_type
        self.get_attrs(data, attr_type)
        X = data[1:, :-1]
        y = data[1:, -1]
        # 先创建⼀个不含label属性的纯变量属性字典
        pure_attrs = self.attrs.copy()
        del(pure_attrs['label'])
        # 构造⼀个只含属性名的列表
        attr_names = [attr_name for attr_name in pure_attrs.keys()]
        # 将属性名编号，⽅便查找其在数据中对应的列
        attr_idx = {}
        for num, attr in enumerate(attr_names):
            attr_idx[attr] = num
        self.attr_idx = attr_idx
        self.create_search_dic(X, y, attr_type)
        
    def create_search_dic(self, X, y, attr_type):
        """
        创建查询字典
        args:
        X -- 训练集数据，shape=(samples, features)
        y -- 训练集标签，shape=(samples, )
        attr_type -- 属性离散或连续的标记列表，1为离散，0为连续
        """
        my_dic = {}
        mxiy_dic = {}
        m = np.size(y)
        self.m = m
        # 获取每个标签的样本数
        for label in self.attrs['label']:
            n = np.sum(y == label)
            my_dic[label] = n
        # 获取每个标签的条件下，每个属性的某个属性值的数量(离散)或每个属性的⽅差和均值(连续)
        for label in self.attrs['label']:
            mxiy_dic[label] = {}
            for attr in self.attrs:
                if attr != 'label':
                    mxiy_dic[label][attr] = {}
                    attr_line = X[:, self.attr_idx[attr]]
                    if attr_type[self.attr_idx[attr]] == 1:
                        for attr_value in self.attrs[attr]:
                            mxiy_dic[label][attr][attr_value] = np.sum(attr_line[np.where(y==label)] == attr_value)
                    else:
                        sample = attr_line[np.where(y==label)].astype('float')
                        var = np.var(sample, ddof=1)
                        mean = np.mean(sample)
                        mxiy_dic[label][attr] = [var, mean]
        self.my_dic = my_dic
        self.mxiy_dic = mxiy_dic
    def predict(self, X, L=True, **kwargs):
        """
        预测数据
        args:
        X -- 预测数据的属性值，shape=(samples, features)
        L -- 是否使⽤拉普拉斯修正
        N -- 若使⽤拉普拉斯修正，给出可能类别数
        returns:
        y -- 预测结果
        """
        y = []
        if L:
            N = kwargs['N']
            up = 1
        else:
            N = 0
            up = 0
        for i in range(np.size(X, 0)):
            label = None
            P = -1
            # 计算每个标签的概率P(yi)
            for yi in self.attrs['label']:
                myi = self.my_dic[yi]
                pyi = (myi + up) / (self.m + N)
                Pi = pyi
                # 计算P(xi|yi)
                for j in range(np.size(X, 1)):
                    attr_value = X[i, j]
                    # 获取该列对应的属性名
                    attr_name = [k for k, v in self.attr_idx.items() if v==j][0]
                    # 离散值
                    if self.attr_type[j] == 1:
                        # 属性值在训练集中出现
                        if attr_value in self.attrs[attr_name]:
                            pxiy = (self.mxiy_dic[yi][attr_name][attr_value] + up) / (myi + N)
                        # 属性值在训练集中没出现
                        else:
                            pxiy = up / N
                    # 连续值
                    else:
                        var = self.mxiy_dic[yi][attr_name][0]
                        mean = self.mxiy_dic[yi][attr_name][1]
                        pxiy = 1 / np.sqrt(2*np.pi*var) * np.exp(-(float(attr_value)-mean)**2 / (2*var))
                    Pi *= pxiy
                if Pi > P:
                    P = Pi
                    label = yi
            y.append(label)
        return np.array(y)
    def lazy_predict(self, train_data, predict_X, attr_type, L, **kwargs):
        """
        懒惰学习预测
        args:
        train_data -- 输⼊的训练集数据矩阵, shape=(samples+1, features+1), dtype='<U?', 其中，第⼀⾏为属性，最后⼀列为标签
        predict_X -- 要预测的测试集数据, shape=(samples, features)
        attr_type -- 属性离散或连续的标记列表，1为离散，0为连续
        L -- 是否使⽤拉普拉斯修正
        N -- 若使⽤拉普拉斯修正，给出可能类别数
        returns:
        y -- 预测结果
        """
        attr_name = train_data[0, :-1]
        X = train_data[1:, :-1]
        y = train_data[1:, -1]
        y_value = sorted(set(y))
        predict_y = []
        if L:
            N = kwargs['N']
            up = 1
        else:
            N = 0
            up = 0
        for i in range(np.size(predict_X, 0)):
            label = None
            P = -1
            # 每个标签取值的概率
            for yi in y_value:
                myi = np.sum(y==yi)
                pyi = (myi + up) / (np.size(y) + N)
                pyi = (myi + up) / (np.size(y) + N)
                Pi = pyi
                for j in range(np.size(X, 1)):
                    attr_value = predict_X[i, j]
                    # 离散属性
                    if attr_type[j] == 1:
                        mxi = np.sum(X[np.where(y==yi), j] == attr_value)
                        pxiy = (mxi + up) / (myi + N)
                    # 连续属性
                    else:
                        mean = np.mean(X[np.where(y==yi), j].astype('float'))
                        var = np.var(X[np.where(y==yi), j].astype('float'), ddof=1)
                        pxiy = 1 / np.sqrt(2*np.pi*var) * np.exp(-(float(attr_value)-mean)**2 / (2*var))
                    Pi *= pxiy
                if Pi > P:
                    P = Pi
                    label = yi
            predict_y.append(label)
        return np.array(predict_y)
if __name__ == "__main__":
    pass
