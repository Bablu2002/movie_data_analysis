
import pandas as pd

df = pd.read_csv("C:/Users/ADMIN/Desktop/python/roadmap_practice/week-4/Data_analysis/data/IMDB-Movie-Data.csv")

"""rename columns for clarity"""

df.rename(columns={
    'Runtime (Minutes)' : 'Runtime',
    'Revenue (Millions)': 'Revenue',
    'Metascore': 'Metascore'
}, inplace= True)

"""fill missing data"""

df['Revenue'] = df['Revenue'].fillna(df['Revenue'].median())
df['Metascore'] = df['Metascore'].fillna(df['Metascore'].median())

"""confirm cleaned data"""
print('\n Cleaned Data Info:')
print(df.info())
print('\n Any missing values left?')
print(df.isnull().sum())