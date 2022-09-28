num = 9119


def square_digits(num):
    numStr = str(num)
    output = []
    for n in numStr:
        n = int(n)
        output.append(n**2)
    outputStr = [str(int) for int in output]
    return int("".join(outputStr))



print(square_digits(num))