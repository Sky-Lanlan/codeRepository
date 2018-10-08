# coding=utf-8
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import urllib
from sklearn import metrics
import time
import pandas as pd
from sklearn.linear_model import LogisticRegression
# 通过url获取数据，并获得相应参数
# 返回数据集字典{dataset_name: {data:[],labelColumn:column,source=""}}


def load_data():
    format_data = {}
    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/zoo/zoo.data"
    # 下载文件
    raw_data = urllib.request.urlopen(url)
    # 格式化数据
    dataset = np.loadtxt(raw_data, delimiter=',', usecols=range(1, 18, 1))
    format_data['zoo数据集'] = {'data': dataset, 'labelColumn': 16, 'multiClass': True}

    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    raw_data = urllib.request.urlopen(url)
    df = pd.read_csv(raw_data, delimiter=',')
    dataset = np.array(df.replace(['Iris-setosa', 'Iris-virginica', 'Iris-versicolor'], [0, 1, 2]))
    format_data['iris数据集'] = {'data': dataset, 'labelColumn': 4, 'multiClass': True}

    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
    raw_data = urllib.request.urlopen(url)
    dataset = np.loadtxt(raw_data, delimiter=',')
    format_data['wine数据集'] = {'data': dataset, 'labelColumn': 0, 'multiClass': True}

    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00267/da" \
          "ta_banknote_authentication.txt"
    raw_data = urllib.request.urlopen(url)
    dataset = np.loadtxt(raw_data, delimiter=',')
    format_data['data_banknote_authentication数据集'] = {'data': dataset, 'labelColumn': 4
        , 'multiClass': False}

    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/blood-tr" \
          "ansfusion/transfusion.data"
    raw_data = urllib.request.urlopen(url)
    df = pd.read_csv(raw_data, delimiter=',', skiprows=1)
    format_data['transfusion数据集'] = {'data': np.array(df), 'labelColumn': 4, 'multiClass': False}

    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connec" \
          "tionist-bench/vowel/vowel-context.data"
    raw_data = urllib.request.urlopen(url)
    dataset = np.loadtxt(raw_data)
    format_data['vowel-context数据集'] = {'data': dataset, 'labelColumn': 13, 'multiClass': True}

    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/ecoli/ecoli.data"
    raw_data = urllib.request.urlopen(url)
    df = pd.read_csv(raw_data, delimiter='\s+', usecols=range(1, 9, 1))
    dataset = np.array(df.replace(['cp', 'im', 'pp', 'imU', 'om', 'omL', 'imL', 'imS'], range(0, 8, 1)))
    format_data['ecoli数据集'] = {'data': dataset, 'labelColumn': 7, 'multiClass': True}

    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/ionosphere/ionosphere.data"
    raw_data = urllib.request.urlopen(url)
    dataset = np.array(pd.read_csv(raw_data, delimiter=',').replace(['g', 'b'], [0, 1]))
    format_data['ionosphere数据集'] = {'data': dataset, 'labelColumn': 34, 'multiClass': False}
    return format_data


# 使用内置函数划分数据集
def deal_data(data, labelColum):
    y = data[:, labelColum]
    x = np.delete(data, labelColum, axis=1)
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.1)
    return train_x, train_y, test_x, test_y


def logistic_regression_clf(tr_x, tr_y):
    model = LogisticRegression()
    model.fit(tr_x, tr_y)
    return model


def tree_clf(tr_x, tr_y):
    model = DecisionTreeClassifier()
    model.fit(tr_x, tr_y)
    return model


def knn_clf(tr_x, tr_y):
    model = KNeighborsClassifier()
    model.fit(tr_x, tr_y)
    return model


def naive_bayes_clf(tr_x, tr_y):
    model = GaussianNB()
    model.fit(tr_x, tr_y)
    return model


def svm_clf(tr_x, tr_y):
    model = SVC()
    model.fit(tr_x, tr_y)
    return model


if __name__ == '__main__':
    clf_dic = {
        '逻辑回归': logistic_regression_clf,
        '决策树': tree_clf,
        'k邻近': knn_clf,
        '朴素贝叶斯': naive_bayes_clf,
        '支持向量机': svm_clf
    }
    data = load_data()

    for key in data:
        results = []
        train_x, train_y, test_x, test_y = deal_data(data[key]['data'], data[key]['labelColumn'])
        for key1 in clf_dic:
            result = [key1]
            start_time = time.time()
            model = clf_dic[key1](train_x, train_y)
            expected = test_y
            predicted = model.predict(test_x)
            ave = 'binary'
            if data[key]['multiClass']:
                ave = 'macro'
            acc = metrics.accuracy_score(expected, predicted)
            pre = metrics.precision_score(expected, predicted, average=ave)
            recall = metrics.recall_score(expected, predicted, average=ave)
            f1 = metrics.f1_score(expected, predicted, average=ave)
            use_time = time.time() - start_time
            result.append(use_time)
            result.append(pre)
            result.append(recall)
            result.append(acc)
            result.append(f1)
            results.append(result)
        print('==============', key, '===================')
        df = pd.DataFrame(results, columns=['分类算法', 'time', 'precision',
                                            'recall', 'acc', 'f1_score'])
        print(df)


