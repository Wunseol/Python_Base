# -*- coding: UTF-8 -*-
from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines

import matplotlib.pyplot as plt
import time

import numpy as np
import operator

def classify0(inX, dataSet, labels,k):

    dataSetSize=dataSet.shape[0]
    diffMat=np.tile(inX, (dataSetSize, 1))-dataSet

    sqDiffMat=diffMat**2

    sqDistances=sqDiffMat.sum(axis=1)

    distances=sqDistances**0.5

    sortedDistIndicies=distances.argsort()
    classCount={}

    for i in range(k):

        voteIlabel=labels[sortedDistIndicies[i]]

        classCount[voteIlabel]=classCount.get(voteIlabel, 0)+1
        sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def file2matrix(filename):

    fr=open(filename)

    arrayOlines= fr.readlines()

    numberOfLines=len(arrayOlines)
    returnMat = np.zeros((numberOfLines,3))
    classLabelVector=[]
    index=0
    for line in arrayOlines:
        line=line.strip()
        listFromLine=line.split('\t')
        returnMat[index,:]=listFromLine[0:3]

        if listFromLine[-1]=='didntLike':
            classLabelVector.append(1)
        elif listFromLine[-1]=='smallDoses':
            classLabelVector.append(2)
        elif listFromLine[-1]=='largeDoses':
            classLabelVector.append(3)
        index+=1
    return returnMat, classLabelVector
def showdatas(datingDataMat, datingLabels):

    font=FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc",size=14)
    fig,axs=plt.subplots(nrows=2,ncols=2, sharex=False, sharey=False, figsize=(13,8))
    LabelsColors=[]
    for i in datingLabels:
        if i==1:
            LabelsColors.append('black')
        if i==2:
            LabelsColors.append('orange')
        if i==3:
            LabelsColors.append('red')
    axs[0][0].scatter(x=datingDataMat[:,0],y=datingDataMat[:,1],
    color=LabelsColors,s=15,alpha=.5)
    axs0_title_text=axs[0][0].set_title(u'每年获得的飞行常客里程数与玩视频游戏 所消耗时间百分比',FontProperties=font)
    axs0_xlabel_text=axs[0][0].set_xlabel(u'每年获得的飞行常客里程数', FontProperties=font)
    axs0_ylabel_text=axs[0][0].set_ylabel(u'玩视频游戏所消耗时间百分比', FontProperties=font)


    plt.setp(axs0_title_text, size=9, weight='bold', color='red')
    plt.setp(axs0_xlabel_text, size=7, weight='bold',color='black')
    plt.setp(axs0_ylabel_text,size=7, weight='bold',color='black')
    axs[0][1].scatter (x=datingDataMat[:,0],y=datingDataMat[:,2],color=LabelsColors,s=15,alpha=.5)
    axsl_title_text=axs[0][1].set＿title(u'每年获得的飞行常客里程数与每周消费的 冰淇淋升???',FontProperties=font)
    axsl_xlabel_text=axs[0][1].set＿xlabel(u'每年获得的飞行常客里程数',FontProperties=font)
    axsl_ylabel_text=axs[0][1].set＿ylabel(u'每周消费的冰淇淋升数',FontProperties=font)
    plt.setp(axsl_title_text, size=9,weight='bold',color='red')
    plt.setp(axsl_xlabel_text, size=7, weight='bold', color='black')
    plt.setp(axsl_ylabel_text,size=7,weight='bold', color='black')
    axs[1] [0].scatter (x=datingDataMat[:,1],y=datingDataMat [:,2],color= LabelsColors,s=15,alpha=.5)
    axs2_title_text=axs[1][0].set_title(u'玩视频游戏所消耗时间百分比与每周消费的冰淇淋升???',FontProperties=font)
    axs2_xlabel_text=axs[1][0].set_xlabel(u'玩视频游戏所消耗时间百分比',FontProperties=font)
    axs2_ylabel_text=axs[1][0].set_ylabel(u'每周消费的冰淇淋升数',FontProperties=font)
    plt.setp(axs2_title_text, size=9,weight='bold', color='red')
    plt.setp(axs2_xlabel_text, size=7, weight='bold', color='black')
    plt.setp(axs2_ylabel_text, size=7, weight='bold',color='black')
    didntLike=mlines.Line2D([], [],color='black', marker='.',markersize=6, label='didntLike')
    smallDoses =mlines.Line2D([],[],color='orange', marker='.', markersize=6, label='smallDoses')
    largeDoses = mlines.Line2D([], [], color='red', marker=',', markersize=6, label='largeDoses')

    axs[0][0].legend(handles=[didntLike, smallDoses, largeDoses])
    axs[0][1].legend(handles=[didntLike,smallDoses,largeDoses])
    axs[1][0].legend(handles=[didntLike, smallDoses, largeDoses])
    plt.show()
def autoNorm(dataSet):

    minVals=dataSet.min(0)
    maxVals= dataSet.max(0)
    ranges=maxVals-minVals

    normDataSet=np.zeros(np.shape(dataSet))
    m=dataSet.shape[0]
    normDataset=dataSet-np.tile(minVals,(m,1))
    normDataSet=normDataset/np.tile(ranges,(m,1))
    return normDataSet, ranges, minVals
def datingClassTest():

    filename=r"C:\VS Code\Pattern_Recognition\KNN\datingTestSet.txt"
    datingDataMat, datingLabels=file2matrix(filename)
    hoRatio=0.10
    normMat,ranges,minVals=autoNorm(datingDataMat)
    m=normMat.shape[0]
    numTestVecs=int(m*hoRatio)
    errorCount=0.0
    for i in range(numTestVecs):
        classifierResult=classify0(normMat[i,:],normMat[numTestVecs:m,:],\
        datingLabels[numTestVecs:m],4)
        print("分类结果???%d\t真实类别:%d"%(classifierResult,datingLabels[i]))
        if classifierResult!=datingLabels[i]:
            errorCount+=1.0
    print("错误率：%f%%"%(errorCount/float(numTestVecs)*100))
def classifyPerson():
    resultList=['讨厌','有些喜欢','非常喜欢']


    ffMiles=float(input("玩视频游戏所消耗时间百分比:"))
    percentTats=float(input("每年获得的飞行常客里程数:"))

    # percentTats=float(input("玩视频游戏所消耗时间百分比:"))
    # ffMiles=float(input("每年获得的飞行常客里程数:"))
    iceCream=float(input("每周消费的冰淇淋升数:"))
    filename=r"C:\VS Code\Pattern_Recognition\KNN\datingTestSet.txt"
    datingDataMat,datingLabels =file2matrix(filename)
    normMat, ranges, minVals=autoNorm(datingDataMat)
    inArr = np.array([percentTats, ffMiles, iceCream])
    norminArr=(inArr-minVals) /ranges
    classifierResult= classify0(norminArr, normMat,datingLabels,4)
    print("你可???%s这个???"%(resultList[classifierResult-1]))
def main():
    start=time.perf_counter()
    filename=r"C:\VS Code\Pattern_Recognition\KNN\datingTestSet.txt"
    datingDataMat,datingLabels = file2matrix(filename)
    normDataset, ranges,minVals= autoNorm(datingDataMat)
    datingClassTest()

    classifyPerson()
    end=time.perf_counter()

    print('Running time:%f seconds'%(end-start))

if __name__ == '__main__':
    main()




