import numpy as np

macierz = np.zeros((5, 5), dtype=int)

macierz[0, :] = 1
macierz[-1, :] = 1
macierz[:, 0] = 1
macierz[:, -1] = 1

def zamien_0_1(a):
    return 1 - a

print(macierz)
print(zamien_0_1(macierz))
