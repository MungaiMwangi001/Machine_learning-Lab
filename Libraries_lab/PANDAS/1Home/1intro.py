
'''
Pandas is a Python library.
Pandas is used to analyze data.
The name "Pandas" has a reference to both "Panel Data",
 and "Python Data Analysis" and was created by Wes McKinney
   in 2008.

Why Use Pandas?
Pandas allows us to analyze big data and make conclusions based on statistical theories.

Pandas can clean messy data sets, and make them readable and relevant.

Relevant data is very important in data science.


'''
#how to import pandas
import pandas as pd

#pandas in use
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

#version of pandas
print(pd.__version__)