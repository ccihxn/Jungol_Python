n , count = int(input()), 1
for i in range(0, n):
    for j in range(0, n):
        print(count, end=' ')
        count += 2
        if (count > 10):
            count -= 10
    print()