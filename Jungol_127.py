n = list(map(int, input().split()))
sum = 0
for i in range(0, len(n) - 1):
    sum += n[i]
print('sum :', sum)
print('avg : %.1f'%(sum/(len(n) - 1)))