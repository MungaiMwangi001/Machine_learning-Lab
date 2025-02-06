#Exponential Distribution

'''
The exponential distribution is a continuous probability distribution that describes the time between events
 in a Poisson process (where events occur continuously and independently at a constant rate).

It is commonly used to model waiting times, such as:

The time between customer arrivals at a store.
The lifespan of a machine before it breaks down.
The time until the next earthquake occurs.

Exponential distribution is used for describing time till next event e.g. failure/success etc.

It has two parameters:

scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.

size - The shape of the returned array

'''

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.exponential(scale=2, size=(2,3))
sns.distplot(x, hist=False)
plt.show()

print(x)

'''
Relation Between Poisson and Exponential Distribution
Poisson distribution deals with number of occurences of an 
event in a time period whereas
 exponential distribution deals with the time between these events.
'''