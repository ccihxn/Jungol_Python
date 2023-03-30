arr = list(map(int, input().split()))
count = list(range(10))

for i in range(len(count)):
    count[i] = 0

for n in arr:
    if n == 0:
        break
    if n < 10:
        count[0] += 1
    else:
        count[int(n / 10)] += 1

for i in range(10):
    if count[i] != 0:
        print(i, ':', count[i])