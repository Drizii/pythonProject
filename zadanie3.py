from core import spliter, fetch_data_from_user, save_data_from_user
# file = open("result.txt", "w")
#
# sentence = input("Wpisz swoje zdanie: ")
#
# for word in sentence.split():
#     file.write(word + " " + str(len(word)) + "\n")
#     print(word + " " + str(len(word)) + "\n")
# print("Zapisano powyższe zmiany do pliku")
#
# file.close()

#sentence = input("Wpisz swoje zdanie: ")
# with open("result.txt", "w") as file:
#     for word in sentence.split():
#         file.write(word + " " + str(len(word)) + "\n")
#         print(word.capitalize() + " " + str(len(word)))


sentence = fetch_data_from_user()
splited_sentence = spliter(sentence)
save_data_from_user(splited_sentence)
