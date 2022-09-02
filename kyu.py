x = "take"
import  string

def high(x):
    dict_letters_points = {}
    points = 0
    for letter in string.ascii_lowercase:
        dict_letters_points[letter] = (ord(letter) - 96)
    for word in x:
        for let in word.split():
            points = points + dict_letters_points[let]

    print(points)


high(x)