import matplotlib.pyplot as plt

import numpy as np

#Plotting x and y points
xpoints = np.array([1,8])
ypoints = np.array([3,10])

# The plot() function is used to draw points (markers) in a diagram.
# By default, the plot() function draws a line from point to point.
# The function takes parameters for specifying points in the diagram.
plt.plot(xpoints, ypoints)
plt.show()

# Plotting Without Line
# To plot only the markers, you can use shortcut string 
# notation parameter 'o', which means 'rings'.
plt.plot(xpoints, ypoints, 'o')
plt.show()

#Multiple Points
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

# Default X-Points
# If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()