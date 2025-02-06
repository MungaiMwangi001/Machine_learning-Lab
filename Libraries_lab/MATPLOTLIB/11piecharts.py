'''Creating Pie Charts
With Pyplot, you can use the pie() function to draw pie charts:'''

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

#adding labels use :  labels parameter
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 

'''As you can see the pie chart draws one piece (called a wedge) for each value in the array (in this case [35, 25, 25, 15]).

By default the plotting of the first wedge starts from the x-axis and moves counterclockwise:

'''

# Start Angle
# As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.

# The startangle parameter is defined with an angle in degrees, default angle is 0:

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

# The explode parameter, if specified, and not None, must be an array with one value for each wedge.

# Each value represents how far from the center each wedge is displayed
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode, shadow= True)
#Add a shadow to the pie chart by setting the shadows parameter to True
plt.show() 


'''Colors
You can set the color of each wedge with the colors parameter.
works the same as previous examples using the hexadecimal
 color values(https://www.w3schools.com/colors/colors_hexadecimal.asp) or 
 colo-names(https://www.w3schools.com/colors/colors_names.asp)
'''
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show() 


'''Legend
To add a list of explanation for each wedge, use the legend() function:'''

plt.pie(y, labels = mylabels)
plt.legend( title = "Four Fruits:") #add a header
plt.show() 