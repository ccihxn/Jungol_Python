height = int(input())
weight = int(input())
obe  = weight + 100 - height
print(obe)

if obe > 0:
    print('Obesity')