
'''
A distribution following Pareto's law i.e.

 80-20 distribution (20% factors cause 80% outcome).

 a small percentage of the population holds the majority of the resources (e.g., wealth distribution, city populations).

It is named after the economist Vilfredo Pareto, who observed that 80% of Italy’s land was owned by 20% of the people.


It has two parameter:

a - shape parameter.

size - The shape of the returned array.
'''

from numpy import random

x = random.pareto(a=2, size=(2, 3))

print(x)

# visualization

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=2, size=1000), kde=False)

plt.show()