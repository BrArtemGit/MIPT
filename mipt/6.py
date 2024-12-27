import pandas as pd
df = pd.read_csv('population.csv')
df.Townspeople = round(df.Townspeople, 2)
df.Villagers = round(df.Villagers, 2)
df.Townspeople_pct = round(df.Townspeople_percent, 2)
df.Villagers_pct = round(df.Villagers_percent, 2)
df.Density = round(df.Density, 2)
# print(df)