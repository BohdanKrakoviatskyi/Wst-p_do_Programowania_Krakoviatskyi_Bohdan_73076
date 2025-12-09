def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)
    print("twoje BMI:", bmi)
    if bmi < 18.5:
        print("niedowaga")
    elif bmi < 25:
        print("waga prawidłowa")
    elif bmi < 30:
        print("nadwaga")
    else:
        print("otyłość")

waga = float(input("podaj wagę (kg): "))
wzrost = float(input("podaj wzrost (m): "))

oblicz_bmi(waga, wzrost)