def pole_trapezu(a, b, h):
    pole = (a + b) * h / 2
    print(pole)

a = float(input("Podaj bok a: "))
b = float(input("Podaj bok b: "))
h = float(input("Podaj wysokość h: "))

pole_trapezu(a, b, h)