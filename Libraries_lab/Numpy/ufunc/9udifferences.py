#Numpy differences

'''
A discrete difference means subtracting two successive elements.

E.g. for [1, 2, 3, 4], the discrete difference would
 be [2-1, 3-2, 4-3] = [1, 1, 1]

To find the discrete difference, use the diff() function
'''
import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr)

#We can perform this operation repeatedly by giving parameter n.

newarr = np.diff(arr, n=2) #performs the diffrence 2 times
print(newarr)