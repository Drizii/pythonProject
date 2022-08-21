def spliter(sentence):
    result = []
    for row in sentence:
        for word in row.split():
            result.append(f"{word.capitalize()} {len(word)}")
    return result


def fetch_data_from_user():
    zdanie = input("Wpisz zdanie aby policzyc ilosc liter w każdym słowie: ")
    return [zdanie]


def fetch_data_from_file():
    with open("file.csv") as file:
        result = []
        for row in file:
            result.append(row)
        return result


def display_data_from_user(splited_sentence):
    for row in splited_sentence:
        print(row)


def save_data_from_user(splited_sentence):
    with open("result.txt", "w") as file:
        for row in splited_sentence:
            file.write(row + "\n")
