arr = [[5, 8, 10, 6, 4], [11, 20, 1, 13, 2], [7, 9, 14, 22, 3]]
for i in range(len(arr)):
    for x in arr[i]:
        print('%2d' % x, end='   ')
    print()