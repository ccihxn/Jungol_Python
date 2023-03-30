n = int(input())
var_str = input()
var_list = var_str.split()

sum, avg = 0, 0.0

for i in range(0, n):
    sum += int(var_list[i])
avg = sum / n
print('avg : %.1f'% avg)
if avg >= 80:
    print('pass')
else:
    print('fail')

# 구글링을 토대로 작성한 코드. 별도의 복습 필요