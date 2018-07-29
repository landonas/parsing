import numpy as np
import pandas as pd

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

x = np.array([1 , 3, 6, 9])


t = np.zeros((5,5))                 #zeros functions returns matrix filled with zeros n*m


print(np.eye(3))                    #eye function retuns matrix as specified 

print(np.zeros((10,10)))            


newArray = np.array([[1,2,3], [4,5,6] , [7,8,9]])   #rank three array
print(newArray)

newArray = np.array([[1,2,3], [4,5,6] , [7,8,9], [10,11,12]]) #rank four array
print(newArray)