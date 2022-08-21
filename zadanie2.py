from core import spliter, display_data_from_user, fetch_data_from_file

sentence = fetch_data_from_file()
splited_sentence = spliter(sentence)
display_data_from_user(splited_sentence)
