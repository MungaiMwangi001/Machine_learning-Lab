#NumPy LCM Lowest Common Multiple

import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)
print(x)

#To find the Lowest Common Multiple of all values in an array,
#  you can use the reduce() method.

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)


#Find the LCM of all values of an array 
# where the array contains all integers from 1 to 10:
arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)