class_avg = [85.6, 79.5, 83.1, 80.0, 78.2, 75.0]
a, b = map(int, input().split())
print(class_avg[a - 1] + class_avg[b - 1])
