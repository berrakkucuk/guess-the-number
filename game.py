import random

a = random.randrange(0,21)
b = random.randrange(0,21)

min = 0
max = 21

while b != a:

    while b < a:
        print(b)
        print("Too small!")
        min = b
        b = random.randrange(min+1, max)


    while b > a:
        print(b)
        print("Too large!")
        max = b
        b = random.randrange(0, max)

print(b)
print("You found it!")
