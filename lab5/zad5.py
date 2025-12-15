import keyword

slowa = ["for", "print", "break", "done", "bad"]

for slowo in slowa:
    if keyword.iskeyword(slowo):
        print(slowo, "- jest słowem kluczowym")
    else:
        print(slowo, "- nie jest słowem kluczowym")