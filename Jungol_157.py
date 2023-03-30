arr =list(map(int, input().split()))
count, sum = 0, 0
for n in arr:
    if n % 5 == 0 and n != 0:
        count += 1
        sum += n
avg = '%.1f' % (sum / count)
print('Multiples of 5 :', count)
print('sum :', sum)
print('avg :', avg)