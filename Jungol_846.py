count_of_3 = 0
count_of_5 = 0
arr = list(map(int, input().split()))

for i in range(10):
    if arr[i] % 3 == 0:
        count_of_3 += 1
    if arr[i] % 5 == 0:
        count_of_5 += 1

print('Multiples of 3 :', count_of_3)
print('Multiples of 5 :', count_of_5)