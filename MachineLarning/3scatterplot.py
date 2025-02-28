#A scatter plot is a diagram where each value in the data set is represented by a dot.

# The x array represents the age of each car.

# The y array represents the speed of each car.

 #two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis:
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()


#Random Data Distributions
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()


# We can see that the dots are concentrated around the value 5 on the x-axis, and 10 on the y-axis.

# We can also see that the spread is wider on the y-axis than on the x-axis.