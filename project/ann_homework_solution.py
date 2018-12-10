# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from scipy.io import loadmat

X = loadmat('flattenedinput.mat')
X = X['flat']
y = loadmat('noofsurebits.mat')
y = np.transpose(y['noofsurebits'])


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train,y_train=X,y

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor


# Initialising the ANN

classifier = Sequential()
# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'normal', activation = 'relu', input_dim = 48000))

# Adding the second hidden layer
classifier.add(Dense(units = 6, kernel_initializer = 'normal', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'normal', activation = 'relu'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)

# Part 3 - Making predictions and evaluating the model

# Predicting the Test set results
y_pred = classifier.predict(X_train)

#mean square error
print(sklearn.metrics.mean_squared_error(y, y_pred))