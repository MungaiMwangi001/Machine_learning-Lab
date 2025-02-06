#Rayleigh Distribution

'''

Rayleigh distribution is used in signal processing.

The Rayleigh distribution is a continuous probability distribution often used in engineering and physics to model the magnitude of a vector in 2D space, where each component is an independent normal variable with zero mean and equal variance.

It is commonly used for:

Modeling wind speeds.
Signal strength in wireless communication.
Noise levels in radar systems.

It has two parameters:

scale - (standard deviation) decides how flat the distribution will be default 1.0).

size - The shape of the returned array.
'''

from numpy import random

x = random.rayleigh(scale=2, size=(2, 3))

print(x)


import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()


'''
Similarity Between Rayleigh and Chi Square Distribution
At unit stddev and 2 degrees of freedom rayleigh
 and chi square represent the same distributions.
'''