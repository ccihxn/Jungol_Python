arr = list(map(int, input().split()))
max, min, count_max, count_min = 0, 10000, 0, 0
for n in arr:
    if n < 1 or n > 10000:
        continue
    if n < 100:
        if n > max:
            max = n
            count_max += 1
    else:
        if n < min:
            min = n
            count_min += 1
if count_max == 0:
    max = 100
if count_min == 0:
    min = 100
print(max, min)