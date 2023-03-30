def ternary_operators(a, b, c):
    temp = a if a > b else b
    max = temp if temp > c else c
    return max

a, b, c = map(int, input().split())
max = ternary_operators(a, b, c)
print(max)