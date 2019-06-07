import random
m = random.randint(1,100)

a = input("Insert N = ")
n = int(a)

if n < m:
    print(m)
elif n > m:
    print(n)
else:
    print("You are lucky! M = N")
