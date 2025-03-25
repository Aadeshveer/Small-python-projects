import re
import random

print(" Dice Roller ".center(60,'*'))
while True:
    while True:
        x = input("Enter command with syntax no_of_dice d no_of_sides_of_dice + modifier\n> ")
        if x.lower()=='q':
            exit(0)
        if re.search("^[0-9]+ *d *[0-9]+ *([+-] *[0-9]+){0,1}$",x)==None:
            print("Invalid input!!")
        else:
            break
    num,side,mod = re.match("^([0-9]+) *d *([0-9]+) *([+-] *[0-9]+){0,1}$",x).groups()
    rolls = []
    result = 0
    for _ in range(int(num)):
        roll = random.randint(1,int(side))
        result+=roll
        rolls.append(roll)
    if mod is None:
        mod = 0
    else:
        result+=int(mod)
        rolls.append(mod)
    print(result,tuple(rolls))