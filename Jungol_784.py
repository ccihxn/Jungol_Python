arr = [1, 2]
n = int(input())
arr.append(n)
# for i in range(len(arr)):
#     print(arr[len(arr) - i - 1])
for i in range(len(arr) - 1, -1, -1):
    print(arr[i])