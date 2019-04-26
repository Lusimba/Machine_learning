#%%
import pandas as pd

data ={'Name': ["John", "Anna", "Peter", "Linda"],
    'Location':["New York", "Paris", "Berlin","London"],
    'Age':[23, 54, 8, 27]
    }
data_pandas = pd.DataFrame(data)
display(data_pandas)
#Displaying a filtered list by age
display(data_pandas[data_pandas.Age>30])
