'''
If your data points clearly will not fit a linear regression (a straight line through all data points), it might be ideal for polynomial regression.

Polynomial regression, like linear regression, uses the relationship between the variables x and y to find the best way to draw a line through the data points.
'''

import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]


#method that lets us make a polynomial model:
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

#pecify how the line will display, we start at position 1,
#  and end at position 22
myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)

#Draw the line of polynomial regression:
plt.plot(myline, mymodel(myline))

plt.show()



'''
R-SQUARED
if there are no relationship the polynomial regression can not be used to predict anything.
The relationship is measured with a value called the r-squared
 r-squared value ranges from 0 to 1, where 0 means no relationship, and 1 means 100% related.

'''
import numpy 
from sklearn.metrics import r2_score


x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y , 3))
print(r2_score(y, mymodel(x)))

'''
Note: The result 0.94 shows that there is a very 
good relationship, and we can use polynomial regression 
in future prediction
'''


speed = mymodel(17)
print(speed)


'''
BADFIT

- This is where where polynomial regression would not be the best method to predict future values.

- The result: 0.00995 indicates a very bad relationship, and tells us that this data set is not suitable for polynomial regression.
'''

import numpy
from sklearn.metrics import r2_score

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))