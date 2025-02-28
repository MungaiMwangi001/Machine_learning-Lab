# The term regression is used when you try to find the relationship between variables.

# In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.


# Linear regression uses the relationship between the data-points to draw a straight line through all them.

# This line can be used to predict future values.

#Import scipy and draw the line of Linear Regression:

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]


#Execute a method that returns some important key values of Linear Regression:
slope, intercept, r, p, std_err = stats.linregress(x, y)

# function that uses the slope and intercept values to 
# return a new value. This new value represents where on 
# the y-axis the corresponding x value will be placed:
def myfunc(x):
  return slope * x + intercept


#Run each value of the x array through the function. This will 
# result in a new array with new values for the y-axis:
mymodel = list(map(myfunc, x)) 

plt.scatter(x, y)
#Draw the line of linear regression:
plt.plot(x, mymodel)

plt.show()

print(r)
''''
linear regeression is based on relationships
the coeffiecient of correlation - is called r
r ranges between -1 to 1 where o means no
 relationship 1 and -1 means 100%related
 scipy automatically fins this for us
 just fee in the x and  y values

'''

#now with the above we can make a Predictionof the  the speed of a 10 years old car:

speed = myfunc(10)

print(speed) #example predicted a speed at 85.6, 

#what is a bad fit
#it essentially means that linear regression is not fit for the given data to make predictions
#Example

import matplotlib.pyplot as plt
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

print(r)
'''The result: 0.013 indicates a very bad relationship,
 and tells us that this data set is not suitable for 
 linear regression.'''
