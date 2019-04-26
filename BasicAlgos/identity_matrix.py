#%%
import numpy as np
from scipy import sparse

x = np.eye(4)
print("A 4x4 identity matrix is as below \n {}".format (x))

data = np.ones(4)
data_col = np.arange(4)
data_row = np.arange(4)
eye_coord= sparse.coo_matrix(data, (data_row, data_col))
print ("An eye coordinate matrix looks like\n {}".format(eye_coord))