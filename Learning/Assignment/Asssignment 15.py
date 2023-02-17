import random

lower = int(input("Enter a lower boundary:"))
higher = int(input("Enter higher boundary :"))

if higher > lower:
    a = random.randrange(lower, higher + 1)
    print(a)
else:
    print("boundary choice isnt right")


