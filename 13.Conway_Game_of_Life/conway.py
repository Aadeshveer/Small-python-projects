import random
import platform
import time
import os

FILE_NAME = "test1.txt"
DEAD_CHAR = ' '
ALIVE_CHAR = '0'

def clear_screen():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

class conway:

    def __init__(self,x,y,frac):
        self.a = []
        self.height = y
        self.width = x
        self.a.append([])
        for _ in range(self.width+2):
            self.a[0].append(DEAD_CHAR)
        for i in range(self.height):
            self.a.append([])
            self.a[i+1].append(DEAD_CHAR)
            for _ in range(self.width):
                self.a[i+1].append(DEAD_CHAR if random.uniform(0,1)>frac else ALIVE_CHAR)
            self.a[i+1].append(DEAD_CHAR)
        self.a.append([])
        for _ in range(self.width+2):
            self.a[-1].append(DEAD_CHAR)
        
    def __str__(self):
        s = ""
        s+='┌'
        for j in range(self.width+2):
            s+='─'
        s+='┐\n'
        for i in range(self.height):
            s+="│ "
            for j in range(self.width):
                s+=self.a[i+1][j+1]
            s+=" │\n"
        s+='└'
        for j in range(self.width+2):
            s+='─'
        s+='┘'
        return s
    
    def read_file(self,s):
        f = open(s, "r")
        x = f.read()
        ctr = 0
        for i in range(self.height):
            for j in range(self.width):
                self.a[i+1][j+1] = x[ctr]
                ctr+=1
            ctr+=1
            
    def step(self):
        new = [[DEAD_CHAR for _ in range(self.width+2)] for _ in range(self.height+2)]
        for i in range(self.height):
            for j in range(self.width):
                x = self.count_neighbours(i,j)
                if x==3:
                    new[i+1][j+1] = ALIVE_CHAR
                elif x==2:
                    new[i+1][j+1] = self.a[i+1][j+1]
                else:
                    new[i+1][j+1] = DEAD_CHAR
        self.a = new

    def count_neighbours(self,i,j):
        n = 0
        # up left char
        if self.a[i][j] == ALIVE_CHAR:
            n+=1
        # up char
        if self.a[i][j+1] == ALIVE_CHAR:
            n+=1
        # up right char
        if self.a[i][j+2] == ALIVE_CHAR:
            n+=1
        # middle left char
        if self.a[i+1][j] == ALIVE_CHAR:
            n+=1
        # middle right char
        if self.a[i+1][j+2] == ALIVE_CHAR:
            n+=1
        # down left char
        if self.a[i+2][j] == ALIVE_CHAR:
            n+=1
        # down right char
        if self.a[i+2][j+2] == ALIVE_CHAR:
            n+=1
        # down char
        if self.a[i+2][j+1] == ALIVE_CHAR:
            n+=1
        return n

print(" Conway's game of life ".center(50,'*'))
while(True):
    frac = 0
    n = input("Enter a file name(enter r for random, q to quit):\n> ")
    
    if n.lower() == 'q':
        exit(0)
    
    if n.lower() == 'r':        
        while(True):
            try:
                frac = input("Enter fraction of alive cells\n> ")
                if frac.lower() == 'q':
                    exit(0)
                frac = float(frac)
                if not 0<=frac<=1:
                    print("Value of fraction must follow constrains [0,1]\n")
                    continue
                break
            except ValueError:
                print("Enter a Valid decimal number between 0 and 1\n")
    else:
        if not os.path.isfile(n):
            print(f"{n} does not exist!\n")
            continue

    while(True): # reads in height
        try:
            y = input("Enter height of board(max 500)\n> ")
            if y.lower() == 'q':
                exit(0)
            y = int(y)
            if not 0<y<=500:
                print("Value of height must follow constrains (0,500]\n")
                continue
            break
        except ValueError:
            print("Please enter integer value for height.\n")

    while(True): # reads in width
        try:
            x = input("Enter width of board(max 1000)\n> ")
            if x.lower() == 'q':
                exit(0)
            x = int(x)
            if not 0<x<=1000:
                print("Value of width must follow constrains (0,1000]\n")
                continue
            break
        except ValueError:
            print("Please enter integer values for width.\n")

    world = conway(x,y,frac)
    if n.lower()!='r':
        world.read_file(n)
    print(world)
    while(True):
        try:
            n = int(input("Enter number of iterations\n> "))
            break
        except ValueError:
            print("Invalid Integer!!\n")
    for _ in range(n):
        clear_screen()
        world.step()
        print(world)
        time.sleep(0.05)
    input("Press Enter to continue...")