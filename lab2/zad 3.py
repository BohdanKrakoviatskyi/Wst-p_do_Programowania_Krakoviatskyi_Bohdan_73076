n = int(input("Podaj liczbę elementów (n): "))
a = float(input("Podaj pierwszy wyraz (a): "))
r = float(input("Podaj różnicę (r): "))

for i in range(n):
    element = a + i * r
    print(element)