x = float(input("Podaj wartość argumentu x: "))

if x > 0:
    a = 2 * x
elif x == 0:
    a = 0
else:
    a = -3 * x
print("a(x) =", a)

if x >= 1:
    b = x ** 2
else:
    b = x
print("b(x) =", b)

if x > 2:
    c = 2 + x
elif x == 2:
    c = 8
else:
    c = abs(x - 4)
print("c(x) =", c)
#