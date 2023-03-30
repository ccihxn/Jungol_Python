odd = int()
even = int()

while True:
    n = int(input())
    if n == 0:
        break
    if n % 2 == 1:
        odd += 1
    else:
        even += 1

print('odd :', odd)
print('even :', even)