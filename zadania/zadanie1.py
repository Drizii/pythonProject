from core import spliter, fetch_data_from_user, display_data_from_user

sentence = fetch_data_from_user()
splited_sentence = spliter(sentence)
display_data_from_user(splited_sentence)
