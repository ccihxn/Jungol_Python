arr = list(map(int, input().split()))
arr = arr[::-1]
for n in arr:
    if n != 0:
        print(n, end=' ')

