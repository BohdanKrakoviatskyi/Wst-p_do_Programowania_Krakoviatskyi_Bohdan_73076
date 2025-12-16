import pandas as pd


dane = {
    "KRAJ": ["Polska", "Niemcy", "Czechy", "Ukraina"],
    2019: [30_000, 90_000, 20_000, 150_000],
    2020: [40_000, 80_000, 25_000, 160_000],
    2021: [45_000, 100_000, 27_000, 170_000],
    2022: [50_000, 120_000, 30_000, 200_000]
}

df = pd.DataFrame(dane)


max_w_kolumnach = df.drop(columns=["KRAJ"]).max()


rok_max = max_w_kolumnach.idxmax()


wiersz_max = df[rok_max].idxmax()


kraj_max = df.loc[wiersz_max, "KRAJ"]
najwiekszy_przyrost = df.loc[wiersz_max, rok_max]

print("Rok:", rok_max)
print("Kraj:", kraj_max)
print("Największy przyrost:", najwiekszy_przyrost)
