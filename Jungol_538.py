while True:
    n = int(input('number? '))
    if n == 0:
        break
    elif n > 0:
        print('positive integer')
    else:
        print('negative number')