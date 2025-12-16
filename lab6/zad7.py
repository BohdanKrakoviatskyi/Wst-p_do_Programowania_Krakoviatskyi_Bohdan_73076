import matplotlib.pyplot as plt

kategorie = ["Elektronika", "Odzież", "Jedzenie", "Zabawki", "Kosmetyki"]
sprzedane = [1200, 800, 1500, 600, 900]

plt.pie(sprzedane, labels=kategorie, autopct="%1.1f%%")
plt.title("Procentowy udział kategorii w całkowitej sprzedaży")
plt.show()
