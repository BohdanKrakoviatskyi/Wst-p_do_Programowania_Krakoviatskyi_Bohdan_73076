zdanie=input("Wpisz jekieś zdanie.  ")
print(zdanie)

#-------------------------------------------A---------------------------------------------
#-------------------------------------------1---------------------------------------------
alfabet=["a","b","c","d","e","f","m"]
lb_w = [0,0,0,0,0,0,0]

for znak in zdanie:
   # print(f"sprawdzam znak: {znak}")
    for i in range(len(alfabet)):
        #print("czy jest to litera:", alfabet[i])
        if znak == alfabet[i]:
            lb_w[i]+=1
            #print("tak")
            break
lista_slow=zdanie.split(" ")

print(lista_slow)

for slowo in lista_slow:
    slowo[0].upper()
    slowo[-1].upper()
    print(slowo)

#tablica ASCI
