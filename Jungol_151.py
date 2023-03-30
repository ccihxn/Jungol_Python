arr = list(map(int, input().split()))
sum = 0
for i in range(0, 5, 2):
    sum += arr[i]
print(sum)