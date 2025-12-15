import random
import math


a = float(input("Podaj dolną granicę przedziału: "))
b = float(input("Podaj górną granicę przedziału: "))


krotka = tuple(random.uniform(a, b) for _ in range(10))

print("Wylosowana krotka:")
print(krotka)


iloczyn = 1
for x in krotka:
    iloczyn *= x

srednia_geometryczna = iloczyn ** (1 / len(krotka))

print("Średnia geometryczna:", srednia_geometryczna)