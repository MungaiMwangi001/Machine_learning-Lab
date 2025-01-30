#A permutation refers to an arrangement of elements
# -shuffle() and permutation()

from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)
print(arr)
#The shuffle() method makes changes to the original array.

arr = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))

#The permutation() method returns a re-arranged 
#array (and leaves the original array un-changed).