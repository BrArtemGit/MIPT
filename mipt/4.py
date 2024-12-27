import itertools as its
n, k = map(int, input().split())
data = [str(i + 1) for i in range(n)]
for el in list(its.combinations(data, k)):
    print(*el)