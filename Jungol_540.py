while True:
    n = int(input())
    if n > 0 and n % 3 != 0:
        continue
    elif n % 3 == 0:
        print(int(n / 3))
    elif n == -1:
        break