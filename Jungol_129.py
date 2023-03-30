while True:
    base = int(input('Base = '))
    height = int(input('Height = '))
    width = base * height / 2
    print('Triangle width = %.1f' % width)
    con = input('Continue? ')
    if str(con) == 'Y' or str(con) == 'y':
        continue
    else:
        break
        
# 콘솔에서는 잘 작동하나, 정올 홈페이지에서 인식 못하는 문제 발생