# file = open("file.csv", "r")
#
# list_of_words = [file.read()]
# list_of_words2 = []
#
# for words in list_of_words:
#     splited_words = words.split()
#     for x in splited_words:
#         print(x + " " + str(len(x)))
#
# file.close()

# with open("file.csv") as file:
#     for words in file:
#         splited_words = words.split()
#         for x in splited_words:
#             print(x.capitalize() + " " + str(len(x)))

from core import spliter, display_data_from_user, fetch_data_from_file

# with open("file.csv") as file:
#     print(spliter(file))


sentence = fetch_data_from_file()
splited_sentence = spliter(sentence)
display_data_from_user(splited_sentence)
