arr = ['', '', '', '']
for i in (range(4)) :
    arr[i] = input()
for i in (range(0, 3, 2)) :
    out = '%s: %s' % (arr[i], arr[i + 1])
    print(out)