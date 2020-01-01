import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel('data.xlsx')
df_csv = pd.read_csv('data.csv',header=None)
df_txt = pd.read_csv('data.txt',header=None, delimiter='\t')
df_txt.columns = ['fname','lname','age']
print(df_txt)