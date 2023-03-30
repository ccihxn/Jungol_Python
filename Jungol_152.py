arr = list(map(int, input().split()))
even_sum, odd_sum = 0, 0

for i in range(len(arr)):
    if i % 2 ==1:
        even_sum += arr[i]
    else:
        odd_sum += arr[i]
print('odd :', odd_sum)
print('even :', even_sum)