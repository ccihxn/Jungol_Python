a, b = input().split()
a = int(a)
b = int(b)
aZero = bool(a != 0)
bZero = bool(b != 0)
print(int(aZero & bZero), int(aZero | bZero))
