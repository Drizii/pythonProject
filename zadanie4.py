from core import fetch_data_from_user, spliter, display_data_from_user

sentence = fetch_data_from_user()
splited_sentence = spliter(sentence)
display_data_from_user(splited_sentence)