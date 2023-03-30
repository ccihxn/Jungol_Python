arr = list([1, 1, 1, 1, 1] for _ in range(5))

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if i > 0 and j > 0:
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
        print(arr[i][j], end=' ')
    print()

