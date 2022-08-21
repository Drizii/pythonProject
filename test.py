import string
s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"


def printer_error(s: str) -> str:
    chars = string.ascii_lowercase
    good = list(chars)[chars.find('a'):chars.find('m')+1]
    count = 0
    for c in s:
        if c not in good:
            count += 1
    print("{}/{}".format(count, len(s)))


printer_error(s)



