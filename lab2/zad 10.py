a = int(input("Podaj pierwszą liczbę całkowitą: "))
b = int(input("Podaj drugą liczbę całkowitą: "))

mniej = min(a, b)
wieksz = max(a, b)

for i in range(mniej, wieksz + 1):
    print(i)