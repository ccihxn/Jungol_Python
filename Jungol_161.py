arr = list(map(int, input().split()))
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for n in arr:
    if n != 0:
        count[int(n / 10)] += 1
for i in range(len(count) - 1, -1, -1):
    if count[i] != 0:
        print(i * 10, ':', count[i], 'person')