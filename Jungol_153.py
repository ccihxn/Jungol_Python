arr = list(map(int, input().split()))

if len(arr) <= 4:
    for i in range(len(arr) - 1):
        print(arr[i], end=' ')
else:
    for i in range(len(arr) - 4, len(arr) - 1):
        print(arr[i], end=' ')
