#Products

'''
To find the product of the elements in an array, 
use the prod() function.
'''

import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)
print(x)

#Find the product of the elements of two arrays:
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x)

#If you specify axis=1, NumPy will return the product of each array.

newarr = np.prod([arr1, arr2], axis=1)
print(newarr)

#Cummulative Product
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)