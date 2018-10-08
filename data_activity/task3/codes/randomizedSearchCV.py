
from scipy.stats import uniform as sp_rand
from sklearn.linear_model import Ridge
from sklearn.grid_search import RandomizedSearchCV

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

# prepare a uniform distribution to sample for the alpha parameter
param_grid = {'alpha': sp_rand()}
# create and fit a ridge regression model, testing random alpha values
model = Ridge()
rsearch = RandomizedSearchCV(estimator=model, param_distributions=param_grid, n_iter=100)
rsearch.fit(X, y)
print(rsearch)
# summarize the results of the random parameter search
print(rsearch.best_score_)
print(rsearch.best_estimator_.alpha)
