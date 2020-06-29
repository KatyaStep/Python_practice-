import random

numberOfStreaks = 0 
streak = 0
flip = []

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        flip.append(random.randint(0,1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for item in range (len(flip)):
        if flip[item] == flip[item-1]:
            streak += 1
        else:
            streak = 0

        if  streak == 6:
            numberOfStreaks += 1

    flip = []

print ("Number of strike: ", numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100)) 