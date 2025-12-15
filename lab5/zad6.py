import math
import keyword

print("Funkcje w module math:")
for nazwa in dir(math):
    if callable(getattr(math, nazwa)):
        print(nazwa)

print("Funkcje typu tuple:")
for nazwa in dir(tuple):
    if callable(getattr(tuple, nazwa)):
        print(nazwa)

print("Funkcje w module keyword:")
for nazwa in dir(keyword):
    if callable(getattr(keyword, nazwa)):
        print(nazwa)