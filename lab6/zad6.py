import matplotlib.pyplot as plt


kategorie = ["Elektronika", "Odzież", "Jedzenie", "Zabawki", "Kosmetyki"]
sprzedane = [120, 80, 150, 60, 90]

plt.bar(kategorie, sprzedane)
plt.title("Ilość sprzedanych produktów w różnych kategoriach")
plt.xlabel("Kategoria")
plt.ylabel("Liczba sprzedanych produktów")
plt.show()
