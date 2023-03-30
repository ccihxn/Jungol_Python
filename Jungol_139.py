a, b = map(int, input().split())
if a > b:
    for i in range(1, 10):
        for x in range(a, b - 1, -1):
            print('%d * %d = %2d' % (x, i, x * i), end='   ')
        print()
else:
    for i in range(1, 10):
        for x in range(a, b + 1):
            print('%d * %d = %2d' % (x, i, x * i), end='   ')
        print()