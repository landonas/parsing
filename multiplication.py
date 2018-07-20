import numpy as np

A = np.arange(1,10).reshape(3,3)    # creating an array 1 - 10 and shaping it into a 3*3 matrix
B = np.arange(1,10).reshape(3,3)    # creating an array 1 - 10 and shaping it into a 3*3 matrix

m = np.dot(A,B)                     # multiplying both arrays 
print(m)                            # printing result
'''
RESULT:
[[ 30  36  42]
 [ 66  81  96]
 [102 126 150]]
'''