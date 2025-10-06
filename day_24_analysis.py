
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

"""top 10 highest rated movies"""
top10 = df.sort_values(by='Rating', ascending=False).head(10)
print("\n Top 10 highest rated movies: ")
print(top10[['Title', 'Rating', 'Revenue']])


"""plot rating vs revenue for top 10"""
plt.figure(figsize=(10,6))
sns.scatterplot(data=top10, x='Rating', y = 'Revenue', hue='Title', s = 100)

for i in range(top10.shape[0]):
    plt.text(x=top10['Rating'].iloc[i]+0.01,
             y=top10['Revenue'].iloc[i]+1,
             s=top10['Title'].iloc[i],
             fontsize =8)
plt.title("Revenue vs IMDB Rating (Top 10 Movies)")
plt.xlabel("IMDB Rating")
plt.ylabel("Revenue (Millions USD)")
plt.tight_layout()
plt.legend(bbox_to_anchor=(1.05, 1), loc = 'upper left')
plt.show()

"""top 5 directors by movie count"""
top_directores = df['Director'].value_counts().head(5)
print("\n Top 5 directors with most movies:")
print(top_directores)

"""movies released by year"""
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='Year', palette='mako')
plt.title("Movies release per year")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

"""heatmap for correlation numeric col"""
plt.figure(figsize=(8,6))
sns.heatmap(df[['Rating', 'Votes', 'Revenue', 'Metascore']].corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Between Rating, Revenue, Votes, Metascore")
plt.tight_layout()
plt.show()

"""🎭 Genre frequency analysis"""
genre_list = df['Genre'].str.split(',').explode().str.strip()
top_genres = genre_list.value_counts().head(10)

plt.figure(figsize=(8, 5))
sns.barplot(x=top_genres.values, y=top_genres.index, palette='viridis')
plt.title("Top 10 Genres by Number of Movies")
plt.xlabel("Number of Movies")
plt.tight_layout()
plt.show()