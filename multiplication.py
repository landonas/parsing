import numpy as np

A = np.arange(1,10).reshape(3,3)
B = np.arange(1,10).reshape(3,3)
print(A)
print(B)

m = np.dot(A,B)
print(m)
