'''
Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
Distplots
Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to
 the distribution of points in the array.
'''

import numpy as np
import seaborn as sns

#plotting a distplot

sns.distplot([0, 1, 2, 3, 4, 5]) # hist = false , sets it without a histogram
 sns.distplt([0,1,2,3,4,5], hist = false)
plt.show()