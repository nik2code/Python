import pandas as pd
from openpyxl.workbook import Workbook

df = pd.read_csv('data.csv',header=None)
df.columns = ['fname','lname','age']

#showing one column
print(df['fname'])
print()
#showing multiple columns
print(df[['fname','age']])
print()
print(df['fname'][0:1])
print()
#show specific row
print(df.iloc[0])
print()
print(df.iloc[1])
print()
#get row-column value
print(df.iloc[1,0])
print(df.iloc[1,2])
print()
#Extract specific values and export it in another workbook
wanted_values = df[['fname','age']]
stored = wanted_values.to_excel('exported.xlsx',index=None)