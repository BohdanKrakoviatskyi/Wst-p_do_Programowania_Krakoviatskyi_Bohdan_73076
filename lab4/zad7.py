import math

def pole_trojkata(a, b, c):
    try:
        if a + b <= c or a + c <= b or b + c <= a:
            print("Z podanych boków nie można zbudować trójkąta.")
            return

        s = (a + b + c) / 2
        pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Pole trójkąta:", pole)

    except Exception:
        print("Wystąpił błąd podczas obliczeń.")

try:
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))
    pole_trojkata(a, b, c)
except ValueError:
    print("Podano nieprawidłowe dane.")