var_list = [[2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9], [6, 7, 8, 9, 10]]

for i in range(len(var_list)):
    for j in range(len(var_list[0])):
        print(var_list[i][j], end=' ')
    print()