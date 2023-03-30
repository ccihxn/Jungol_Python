arr = list(map(int, input().split()))
arr.sort(reverse = True)
for n in arr:
    print(n, end=' ')