import random
def HelperChance(a, b):
    if a ^ b == True:
        return 0.6
    else:
        return 0.2
def Rain_Days(n):
    previous = True
    current = True
    for i in range(n):
        if random.uniform(0, 1) < HelperChance(previous, current):
            previous = current
            current = True
        else:
            previous = current
            current = False
    return HelperChance(previous, current)

print(Rain_Days(5))
