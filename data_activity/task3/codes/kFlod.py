# 交叉验证评估，使用默认的k折交叉验证kFold

import numpy as np
import urllib.request
from sklearn import preprocessing



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

from sklearn.model_selection import _validation
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
score = _validation.cross_val_score(estimator=model, X=X, y=y, cv=10)
print(score)
