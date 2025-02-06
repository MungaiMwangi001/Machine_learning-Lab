
'''
Empty Cells
Empty cells can potentially give you a wrong result when 
you analyze data.
Remove Rows
One way to deal with empty cells is to
 remove rows that contain empty cells.
This is usually OK, since data sets can be very big, 
and removing a few rows will not have a big impact on
 the result.
'''

import pandas as pd
df = pd.read_csv('data.csv')
#new_df = df.dropna()
#By default, the dropna() method returns a new DataFrame, 
# and will not change the original

#print(new_df.to_string())

# to change the original DataFrame, 
# use the inplace = True argument:

#df.dropna(inplace = True)

#print(df.to_string())

'''
#Notice in the result that some rows have been
#  removed (row 18, 22 and 28).
#These rows had cells with empty values.
'''

#Replace Empty Values
'''
Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value:
'''
df.fillna(130, inplace=True)
print(df.to_string())
#Notice in the result: 
# empty cells got the value 130 (in row 18, 22 and 28).

#replace null values for a specified column
df['Calories'].fillna(130,inplace=True)
print(df)

#This operation inserts 130 in empty cells in the "Calories"
#  column (row 18 and 28).


#Replace Using Mean, Median, or Mode
'''
A common way to replace empty cells, is to calculate the
 mean, median or mode value of the column.
Pandas uses the mean() median() and mode() 
methods to calculate the respective values for
 a specified column:
'''
x = df['Calories'].mean()#the average value (the sum of all values divided by number of values).
df['Calories'].fillna(x,inplace=True)

y = df['Calories'].median()# the value in the middle, after you have sorted all values ascending.
df['Calories'].fillna(y,inplace=True)

z = df['Calories'].mode()#the value that appears most frequently
df['Calories'].fillna(z,inplace=True)