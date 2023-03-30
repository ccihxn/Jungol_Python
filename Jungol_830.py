from builtins import print

count = 0

while True:
    n = int(input())
    if n == 0:
        break
    if n % 3 == 0 or n % 5 == 0:
        continue
    count += 1

print(count)