import trees
import treePlotter

fr = open("Python\数据挖掘实习\基础实验2\lenses.txt")
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age','prescript','astigmatic','tearrate']
lensesTree = trees.createTree(lenses, lensesLabels)
print(lensesTree)
print()
print("Done!")
print("20211113492 陈文聪 \n")
treePlotter.createPlot(lensesTree)

