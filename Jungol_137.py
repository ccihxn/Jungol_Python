row, column = map(int, input().split())
for i in range(1, row + 1):
    for j in range(1, column + 1):
        print(i * j, end=' ')
    print()