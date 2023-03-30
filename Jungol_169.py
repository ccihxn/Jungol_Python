arr = [list(input().split()) for _ in range(3)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(chr(ord(arr[i][j]) + 32), end=' ')
    print()