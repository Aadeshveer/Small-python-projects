import random

DEAD_CHAR = '_'
ALIVE_CHAR = '*'

class conway:
    a = []

    def __init__(self,x,y,frac):
        self.height = y
        self.width = x
        for i in range(self.height):
            self.a.append([])
            for _ in range(self.width):
                self.a[i].append(DEAD_CHAR if random.uniform(0,1)>frac else ALIVE_CHAR)
        
    def print_cells(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.a[i][j],end='')
            print()
    
    def iterate(self):
        # TODO: make function to follow rules of game of life to next generation
        pass

print(" Conway's game of life ".center(50,'*'))
while(True):
    try:
        x = int(input("Enter width of board(max 100)\n> "))
        y = int(input("Enter height of board(max 50)\n> "))
        frac = float(input("Enter fraction of alive cells\n> "))
        if not 0<x<=100:
            print("Value of width must follow constrains (0,100]")
            continue
        if not 0<y<=50:
            print("Value of height must follow constrains (0,50]")
            continue
        if not 0<=frac<=1:
            print("Value of fraction must follow constrains [0,1]")
            continue
        break
    except ValueError:
        pass
    except TypeError:
        print("Please enter integer values for height and width and real for fraction")

world = conway(x,y,frac)

# TODO: Make the loop to continue