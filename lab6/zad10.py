import numpy as np

wagi_lista = [128, 64, 32, 16, 8, 4, 2, 1]
wagi = np.array(wagi_lista)

liczba_bin = np.random.randint(0, 2, 8)

def wartosc_liczby_bin(wagi, liczba_bin):
    return int(np.sum(wagi * liczba_bin))

print("wagi:      ", wagi)
print("liczba_bin:", liczba_bin)
print("wartość dziesiętna:", wartosc_liczby_bin(wagi, liczba_bin))
