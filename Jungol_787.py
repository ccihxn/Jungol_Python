arr = list(range(6))
arr_key = []
for i in range(len(arr)) :
    arr[i] = input('Element? ')
arr_key.append(arr[0])
arr_key.append(arr[2])
arr_key.append(arr[4])
arr_key.append(arr[1])
arr_key.append(arr[3])
arr_key.append(arr[5])

print(arr_key)
