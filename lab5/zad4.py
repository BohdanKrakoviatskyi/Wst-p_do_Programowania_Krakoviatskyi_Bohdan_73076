from datetime import datetime, date


laboratoria = date(2025, 11, 20)


kolokwium = date(2025, 12, 19)


dzis = date.today()


dni_od_laboratoriow = (dzis - laboratoria).days
dni_do_kolokwium = (kolokwium - dzis).days


laboratoria_str = laboratoria.strftime("%d %B %Y")
kolokwium_str = kolokwium.strftime("%d %B %Y")
dzis_str = dzis.strftime("%d %B %Y")


print("Dzisiejsza data:", dzis_str)
print("Ostatnie laboratoria:", laboratoria_str)
print("Minęło dni od laboratoriów:", dni_od_laboratoriow)
print("Kolokwium:", kolokwium_str)
print("Pozostało dni do kolokwium:", dni_do_kolokwium)