a, b = map(int, input().split())
arr = [a, b, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(2, len(arr)):
    arr[i] = (arr[i-2] + arr[i-1]) % 10

for n in arr:
    print(n, end=' ')