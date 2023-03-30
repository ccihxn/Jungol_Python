a, b = map(int, input().split())
min = a if a < b else b
max = a if a >= b else b
sum = 0
count = 0
for n in range(min, max + 1):
    if n % 3 == 0 or n % 5 == 0:
        sum += n
        count += 1
print('sum :', sum)
print('avg : %.1f' % (sum / count))