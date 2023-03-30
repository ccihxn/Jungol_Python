n = list(map(int, input().split()))
count = 0
for i in n:
    if i == 0:
        break
    if i% 3 != 0 and i % 5 != 0:
        count += 1
print(count)