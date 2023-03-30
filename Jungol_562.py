arr, even, odd = list(map(int, input().split())), 0, 0
for i in range(len(arr)):
    if i % 2 == 1:
        even += arr[i]
    else:
        odd += arr[i]
avg_odd = ('%.1f'% (odd / 5))
print('sum :', even)
print('avg :', avg_odd)
