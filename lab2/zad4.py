n = int(input('Podaj liczbę ciangu (n):'))

element = 1

for i in range(1, n + 1):
    element *= i
print("Silnia =", element)