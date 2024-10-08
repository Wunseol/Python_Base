import regTrees
import numpy as np

# reload(regTrees)
# 在Python中，reload(module_name)函数用于重新导入已经导入过的模块。
# 这个函数主要在交互式编程环境（如IPython或Jupyter notebook）或开发过程中使用，
# 当您对已导入模块的源代码进行了修改并希望在当前会话中立即看到这些修改的效果时，可以调用reload来更新模块。
# 加载训练数据集
trainMat = regTrees.loadDataSet(r'C:\Users\coc\Desktop\数据挖掘实习\实验5\bikeSpeedVsIq_train.txt')
# 加载测试数据集
testMat = regTrees.loadDataSet(r'C:\Users\coc\Desktop\数据挖掘实习\实验5\bikeSpeedVsIq_test.txt')

# print(trainMat)
# print(testMat)
# trainMat= np.matrix(trainMat)
# testMat = np.matrix(testMat)
# trainMat = np.array(trainMat)
# testMat = np.array(testMat)
# print(trainMat)
# print(testMat)

# 使用训练数据创建决策树
myTree = regTrees.createTree(trainMat, ops=(1, 20))

# 对测试数据集进行预测
yHat = regTrees.createForeCast(myTree, testMat[:, 0])

# 计算预测值（yHat）与实际值（testMat[:, 1]）之间的相关系数
corr_coef = np.corrcoef(yHat, testMat[:, 1], rowvar=0)[0, 1]
print(corr_coef)

myTree = regTrees.createTree(trainMat, regTrees.modelLeaf, regTrees.modelErr, {1, 20})
yHat = regTrees.createForeCast(myTree, testMat[:, 0], regTrees.modelTreeEval)
corr_coef = np.corrcoef(yHat, testMat[:, 1], rowvar=0)[0, 1]
print(corr_coef)


