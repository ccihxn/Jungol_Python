a, b = map(int, input().split())
min = a if a <= b else b
max = a if a >= b else b

for i in range(min, max+1):
    print(i, end=' ')