n = int(input())
x = int()
i = 1
while True:
    x = n * i
    if x >= 100:
        break
    print(x, end=' ')
    i += 1
    if x % 10 == 0:
        break