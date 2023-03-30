n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        if i == j or j == 0:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
for i in range(n-1, -1, -1):
    for j in range(i+1):
        print(arr[i][j], end=' ')
    print()