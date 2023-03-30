arr = [[0, 0, 0] for _ in range(4)]
sum = [0, 0, 0, 0]
for i in range(len(arr)):
    print(i+1, 'class?', sep = '', end=' ')
    arr[i] =list(map(int, input().split()))

for i in range(len(arr)):
    for j in range(len(arr[i])):
        sum[i] += arr[i][j]
    print(i+1, 'class', ' : ', sum[i], sep='')