lista_wyrazow = []
zdanie = input("Wpisz zdanie aby policzyc ilosc liter w każdym słowie: ")

lista_wyrazow.append(zdanie.split())

for wyraz in zdanie.split():
    print(wyraz + " " + str(len(wyraz)))
