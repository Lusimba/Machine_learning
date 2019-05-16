import pandas as pd
iris = pd.read_csv(open(r'C:\Users\User\Anaconda3\Lib\site-packages\sklearn\datasets\data\iris.csv','rb'))
#Read by row x column
print(iris[['150','4','setosa','versicolor']]) 

#read 1 column
print(iris[['virginica']])
