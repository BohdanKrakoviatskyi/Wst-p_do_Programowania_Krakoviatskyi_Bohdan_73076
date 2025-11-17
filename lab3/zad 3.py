tek = input("Podaj ciąg znaków: ")
czysty = tek.replace(" ", "").lower()

if czysty == czysty[::-1]:
    print("To jest palindrom.")
else:
    print("To nie jest palindrom.")