import pandas as pd

df = pd.read_csv('data.csv',header=None)
df.columns =  ['fname','lname','age']

#print all records 
print(df)
print()
#print all record whose lname match with 'Shelke'
print(df.loc[df['lname'] == 'Shelke'])
print()
#use multiple condition to get filter records
print(df.loc[(df['lname'] == 'kumar') | (df['lname'] == 'Kumar')])
print()
#insert new columns with value based on the condition of the row
df['decades'] = df['age'].apply(lambda x: '20s' if 20 <= x < 30 else '30s' if 30 <= x < 40 else 'others')
print(df)
#add new columns with mathematical calculation with the other rows 
df['age -5'] = df['age'] - 5
print(df['age -5'])
#can drop columns from data frame 
to_drop = ['fname','lname']
df.drop(columns=to_drop,inplace=True)
print(df)
print()

#check condition and set value of a specific row-column
df['Test Col'] = False
df.loc[df['age'] < 30 , 'Test Col' ] = True
print(df)
print()
#grouping ... you can add math function with the columns
print(df.groupby(['age']))

#sorting
print(df.sort_values('age'))
print()
print(df.sort_values('decades'))
