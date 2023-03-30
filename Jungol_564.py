arr = list(input().split())
alphabet = list(range(0, 26))

for i in range(len(alphabet)):
    alphabet[i] = 0

for x in arr:
    if ord(x) >= ord('A') and ord(x) <= ord('Z'):
        alphabet[ord(x) - ord('A')] += 1

for i in range(0, 26):
    if alphabet[i] != 0:
        print(chr(ord('A') + i), ':', alphabet[i])