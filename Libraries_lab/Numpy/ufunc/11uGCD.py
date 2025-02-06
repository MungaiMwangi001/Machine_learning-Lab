#NumPy GCD Greatest Common Denominator or 
# HCF (Highest Common Factor)

import numpy as np
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)

#To find the Highest Common Factor of
#  all values in an array, you can use the reduce() method.
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)