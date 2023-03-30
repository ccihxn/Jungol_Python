arr = list(input().split())
arr_num = []
for i in range(2, len(arr), 3):
    arr_num.append(arr[i])
print(arr_num)