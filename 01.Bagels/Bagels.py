import random
print("Welcome to BAGELS!")
name = input("\nPlease enter your name: ")
print(f"\nHello! {name}.\nHere is a quick set of rules: ")
print('''
1. I will think of a three digit number, you have to guess it.
2. You will get 10 attempts.
3. Each turn I will give you following hints corresponding to your answer:
    a) Pico-     One digit is correct, but at incorrect position.
    b) Fermi-    One digit is correct and is at correct position.
    c) Bagels-   None of the digits is correct.
      
For example if the number is 248 and you guessed 849 the hint would be:\nPico Fermi\n''')

num = str(random.randrange(100,1000))
n = [num[0],num[1],num[2]]

print("I have thought my number.\nLet the guessing begin!")
for i in range(0,10):
    a = input(f"\n\nGuess #{i+1}\nEnter your guess: ")
    b = [a[0],a[1],a[2]]
    p = []
    d = {}
    if a==num:
        print("\nCongratulations! You have guessed the number.\n !!! YOU WIN !!! ")
        break
    for k in b:
        d[k]=True
    for j in range(0,3):
        if b[j]==n[j]:
            p.append("Fermi")
        elif b[j] in n:
            p.append("Pico")
        else:
            p.append("Bagels")
    match p.count("Bagels"):
        case 3:
            p=["Bagels"]
        case 2:
            p.remove("Bagels")
            p.remove("Bagels")
        case 1:
            p.remove("Bagels")
        case _:
            pass
    for k in p:
        print(k, end=" ")
else:
    print(f"\n\nOh, it seems you have run out of chances. The number was {num}, Well better luck next time!\n  :( YOU LOSE :( ")
print("\nThank you for playing.")