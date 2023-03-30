arr = [[0, 0, 0, 0, 0] for _ in range(5)]
arr[0][0], arr[0][2], arr[0][4] = 1, 1, 1

for i in range(1, len(arr)):
    for j in range(len(arr[i])):
        if j == 0:
            arr[i][j] = arr[i-1][j+1]
        elif j == len(arr[i]) - 1:
            arr[i][j] = arr[i-1][j-1]
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
    print()