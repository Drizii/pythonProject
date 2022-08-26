from zadania.core import read_data_from_file, spliter, save_data_from_user

sentence = read_data_from_file()
splited_sentence = spliter(sentence)
save_data_from_user(splited_sentence)