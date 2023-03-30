n = list(map(int, input().split()))

thr = 0
fiv = 0

for i in n:
    if i % 3 == 0:
	    thr += 1
    if i % 5 == 0:
        fiv += 1
print('Multiples of 3 :', thr)
print('Multiples of 5 :', fiv)