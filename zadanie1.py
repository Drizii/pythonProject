zdanie = input("Wpisz zdanie aby policzyc ilosc liter w każdym słowie: ")

for wyraz in zdanie.split():
    print(wyraz.capitalize() + " " + str(len(wyraz)))
