import random

f = open("test2.txt", "w")

MAX_CITIES = 50
MAX_ITEMS = 100
MAX_ITEM_PER_CITY = 4

n = random.randint(0, MAX_CITIES)
weight = random.randint(0, 100)
value = random.randint(0, 100)

f.write(str(weight) + " " + str(value) + " " + str(n) + "\n")

for i in range(n):
    x = random.randint(0, 200)
    y = random.randint(0, 200)
    m = random.randint(1, MAX_ITEM_PER_CITY)
    f.write(str(x) + " " + str(y) + " " + str(m) + "\n")

    for j in range(m):
        wei = random.randint(0, 15)
        val = random.randint(0, 15)
        f.write(str(wei) + " " + str(val) + "\n")

f.close()