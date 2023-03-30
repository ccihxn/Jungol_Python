a, b = map(int, input().split())

max = a if a > b else b
min = b if a > b else a

print(max - min)