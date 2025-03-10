'''
Binomial Distribution is a Discrete Distribution.

It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.

It has three parameters:

n - number of trials.

p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).

size - The shape of the returned array.

Discrete Distribution:The distribution is defined at separate set of events, e.g. a coin toss's result is discrete as it can be only head or tails whereas height of people is continuous as it can be 170, 170.1, 170.11 and so on.

'''

from numpy import random

x = random.binomial( n=10, p=0.5, size=10)
print(x)

import  matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binoial(n=20, p=0.4,size=1000), hist= True, kde= False)

