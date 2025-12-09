def pokaz_dane(imie, wiek=20):
    #Funkcja wypisuje na ekran imię oraz wiek użytkownika.
    print("Imię:", imie)
    print("Wiek:", wiek)

print(pokaz_dane.__doc__)

pokaz_dane("Bohdan", 22)
pokaz_dane("Anna")