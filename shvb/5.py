def isprime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


class PrimesIterator:
    def __init__(self, q = 0):
        self.q = q
        self.A = [1]
        for i, el in enumerate(self.A):
            if isprime(i): self.A.append(i)

    def isprime(self, n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def __str__(self):
        return self.A


for el in PrimesIterator():
    print(el)
