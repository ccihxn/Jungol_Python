height, weight = map(int, input().split())
ob = weight+100-height
print(ob)
if ob > 0 : print('Obesity')