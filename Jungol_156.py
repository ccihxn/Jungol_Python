arr = list(map(int, input().split()))
min, max = arr[0], arr[0]

for n in arr:
    if n == 999:
        break
    elif n < min:
        min = n
    elif n > max:
        max = n
print('max :', max)
print('min :', min)
