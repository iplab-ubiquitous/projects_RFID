from sklearn import svm, neighbors, metrics, preprocessing
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, StratifiedShuffleSplit
from sklearn.metrics import classification_report, accuracy_score
from sklearn.externals import joblib
import pandas as pd
import numpy as np


dataset = pd.read_csv("test0930_bonsai.csv", header=None)
# data_train, data_test = train_test_split(dataset, test_size=0.2)
# train_label = data_train.iloc[:, 6]
# train_data = data_train.iloc[:, 0:6]

# test_label = data_test.iloc[:, 6]
# test_data = data_test.iloc[:, 0:6]

#データ分割
sss = StratifiedShuffleSplit(test_size=0.2)
data = dataset.iloc[:, 0:9]
label = dataset.iloc[:, 9]
for train_index, test_index in sss.split(data, label):
    train_data,  test_data  = data.loc[train_index], data.loc[test_index]
    train_label, test_label = label.loc[train_index], label.loc[test_index]


print(train_data)

# # クロスバリデーションで最適化したいパラメータをセット
# tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
#                      'C': [0.1, 1, 10]},
#                     {'kernel': ['linear'], 'C': [0.1, 1, 10]}]

# scores = ['precision', 'recall', 'f1']

# print("# Tuning hyper-parameters for accuracy")

#  # グリッドサーチと交差検証法
# # clf = GridSearchCV(svm.SVC(), tuned_parameters, cv=5,
# #                     scoring='accuracy', n_jobs=-1)
# # clf.fit(train_data, train_label)
# # print(clf.best_estimator_)
# # print(classification_report(test_label, clf.predict(test_data)))

# # joblib.dump(clf, 'test.pkl')

# # for score in scores:
# #     print("# Tuning hyper-parameters for {}".format(score))

# #     # グリッドサーチと交差検証法
# #     clf = GridSearchCV(svm.SVC(), tuned_parameters, cv=5,
# #                        scoring='%s_weighted' % score, n_jobs=-1)
# #     clf.fit(train_data, train_label)
# #     print(clf.best_estimator_)
# #     print(classification_report(test_label, clf.predict(test_data)))
    



# clf_svc = svm.SVC(C=0.1, kernel='linear')
# result = clf_svc.fit(train_data, train_label)
# pred = clf_svc.predict(test_data)
# # print(test_pred);
# print(classification_report(test_label, pred))
# print("正答率 = ", metrics.accuracy_score(test_label, pred))