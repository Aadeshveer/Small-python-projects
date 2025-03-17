print(" Collatz Sequence, or the 3n+1 Problem ".center(50,'*'))
print("""The Collatz sequence is a sequence of numbers made from a given number n by following the following 3 rules:-
    1.) If n is even the next number is n/2.
    2.) If n is odd the next number is 3*n+1.
    3.) If n is 1, Stop. Otherwise, repeat.""")

while(True):
    try:
        inp = input("Enter a statring number (greater than 0)\n> ")
        inp = int(inp)
        if(inp<1):
            print("Invalid number!")
            continue
        break
    except TypeError:
        print("Entered value must be a positive integer!")

while inp!=1:
    print(inp,end=", ")
    if inp%2==1:
        inp = 3*inp+1
    else:
        inp = inp//2
print(1)