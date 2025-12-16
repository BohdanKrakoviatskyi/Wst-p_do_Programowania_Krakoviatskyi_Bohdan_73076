import numpy as np

macierz = np.random.randint(0, 50, size=(5, 5))

wieksze_20 = macierz[macierz > 20]
liczba_wiekszych_20 = wieksze_20.size

srednia = np.mean(macierz)

print("macierz:\n", macierz)
print("elementy > 20:", wieksze_20)
print("liczba elementów > 20:", liczba_wiekszych_20)
print("średnia całej tablicy:", srednia)
