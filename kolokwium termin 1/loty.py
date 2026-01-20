def czas_lotu (odloty, przyloty):
    h1, m1 = [int(x) for x in odloty.split(':')] #rachuje odlot
    h2, m2 = [int(x) for x in przyloty.split(':')] #rachuje przylot

    start = h1 * 60 + m1
    end = h2 * 60 + m2

    if start > end: end += 1440

    diff = end - start
    return f"{diff//60:02d}:{diff%60:02d}"


print(f"czas lotu: {czas_lotu('13:34', '20:46')} godzin") #wypisuje czas

def koszt_biletu (cena, bagaz, koszt_bagazu):

    if bagaz.lower() == "tak":

        return cena + koszt_bagazu #rachuje cenu

    return cena

bagaz = input("Czy ma Pan/Pani bagaż? (tak/nie): ")
print(koszt_biletu(200, bagaz, 50))

def liczba_miejsc (suma_miejsc, zajete):#rachuje miejsca
    print("Suma miejsc:", suma_miejsc)
    print("Zajęte:", zajete)
    print("Wolne:", suma_miejsc - zajete)


liczba_miejsc(180, 120)