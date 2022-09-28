n = 10


# Standardowa implementacja ciągu fibonacciego
def fibb(n):
    result = [1, 2]
    for i in range(n-2):
        result.append(result[i] + result[(i + 1)])
    return result


# Implementacja ciągu fibonacciego przez generator
def fibbGenerator(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a


# Implementacja ciągu fibonacciego rekurencyjnie
def rec_fibb(n):
    if n < 2:
        return 1
    else:
        return rec_fibb(n-1) + rec_fibb(n-2)


def fibb2(n):
    return (rec_fibb(a) for a in range(n))


# Implementacja ciągu fibonacciego przez iterator
class FibIterator:

    def __init__(self, n):
        self.n = n
        self.i = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == self.i:
            raise StopIteration

        self.i += 1
        self.a, self.b = self.b, self.a + self.b
        return self.a

print(fibb(n))
print(rec_fibb(n))
print(FibIterator.__init__(self, n=10))

