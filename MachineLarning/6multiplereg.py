'''
Multiple regression is like linear regression, but with more than one independent value, meaning that we try to predict a value based on two or more variables.

Examples:
We can predict the CO2 emission of a car based on the size of the engine, but with multiple regression we can throw in more variables, like the weight of the car, to make the prediction more accurate.

'''

import pandas
from sklearn import linear_model

#read csv files and return a DataFrame object.
df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]#list of indepedent values, in variable x
y = df['CO2']#depedant values in a variable y

regr = linear_model.LinearRegression() #create a linear regression object.
regr.fit(X, y)# takes the independent and dependent values as parameters and fills the 
#regression object with data that describes
#  the relationship

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)

#We have predicted that a car with 1.3 liter engine,
#  and a weight of 2300 kg, will release approximately 
# 107 grams of CO2 for every kilometer it drives.


'''
Coefficient
The coefficient is a factor that describes the relationship with an unknown variable.

Example: if x is a variable, then 2x is x two times. 
x is the unknown variable, and the number 2 is the
 coefficient.
'''
# we can ask for the coefficient value of weight against CO2,
# and for volume against CO2.
print(regr.coef_)
#The result array represents the coefficient values of weight and volume.
'''
These values tell us that if the weight increase by 1kg, the CO2 emission increases by 0.00755095g.

And if the engine size (Volume) increases by 1cm3, the CO2 emission increases by 0.00780526g.

lets test this out:
change weight to 3300kg
'''
predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)

'''
We have predicted that a car with 1.3 liter engine, and a weight of 3300 kg, will release approximately 115 grams of CO2 for every kilometer it drives.

Which shows that the coefficient of 0.00755095 is correct:

107.2087328 + (1000 * 0.00755095) = 114.75968
'''