import math


a = math.sqrt(81)


b = pow(8, 10)


c = math.sqrt(2) + math.sqrt(3) + math.sqrt(6)


try:
    d = math.sqrt(-5)
except ValueError:
    d = "Błąd: pierwiastek z liczby ujemnej (brak w R)"


e = 3 * math.sqrt(125)

print("a) √81 =", a)
print("b) 8^10 =", b)
print("c) √2 + √3 + √6 =", c)
print("d) √(-5) =", d)
print("e) 3√125 =", e)