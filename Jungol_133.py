n = int(input())
arr = [n]
arr = list(map(int, input().split()))
sum = 0
for i in range(0, n):
    sum += arr[i]
avg = ('%.2f' % (sum/n))
print(avg)