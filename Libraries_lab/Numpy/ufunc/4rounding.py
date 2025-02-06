'''
There are primarily five ways of rounding off decimals in NumPy:

truncation
fix
rounding
floor
ceil

'''
#Truncation
#Remove the decimals, and return the float number closest to 
# zero. Use the trunc() and fix() functions.

import numpy as np

arr = np.trunc([-3.1666, 3.6667])
print(arr)

#fix
arr2 = np.fix([-3.1666, 3.6667])
print(arr2)

#Rounding
#The around() function increments
#preceding digit or decimal by 1 if >=5 else do nothing.

arr = np.around(3.1666, 2)
print(arr)


#The floor() function rounds off decimal to nearest lower integer.
arr = np.floor([-3.1666, 3.6667])
print(arr)


#arr = np.floor([-3.1666, 3.6667])
arr = np.floor([-3.1666, 3.6667])
print(arr)

#The ceil() function 
# rounds off decimal to nearest upper integer.
arr = np.ceil([-3.1666, 3.6667])

print(arr)