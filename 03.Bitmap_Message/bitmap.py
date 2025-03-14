# checks if nCr is odd
def odd_ncr(n,r):
    return pow_x(n,2) == pow_x(r,2)+pow_x(n-r,2)

# claculates the power of x in n!
def pow_x(n,x):
    p = 0
    factor = x
    while(n//factor):
        p+=n//factor
        factor*=x
    return p

# generates a pascal triangle and returns its characters in list
def pascal_traiangle(n,char):
    lst = []
    for i in range(n):
        for j in range(n-1-i): lst.append(" ")
        for j in range(i+1):
            lst.append(char+" " if odd_ncr(i,j) else "  ")
        lst.append("\n")
    return lst

print("Bitmap message(pascal's triangle)")
string = input("Enter message to put on bitmap:\n> ")
message = pascal_traiangle(64,"*")
j = 0
for i in range(len(message)):
    if message[i] == "* ":
        message[i] = string[j]+" "
        j += 1
        j %= len(string)
for i in message:
    print(i,end="")