import numpy as np
from scipy import sparse
data  = np.ones(4)
row_i = np.arange(4)
col_i = np.arange(4)
eye_c = sparse.coo_matrix(data, (row_i, col_i))
print(eye_c)

import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
y = np.sin(x)
plt.plot(x, y, marker="x")

import pandas as pd
clients = {
    'Name':["Lucy","John","Anna","Peter"],
    'City':["Nairobi", "Mombasa", "Malindi", "Berlin"],
    'Age': [34, 12, 45, 56]
}
p_data = pd.DataFrame(clients)
display(p_data[p_data.Age>30])


