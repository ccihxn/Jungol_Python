arr = list(map(int, input().split()))
min = arr[0]
for n in arr:
    if(n < min):
        min = n
print(min)


