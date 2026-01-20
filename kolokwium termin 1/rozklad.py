# 1. Czas lotu 9:00 -> 13:30
def czas_lotu(odloty, przyloty):

    h1, m1 = [int(x) for x in odloty.split(':')]
    h2, m2 = [int(x) for x in przyloty.split(':')]

    start = h1 * 60 + m1

    end = h2 * 60 + m2

    if start > end: end += 1440

    diff = end - start

    return f"{diff//60:02d}:{diff%60:02d}"

czas = czas_lotu("09:00", "13:30")
print(f"1. Czas lotu: {czas}")  # 04:30

# 2. Koszt biletu 200zł + bagaż 50zł
def koszt_biletu(cena, bagaz, koszt_bagazu):

    if bagaz.lower() == "tak":

        return cena + koszt_bagazu

    return cena

koszt = koszt_biletu(200, "tak", 50)
print(f"2. Koszt biletu z bagażem: {koszt} zł")  # 250 zł

# 3. Wolne miejsca: 180 - 150
def liczba_miejsc(suma, zajete):
    wolne = suma - zajete

    print(f"3. Suma miejsc: {suma}")
    print(f"   Zajęte: {zajete}")
    print(f"   Wolne: {wolne}")

    return wolne

liczba_miejsc(180, 150)  # 30 wolnych
