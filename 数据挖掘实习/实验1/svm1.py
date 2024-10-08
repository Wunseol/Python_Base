# 支持向量机

import h5py
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import numpy as np

# 加载数据
with h5py.File(r'B:\数据挖掘实习\综合实验1\train.hdf5', 'r') as train_file:
    X_train = train_file['X_train'][:]
    y_train = train_file['y_train'][:].reshape(-1)

with h5py.File(r'B:\数据挖掘实习\综合实验1\test.hdf5', 'r') as test_file:
    X_test = test_file['X_test'][:]
    y_test = test_file['y_test'][:].reshape(-1)


# 修改数据预处理部分
X_train = X_train.reshape(-1, X_train.shape[-2] * X_train.shape[-1])  # 展平最后一个两个维度
X_test = X_test.reshape(-1, X_test.shape[-2] * X_test.shape[-1])  # 展平最后一个两个维度

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# 构建SVM模型
svm_classifier = svm.SVC()

# 使用网格搜索调整SVM参数（可选，根据实际情况调整参数范围）
param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf'], 'gamma': ['scale', 'auto']}
grid_search = GridSearchCV(svm_classifier, param_grid, cv=5, scoring='accuracy', verbose=2)
grid_search.fit(X_train, y_train)

best_svm_classifier = grid_search.best_estimator_
print("Best SVM parameters:", grid_search.best_params_)

# 训练模型
best_svm_classifier.fit(X_train, y_train)

# 预测
y_pred = best_svm_classifier.predict(X_test)

# 计算评价指标
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
y_prob = best_svm_classifier.decision_function(X_test)
auc = roc_auc_score(y_test, y_prob)

print(f"Accuracy: {acc:.3f}")
print(f"Precision: {prec:.3f}")
print(f"Recall: {rec:.3f}")
print(f"AUC: {auc:.3f}")

# 绘制ROC曲线
fpr, tpr, _ = roc_curve(y_test, y_prob)
plt.plot(fpr, tpr, label='SVM')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.show()
