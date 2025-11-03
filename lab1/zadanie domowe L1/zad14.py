nazwa_pliku = input("Podaj nazwę pliku: ")

if nazwa_pliku.endswith('.xls') or nazwa_pliku.endswith('.xlsx'):
    print("To jest plik arkusza Excel.")
else:
    print("To NIE jest plik arkusza Excel.")
#