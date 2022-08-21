from core import fetch_data_from_user, spliter, save_data_from_user

sentence = fetch_data_from_user()
splited_sentence = spliter(sentence)
save_data_from_user(splited_sentence)