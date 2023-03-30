animal = ["", "", ""]
sound = ["", "", ""]
for i in range(3) :
    animal[i], sound[i] = input().split()
    print(animal[i], 'sounds', sound[i]+'.')