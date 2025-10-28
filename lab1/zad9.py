a = float(input("ile masz lat:"))

if a <= 4:
    print('wstęp dla ciebe jest bezpłatny')

elif a > 4 and a < 18:
    print('wstęp dla ciebe kosztuje 10 zł')

elif a >= 18:
    b = input("jestesz studentem:")
    if b == 'tak':
        print('masz 25% zniżki')
    elif b == 'nie':
        print('wstęp dla ciebe kosztuje 20 zł')
