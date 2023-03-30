a, b = map(int, input().split())
min, max = a if a <= b else b, a if a >= b else b
sum = 0
count = 0
for x in range(min, max + 1):
    if x % 3 == 0 or x % 5 == 0:
        sum += x
        count += 1
avg = ('%.1f' % (sum / count))
print('sum :', sum)
print('avg :', avg)