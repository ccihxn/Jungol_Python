arr= []
s = input()
for i in range(len(s)-1, -1, -1):
    arr.append(s[i])
print(arr)