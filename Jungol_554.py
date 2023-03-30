n = int(input())
c = ord('A')
x = 1
for i in range(0, n):
    for j in range(n, i, -1):
        print(x, end=' ')
        x += 1
    for j in range(0, i + 1):
        print(chr(c), end=' ')
        c += 1
    print()