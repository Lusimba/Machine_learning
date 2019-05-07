#%%
# import keyboard
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# f = open("E:\Downloads\Iris.xlsx")
# f.readline()  # skip the header
#iris_dataset = np.loadtxt('E:\Downloads\Iris.xlsx', delimiter=',')

# input_file = "E:\Downloads\Iris.csv"
iris_dataset = pd.read_csv('E:\Downloads\Iris.csv', sep=',', header = 0, encoding='ascii', engine='python')

knn = KNeighborsClassifier(n_neighbors=1)
X_train, X_test, y_train, y_test=train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
knn.fit(X_train, y_train)
X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape: {}".format(X_new.shape))
prediction = knn.predict(X_new)
print("Prediction: {}".format(prediction))
print("Predicted target name: {}".format(
iris_dataset['target_names'][prediction]))
y_pred = knn.predict(X_test)
print("Test set predictions:\n {}".format(y_pred))
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))
# keyboard.wait("esc")