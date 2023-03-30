arr = [20]
arr = list(map(int, input().split()))
sum, count = 0, 0

for i in range(0, 20):
    if arr[i] == 0:
        for j in range(i + 1, len(arr)):
            arr[j] = 0
        break
    sum += arr[i]
    count += 1
avg = int(sum/count)
print('%d %d'%(sum, avg))