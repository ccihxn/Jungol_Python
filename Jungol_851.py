a, b = map(int, input().split())
min = a if a <= b else b
max = a if a >= b else b
for n in range(min, max + 1):
    print(n, end=' ')