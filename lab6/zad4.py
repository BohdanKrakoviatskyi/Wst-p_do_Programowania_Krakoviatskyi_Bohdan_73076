import pandas as pd


data = {
    "id": [1, 2, 3, 4, 5],
    "imie": ["Anna", "Jan", "Katarzyna", "Tomasz", "Michał"],
    "nazwisko": ["Kowalska", "Nowak", "Wiśniewska", "Kaczmarek", "Zieliński"],
    "stanowisko": ["Manager", "Programista", "Konsultant", "Programista", "Manager"],
    "wiek": [35, 28, 40, 30, 45],
    "pensja": [8000, 4500, 6000, 5500, 7000]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df, "\n")


df_a = df[df["pensja"] > 5000]
print("a) pensja > 5000:\n", df_a, "\n")


df_b = df.sort_values(by="wiek")
print("b) posortowani po wieku:\n", df_b, "\n")


df_c = df.groupby("stanowisko")["pensja"].mean().reset_index()
print("c) średnia pensja wg stanowiska:\n", df_c, "\n")


awans = pd.DataFrame({
    "id": [2, 4],
    "nowe_stanowisko": ["Manager", "Senior Programista"]
})

df_d = df.merge(awans, on="id", how="left")
print("d) połączone z awansami:\n", df_d, "\n")


df.to_csv("pracownicy.csv", index=False)


df_loaded = pd.read_csv("pracownicy.csv")
print("f) wczytane dane:\n", df_loaded)
print("Czy dane identyczne:", df.equals(df_loaded))
