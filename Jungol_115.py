min_height, min_weight = map(int, input().split())
gi_height, gi_weight = map(int, input().split())
if min_height > gi_height and min_weight > gi_weight : print(int(True))
else : print(int(False))