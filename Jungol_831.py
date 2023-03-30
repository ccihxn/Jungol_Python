while True:
    width = int(input('Width = '))
    height = int(input('Height = '))
    print('Triangle Area = %.1f' % (width * height / 2))
    c = input('Continue? ')
    if c == 'Y' or c == 'y':
        continue
    else:
        break