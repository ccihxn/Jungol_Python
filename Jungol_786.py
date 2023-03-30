arr = list(range(6))

for i in range(len(arr)) :
    arr[i] = input('Element? ')
n = int(input('Index? '))
for _ in range(n) :
    arr.pop(0)
print(arr)