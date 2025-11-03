#zadanie domowe!a
import random

srednie_spalanie = float(input("Podaj średnie spalanie samochodu (l/100 km): "))

dlugosc_podrozy = random.randint(50, 500)

zuzycie_paliwa = (srednie_spalanie / 100) * dlugosc_podrozy

koszt = zuzycie_paliwa * 6.5

# Wyświetl wyniki
print(f"Długość podróży: {dlugosc_podrozy} km")
print(f"Przewidywane zużycie paliwa: {zuzycie_paliwa:.2f} l")
print(f"Szacowany koszt podróży: {koszt:.2f} zł")
