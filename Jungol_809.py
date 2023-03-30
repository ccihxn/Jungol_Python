a, b, c = map(int, input().split())

temp = a if a < b else b
min = temp if temp < c else c

print(min)