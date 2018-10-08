from sklearn.tree import DecisionTreeClassifier
import numpy as np
import urllib.request
from sklearn import preprocessing
from sklearn import metrics


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

# fit a CART model to the data
model = DecisionTreeClassifier()
# 设置参数criterion(最优划分属性衡量标准)、max_depth(树的最大深度)
# model = DecisionTreeClassifier(criterion="entropy", max_depth=20)
model.fit(X, y)
print(model)
# make predictions
expected = y
predicted = model.predict(X)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))
