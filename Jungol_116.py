arr = list(map(int, input().split()))
sum = 0
for n in arr :
    sum += n
print('%.1f' % (sum / len(arr)))