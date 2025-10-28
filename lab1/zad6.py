a = float(input("Podaj długość drogi :"))
b = float(input("Ile samochód mają średnie spalamje (w litrach na 100km):"))
cena = 6.5
zuzycie = a*(b/100)
print(f"{zuzycie} litrów")
print(f"{zuzycie*cena} zł")
#f