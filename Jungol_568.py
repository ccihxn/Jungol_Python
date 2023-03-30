print('first array')
arr_first = [list(map(int, input().split())) for _ in range(2)]
print('second array')
arr_second = [list(map(int, input().split())) for _ in range(2)]
for i in range(len(arr_first)):
    for j in range(len(arr_first[i])):
        print(arr_first[i][j] * arr_second[i][j], end=' ')
    print()