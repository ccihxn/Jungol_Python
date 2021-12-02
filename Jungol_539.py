arr = list(map(int, input().split()))
sum = 0
count = 0
for i in arr:
    sum += i
print(sum)
print('%.1f'%(sum/len(arr)))

# 결함 : 100 이상일 때 멈추는 조건이 없음.