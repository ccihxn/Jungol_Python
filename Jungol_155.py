arr = ['J', 'U', 'N', 'G', 'O', 'L']
c, count = input(), 0

for x in arr:
    if x == c:
        print(arr.index(x))
        count += 1
if count == 0:
    print('none')