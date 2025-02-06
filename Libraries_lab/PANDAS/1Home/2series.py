'''
A pandas series is like a column in a table
It is a one dimensional array holding data of any type

'''
import pandas as pd

a = [1,7,2]
myvar = pd.Series(a)
print(myvar)

#This label can be used to access a specified value.
print(myvar[0])

#Create Labels

myvar2 = pd.Series(a,index=['x', 'y', 'z'])
print(myvar2)
print(myvar2['x']) #accessing an  item by referring to a label

#key/value objects as series

#: The keys of the dictionary become the labels.
calories = {"day1":420, "day2":380, "day3":390}
myvar3 = pd.Series(calories)
print(myvar3)

#Create myvar = pd.Series(calories, index = ["day1", "day2"])

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)


#DATAFRAMES
'''
Data sets in Pandas are usually multi-dimensional tables,
 called DataFrames.
Series is like a column, a DataFrame is the whole table.
'''
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)