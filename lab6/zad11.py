import numpy as np

macierz = np.random.rand(5, 5)

najwiekszy = np.max(macierz)
najmniejszy = np.min(macierz)

max_wiersze = np.max(macierz, axis=1)
max_kolumny = np.max(macierz, axis=0)

suma_wiersze = np.sum(macierz, axis=1)

print("macierz:\n", macierz)
print("największy:", najwiekszy)
print("najmniejszy:", najmniejszy)
print("max w wierszach:", max_wiersze)
print("max w kolumnach:", max_kolumny)
print("suma wierszy:", suma_wiersze)
