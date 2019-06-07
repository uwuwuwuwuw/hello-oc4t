import random
m = random.randint(1,100)

a = input("Insert N = ")
n = int(a)

if n < m:
    print("N smaller than M")
elif n > m:
    print("N bigger than M")
else:
    print("You are lucky!")
