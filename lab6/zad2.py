import pandas as pd

dane = {
    "kraj": ["Polska", "Niemcy", "Czechy", "Ukraina"],
    "przyrost_2022": [50_000, 120_000, 30_000, 200_000]
}

df = pd.DataFrame(dane)
df = df.set_index("kraj")

print(df)

kraj_max = df["przyrost_2022"].idxmax()       # domyślnie skipna=True
print(kraj_max)
