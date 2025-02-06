#Simple Arithmetic
'''
You could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally.

Arithmetic Conditionally: means that we can define conditions where the arithmetic operation should happen.

All of the discussed arithmetic functions take a where parameter in which we can specify that condion'''

import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

#The add() function sums the content of two arrays, and return the results in a new array.
newarr = np.add(arr1, arr2)
print(newarr)


#The subtract() function subtracts the values from one array with the values
#  from another array, and return the results in a new array.
newarr2 = np.subtract(arr1, arr2)
print(arr2)

# multiply() function multiplies the values from one array with the values from another array,
# # and return the results in a new array
newarr3 = np.multiply(arr1, arr2)
print(newarr3)

#divide() function divides the values from one array with the values
#  from another array, and return the results in a new array.
newarr4 = np.divide(arr1, arr2)
print(newarr4)


#power() function rises the values from the first array to the power of the values
#of the second array, and return the results in a new array.
newarr5 = np.power(arr1, arr2)
print(newarr5)


# same result when using the remainder() function
newarr = np.remainder(arr1, arr2)
print(newarr)

#The divmod() function return both the quotient and the mod. 
# The return value is two arrays, the first array contains the quotient and second array contains the mod.
newarr6 = np.divmod(arr1, arr2)
print(newarr6)

#Both the absolute() and the abs() functions do the same
#absolute operation element-wise but we should use absolute() to avoid confusion with python's inbuilt math.abs()

arr2 = np.array([-1,-2,1,2,3,-4])
newarr7 = np.absolute(arr2)
print(newarr7)