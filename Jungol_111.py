arr = list(map(int, input().split()))
sum = 0
for n in arr :
    sum += n
print('sum', sum)
print('avg',int(sum/len(arr)))