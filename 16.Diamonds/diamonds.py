def main():
    print(" Diamonds ".center(50,'*'))
    while(True):
        try:
            n = input("Enter size of diamond(q to quit)\n> ")
            if n.lower() == 'q':
                exit()
            else:
                n = int(n)
                if not n>0:
                    raise ValueError
                break
        except ValueError:
            print("Please enter a positive integer for size!")
    print(draw_hollow(n))
    print(draw_solid(n))

def draw_hollow(n):
    lst = []
    for i in range(n):
        lst.append(' '*(n-i-1)+'/'+' '*i*2+'\\'+"\n")
    for i in range(n-1,-1,-1):
        lst.append(' '*(n-i-1)+'\\'+' '*i*2+'/'+"\n")
    return ''.join(lst)

def draw_solid(n):
    lst = []
    for i in range(n):
        lst.append(' '*(n-i-1)+'/'*(i+1)+'\\'*(i+1)+"\n")
    for i in range(n-1,-1,-1):
        lst.append(' '*(n-i-1)+'\\'*(i+1)+'/'*(i+1)+"\n")
    return ''.join(lst)

if __name__=='__main__':
    main()