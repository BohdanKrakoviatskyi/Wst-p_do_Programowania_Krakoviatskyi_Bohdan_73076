imie = input("Podaj imię: ")
wiek = input("Podaj wiek: ")
nazwisko = input("Podaj nazwisko: ")
tekst = input("Podaj łańcuch: ")
a = input("Podaj pierwszy łańcuch: ")
b = input("Podaj drugi łańcuch: ")
inicjaly = imie[0] + nazwisko[0]
pol_a = len(a) // 2
pol_b = len(b) // 2
polaczone = a + b
nowy_lancuch = a[:pol_a] + b[pol_b:]
print("Witaj", imie)
print("Twój wiek to:", wiek)
print("Inicjały:", inicjaly)
print("Łańcuch wypisany 5 razy:")
for i in range(5):
    print(tekst)
print("Połączony łańcuch:", polaczone)
print("Nowy łańcuch:", nowy_lancuch)