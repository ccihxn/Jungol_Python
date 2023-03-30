arr = list(map(int, input().split()))
count = [0, 0, 0, 0, 0, 0]

for n in arr:
    count[n-1] += 1

for i in range(6):
    print(i+1, ':', count[i])