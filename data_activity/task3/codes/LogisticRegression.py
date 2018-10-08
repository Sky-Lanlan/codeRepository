import numpy as np
import urllib.request
from sklearn import preprocessing
from sklearn import metrics
from sklearn.linear_model import LogisticRegression


# url with dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/cmc/cmc.data"
# download the file
raw_data = urllib.request.urlopen(url)
# load the CSV file as a numpy matrix
dataset = np.loadtxt(raw_data, delimiter=',')
# separate the data from the target attributes
X = dataset[:, 1:-1]
y = dataset[:, -1]
# normalize the data attributes
normalized_X = preprocessing.normalize(X)

model = LogisticRegression()
# penalty(正则化选择参数)、solver（优化算法选择参数）、
# multi_class(分类方式选择参数)、class_weight(类型权重)
# model = LogisticRegression(penalty='l1',
#                            solver='liblinear', multi_class='ovr', class_weight={})
model.fit(normalized_X, y)
print(model)
# make predictions
expected = y
predicted = model.predict(normalized_X)
# summarize the fit of the model
print(metrics.precision_score(expected, predicted))
# print(metrics.confusion_matrix(expected, predicted))



