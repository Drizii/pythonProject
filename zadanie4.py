lista = ["ala ma kota", "kuba ma brode", "wojtek ma skilla"]


def spliter(lista):
    result = []
    for row in lista:
        for word in row.split():
            result.append(f"{word.capitalize()} {len(word)}")
    return result


print(spliter(lista))
