
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from scipy.io import loadmat

# Importing the dataset
X = loadmat('flattenedinput.mat')
X = X['flat']
y = loadmat('noofsurebits.mat')
y = np.transpose(y['noofsurebits'])

#Random forest
from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=300,random_state=0)
regressor.fit(X,y)

# Fitting SVR to the dataset
"""from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y)"""

# Predicting a new result
y_pred = regressor.predict(X)

#mean square error
print(sklearn.metrics.mean_squared_error(y, y_pred))
