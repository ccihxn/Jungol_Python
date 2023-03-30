n, count, x, p = int(input()), 0, ord('A'), 0
for i in range(0, n):
    for j in range(n, i, -1):
        print(chr(x + count), end=' ')
        count += 1
    for j in range(0, i):
        print(p, end=' ')
        p += 1
    print()