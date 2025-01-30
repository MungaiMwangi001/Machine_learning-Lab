'''
) is a continuous probability distribution that is symmetric around its mean. It follows the well-known bell curve shape.


Defined by Two Parameters – A normal distribution is fully described by:
 1.Mean (μ): Determines the center of the distribution.
2 .Standard deviation (σ): Controls the spread (wider for larger σ, narrower for smaller σ).





Use the random.normal() method to get a Normal Data Distribution.

It has three parameters:

loc - (Mean) where the peak of the bell exists.

scale - (Standard Deviation) how flat the graph distribution should be.

size - The shape of the returned array. 

'''


from numpy import random
y =  random.normal(size = 2,3)
x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)

# visualize

import seaborn as sb
import matplotlib.pyplt as plt

sns.distplot(random.normal(size=100),hist = false)
plt.show()


#normal vs binomial

''' 
The main difference is that normal distribution is continous whereas binomial is discrete, but if there are enough data points it will be quite 
similar to normal distribution with certain loc and scale.

'''
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()
