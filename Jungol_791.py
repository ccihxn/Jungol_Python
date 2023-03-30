num1, count1 = map(int, input().split())
num2, count2 = map(int, input().split())
arr = []

for i in range(count1):
    arr.append(num1)
for i in range(count2):
    arr.append(num2)
print(arr)