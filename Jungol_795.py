arr = list(input().split())
arr.pop(len(arr) - 1)
arr.pop(0)
arr.reverse()
print(arr)