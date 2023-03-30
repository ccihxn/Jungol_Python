def exponentiation(n, r):
    k = 1
    for _ in range(r):
        k *= n
    return k

n, r = map(int, input().split())
key = exponentiation(n, r)
print(key)