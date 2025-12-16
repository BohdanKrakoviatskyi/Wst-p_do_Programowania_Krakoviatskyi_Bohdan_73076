import numpy as np

tablica = np.zeros((3, 3), dtype=int)

tablica[0, 1] = 1
tablica[1, :] = 1
tablica[2, 0] = 1

print(tablica)
