# zdanie = input("Wpisz zdanie aby policzyc ilosc liter w każdym słowie: ")

# for wyraz in zdanie.split():
#     print(wyraz.capitalize() + " " + str(len(wyraz)))
#
#
from core import spliter, fetch_data_from_user, display_data_from_user

# print(spliter(zdanie))


sentence = fetch_data_from_user()
splited_sentence = spliter(sentence)
display_data_from_user(splited_sentence)



