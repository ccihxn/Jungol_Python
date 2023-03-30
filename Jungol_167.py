arr = [list(map(int, input().split())) for _ in range(4)]
avg, avg_low, avg_high = 0., [0, 0, 0, 0], [0, 0]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        avg_low[i] += arr[i][j]
        avg_high[j] += arr[i][j] / len(arr)
        avg += arr[i][j]
    avg_low[i] = int(avg_low[i] / len(arr[i]))
avg = int(avg / (len(arr) * len(arr[0])))
for i in range(len(avg_low)):
    print(avg_low[i], end=' ')
print()
for i in range(len(avg_high)):
    print(int(avg_high[i]), end=' ')
print()
print(avg)