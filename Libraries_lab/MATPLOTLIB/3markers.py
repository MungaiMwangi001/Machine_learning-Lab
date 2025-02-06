# Markers
# You can use the keyword argument marker to emphasize
#  each point with a specified marker:

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

'''there are a variety of markers check them out on 
https://www.w3schools.com/python/matplotlib_markers.asp '''


# Format Strings fmt
# You can also use the shortcut string notation parameter to specify the marker.

# This parameter is also called fmt, and is written with this syntax:

# marker|line|color




plt.plot(ypoints, 'o:r') # circle marker, dotted line, red
plt.show()

# - solid line  : dotted --dashed line -. dashed/dotted line
# r -red, g -green , b -blue, c- cyan , m - magenta, y - yellow, k - black, w -white


'''Marker Size
You can use the keyword argument markersize or 
the shorter version, ms to set the size of the markers:'''

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

'''
Marker Color
You can use the keyword argument markeredgecolor or the
 shorter mec to set the color of the edge of the markers:'''

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

'''You can use the keyword argument markerfacecolor or the
 shorter mfc to set the color inside the edge of the markers:'''

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()