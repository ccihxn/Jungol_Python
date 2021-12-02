a, b, c = map(int, input().split())
n1 = a if a < b else b
n = n1 if n1 < c else c

print(n)