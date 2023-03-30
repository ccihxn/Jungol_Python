n = int(input())
for i in range(0, n):
    for j in range(0, n):
        print('(%d, %d)'%(i + 1, j + 1), end=' ')
    print()