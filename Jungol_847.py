arr = list(map(int, input().split()))
sum = 0
for i in range(len(arr)):
    sum += arr[i]
    avg = float(format('%.1f'%(sum/len(arr))))
print('avg :', avg)
if(avg >= 80):
    print('pass')
else:
    print('fail')