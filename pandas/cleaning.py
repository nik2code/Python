import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

df = pd.read_csv('data.csv',header=None)
df.columns = ['fname','lname','age']

#df.drop(columns='lname',inplace=True)

df = df.set_index('age')

print(df.loc[30])
print()
print(df.iloc[0])
print()
print(df.iloc[1])
print()
print(df.loc[30: ,'lname'])
print()
print(df.fname.str.split(expand=True))
df.fname = df.fname + '^'
print(df)


