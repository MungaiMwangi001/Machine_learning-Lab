
#the DataFrame is like a table with rows and columns.
import pandas as pd

a  = {
    "calories": [420,380, 390],
    "duration":[50,40,45]
}

myvar = pd.DataFrame(a)
print(myvar)

#Locate Row
#andas use the loc attribute to return one or more 
# specified row(s)

print(myvar.loc[0]) # returns a Pandas Series.

print(myvar.loc[[0, 1]]) #When using [], the result is a Pandas DataFrame.

#Named Indexes - With the index argument,
#  you can name your own indexes.
df = pd.DataFrame(a, index = ["day1", "day2", "day3"])

print(df) 

#refer to the named index:
print(df.loc["day2"])

#load files into dataframe


df = pd.read_csv('data.csv')#Load a comma separated file (CSV file) into a DataFrame

print(df) 