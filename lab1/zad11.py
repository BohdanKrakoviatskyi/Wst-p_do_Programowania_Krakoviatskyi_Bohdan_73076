a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

delta = b**2 - 4*a*c

if a == 0:
    if b != 0:
        x = -c / b
        print("Równanie liniowe, rozwiązanie: x =", x)
    else:
        print("Brak rozwiązań.")
else:
    if delta > 0:
        x1 = (-b + (delta)**0.5) / (2*a)
        x2 = (-b - (delta)**0.5) / (2*a)
        print("Dwa pierwiastki rzeczywiste:", x1, "oraz", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Jeden pierwiastek rzeczywisty:", x)
    else:
        print("Brak pierwiastków rzeczywistych.")
