import numpy as np
from scipy import sparse

eye = np.eye(4)
print("Numpy array:\n{}".format(eye))

sparse_matrix = sparse.csr_matrix(eye)
print("SciPy CSR array:\n{}".format(sparse_matrix))

data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)

eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))

print("COO exp : \n{}".format(eye_coo))

#%matplotlib inline
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)

y = np.sin(x)

plt.plot(x, y, marker="x")
plt.show()


