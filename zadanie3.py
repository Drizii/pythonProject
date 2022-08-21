from core import spliter, fetch_data_from_user, save_data_from_user

sentence = fetch_data_from_user()
splited_sentence = spliter(sentence)
save_data_from_user(splited_sentence)
