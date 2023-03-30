arr = list(map(int, input().split()))
print(len(arr) - 1)

for n in arr:
    if n == 0:
        break
    if n % 2 == 0:
        print(int(n / 2), end=' ')
    else:
        print(n * 2, end=' ')
