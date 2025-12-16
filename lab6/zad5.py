import pandas as pd


data = {
    "nr_albumu": [1, 2, 3, 4, 5],
    "imie": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "ocena": [4.5, 3.0, 5.0, 4.0, 2.5],
    "wiek": [22, 21, 24, 23, 25]
}


df = pd.DataFrame(data)
print("DataFrame bazowy:")
print(df, "\n")


df_ocena_wieksza_4 = df[df["ocena"] > 4]
print("a) Ocena > 4:")
print(df_ocena_wieksza_4, "\n")


df_sort_wiek = df.sort_values(by="wiek")
print("b) Posortowani wg wieku:")
print(df_sort_wiek, "\n")


sredni_wiek_wg_oceny = df.groupby("ocena")["wiek"].mean()
print("c) Średni wiek w grupach ocen:")
print(sredni_wiek_wg_oceny, "\n")


data_poprawa = {
    "nr_albumu": [2, 4],
    "ocena_poprawa": [4.0, 5.0]
}
df_poprawa = pd.DataFrame(data_poprawa)

df_polaczony = pd.merge(df, df_poprawa, on="nr_albumu", how="left")
print("d) Połączenie z ramką poprawy po nr_albumu:")
print(df_polaczony, "\n")


df.to_csv("studenci.csv", index=False)
print("e) Zapisano do pliku studenci.csv\n")


df_wczytany = pd.read_csv("studenci.csv")
print("f) Wczytany z CSV:")
print(df_wczytany, "\n")


nowy_student = {
    "nr_albumu": 6,
    "imie": "Piotr",
    "nazwisko": "Lewandowski",
    "ocena": 5.0,
    "wiek": 22
}
df = pd.concat([df, pd.DataFrame([nowy_student])], ignore_index=True)
print("g) Po dodaniu nowego studenta:")
print(df, "\n")


unikalne_oceny = df["ocena"].unique()
print("h) Unikalne oceny:")
print(unikalne_oceny, "\n")


liczba_ocena_5 = (df["ocena"] == 5.0).sum()
print("i) Liczba studentów z oceną 5:")
print(liczba_ocena_5)
