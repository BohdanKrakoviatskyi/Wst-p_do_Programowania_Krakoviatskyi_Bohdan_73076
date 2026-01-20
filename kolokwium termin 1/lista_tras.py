#to jest list lotów
flights = [
    (130, '05:45', '06:40'), (150, '12:00', '12:55'), (160, '14:40', '15:30'),
    (550, '15:00', '17:35'), (600, '09:00', '11:45'), (650, '18:00', '20:30'),
    (200, '06:55', '08:10'), (250, '14:00', '15:15'), (220, '19:00', '20:15')
]
#to racuje wszystko

czasy = []
for cena, dep, arr in flights:
    dh, dm = map(int, dep.split(':'))
    ah, am = map(int, arr.split(':'))
    diff = (ah*60 + am) - (dh*60 + dm)
    czasy.append(diff)
    print(f"{dep}-{arr}: {diff//60}h{diff%60}m {cena}zł")

#oblicza średnie
srednia = sum(czasy)/9
print(f"\nŚrednia: {srednia//60}h{srednia%60}m")
