def calc(x, c, y) :
    if c == '+':
        s = str(x)+" "+c+" "+str(y)+" = "+str(x + y)
    elif c == '-':
        s = str(x)+" "+c+" "+str(y)+" = "+str(x - y)
    elif c == '*':
        s = str(x)+" "+c+" "+str(y)+" = "+str(x * y)
    elif c == '/':
        s = str(x)+" "+c+" "+str(y)+" = "+str(int(x / y))
    else :
        s = str(x) + " " + c + " " + str(y) + " = " + str(0)
    return s

x, c, y = input().split()
x = int(x)
y = int(y)
s = calc(x, c, y)
print(s)