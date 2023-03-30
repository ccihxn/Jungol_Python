arr = [[3, 5, 9], [2, 11, 5], [8, 30, 10], [22, 5, 1]]
sum = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=' ')
        sum += arr[i][j]
    print()
print(sum)