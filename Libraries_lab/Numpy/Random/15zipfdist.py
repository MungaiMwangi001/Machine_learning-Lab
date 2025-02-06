'''
Zipf distributions are used to sample data based on zipf's law.

Zipf's Law: In a collection, the nth common term is 1/n times of the most common term. E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.

It has two parameters:

a - distribution parameter.

size - The shape of the returned array.
'''


from numpy import random

x = random.zipf(a=2, size=(2, 3))

print(x)

#visualization

import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()


''''
The Zipf distribution is a discrete probability distribution that follows Zipf's Law, which states that a few items occur very frequently, while many items occur rarely. It is commonly used in linguistics, internet traffic, and economics.

Example:

In language, the most common word (e.g., "the") appears much more than the second most common word, which appears much more than the third, and so on.

In website traffic, a few websites get most of the visits (e.g., Google, YouTube), while most sites have very few visitors.
'''