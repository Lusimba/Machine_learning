#%%
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
data = load_iris()

knn = KNeighborsClassifier(n_neighbors=1)
X_train, X_test, y_train, y_test = train_test_split(data['data'],data['target'], random_state = 0)

knn.fit(X_train, y_train)
X_new = np.array([[1,2,5,0.2]])

print("X New shape: {}".format(X_new.shape))
pred = knn.predict(X_new)
print("Prediction: {}".format(pred))
print("Predicted target Names: {}".format(data['target_names'][pred]))

y_pred = knn.predict(X_test)
print("Test set predictions:\n {}".format(y_pred))
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))