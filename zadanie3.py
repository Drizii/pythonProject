file = open("result.txt", "w")

sentence = input("Wpisz swoje zdanie: ")

for word in sentence.split():
    file.write(word + " " + str(len(word)) + "\n")
    print(word + " " + str(len(word)) + "\n")
print("Zapisano powyższe zmiany do pliku")

file.close()
