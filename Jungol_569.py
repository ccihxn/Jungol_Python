grade = [list(map(int, input().split())) for _ in range(5)]
sum, count = list(range(len(grade))), 0
for i in range(len(sum)):
    sum[i] = 0

for i in range(len(grade)):
    for j in range(len(grade[i])):
        sum[i] += grade[i][j]

for i in range(len(sum)):
    avg = sum[i] / len(grade[i])
    if avg >= 80:
        print('pass')
        count += 1
    else:
        print('fail')
print('Successful :', count) 