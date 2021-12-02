gender, age = input().split()
age = int(age)
if gender == 'M':
    if age > 17:
        print('MAN')
    else:
        print('BOY')
elif gender == 'F':
    if age > 17:
        print('WOMAN')
    else:
        print('GIRL')