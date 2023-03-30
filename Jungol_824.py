sum = 0
count = 0
while True:
    n  = int(input())
    sum += n
    count += 1
    if n >= 100:
        break
avg = format('%.1f' % (sum / count))
print(sum)
print(avg)