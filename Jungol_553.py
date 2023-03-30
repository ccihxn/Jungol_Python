n = int(input())
tmp = n
x = ord('A')
for i in range(0, n):
    for j in range(0, n - i):
        print(chr(x), end='')
        x += 1
    print()