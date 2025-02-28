import pandas as pd

a = {"gluc":[1,2,3,1,2],
     "alco":[3,2,1,3,1]
     }

df = pd.DataFrame(a)
print(df.melt())

