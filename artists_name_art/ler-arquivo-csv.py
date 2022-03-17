import pandas as pd

f = pd.read_csv("z-artist-names.csv")

# 5 Primeiras linhas
print(f.head())

# 5 Ultimas linhas
print(f.tail())

# Informacões sobre o dataframe
print(f.info())