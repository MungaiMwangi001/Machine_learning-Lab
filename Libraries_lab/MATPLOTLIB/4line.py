'''Linestyle
You can use the keyword argument linestyle, or shorter ls,
 to change the style of the plotted line:'''

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted') # dashed/--, solid(default)/-, dashdot/-., none/or
plt.show()

'''Line Color
You can use the keyword argument color or the shorter c 
to set the color of the line:'''

plt.plot(ypoints, color = 'r') 
plt.show()

# we can also use  the hexadecimal colors
plt.plot(ypoints, c = '#4CAF50')
plt.show()

#or the 140 supported color names
...
plt.plot(ypoints, c = 'hotpink')
...

# Line Width
# You can use the keyword argument linewidth or the 
# shorter lw to change the width of the line.
# The value is a floating number, in points:


plt.plot(ypoints, linewidth = '20.5')
plt.show()

'''Multiple Lines
You can plot as many lines as you like by simply
 adding more plt.plot() functions:'''

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

'''You can also plot many lines by adding the points
 for the x- and y-axis for each line in the same plt.plot() function.'''

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()