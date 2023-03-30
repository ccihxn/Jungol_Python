n = int(input())
sum, count, x = 0, 0, 1
while sum < n:
    sum += x
    x += 2
    count += 1
print('%d %d'%(count, sum))