
#Logs
'''
NumPy provides functions to perform log at the base 2, e and 10.

We will also explore how we can take log for any base by creating a custom ufunc.

All of the log functions will place -inf or inf in the elements if the log can not be computed.
'''

import numpy as np

arr = np.arange(1, 10) #arange -from numpy library ,output type - ndarray, supports float(the step), uses more memory than range(python libary)
#Use range() when working with loops and integer sequences. Use numpy.arange() for numerical computations, 
# especially when floating-point steps are required


#Log at Base 2
print(np.log2(arr))
#Log at Base 10
print(np.log10(arr))
#Natural Log, or Log at Base e
print(np.log(arr))



#Log at Any Base
'''
NumPy does not provide any function to take log at any base, 
so we can use the frompyfunc() function along with inbuilt 
function math.log() with two input parameters and one output
 parameter:

Example
'''

from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
