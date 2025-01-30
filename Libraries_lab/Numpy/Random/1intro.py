from numpy import random
import numpy as np

b = np.random.rand() # floats 0 -1
a = np.random.randint(10,20,size=(3,2)) #Intergers
x=np.random.randint(100,200, size=(5))
c =  np.random.choice([3, 5, 7, 9]) #choose a random numbr from an existing array
d= np.random.choice ([1,2,3,4,5], size=(3,5)) # 2d array
print(x)
# Generate a random float between 100 and 200
random_float = np.random.uniform(100, 200)


# Generate 5 random floats between 100 and 200
random_floats = np.random.uniform(100, 200, size=5)