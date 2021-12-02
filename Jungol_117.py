arr = list(map(float, input().split()))
sum = 0
sumf = 0
for f in arr :
    sum += int(f)
    sumf += f
print('sum', sum)
print('avg', int(sumf / len(arr)))