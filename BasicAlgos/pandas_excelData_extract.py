#%%
import pandas as pd

#Extracting files from an excel file. 
data = pd.read_excel(open('E:\Downloads\February2014.xls', 'rb'), sheet_name='SOCIOECONOMIC')
data_pandas = pd.DataFrame(data)
display(data_pandas)