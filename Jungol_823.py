while True:
    num = int(input('number? '))
    if num == 0:
        break
    elif num > 0:
        print('positive integer')
    else:
        print('negative number')