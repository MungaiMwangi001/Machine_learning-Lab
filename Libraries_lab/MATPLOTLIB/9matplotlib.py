#With Pyplot, you can use the bar() function to draw bar graphs:import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)# takes arguments that describes the layout of the bars
plt.show()

#If you want the bars to be displayed horizontally instead of vertically, use the barh() function:


plt.barh(x, y , color='red')
plt.show()

# Bar Color
# The bar() and barh() take the keyword argument color to set the color of the bars

#you can used named colors or hexadecimal color values
