arr = list(map(float, input().split()))
sum = 0.
for n in arr:
    sum += n
avg = '%.1f' % (sum / len(arr))
print(avg)