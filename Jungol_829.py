sum = 0
count = 0

while True:
    n = int(input())
    if n > 100 or n < 0:
        break
    sum += n
    count += 1

print('sum :', sum)
print('avg : %.1f' % (sum / count))