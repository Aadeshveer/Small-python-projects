import random
import sys
sys.path.append('../')
from Collective_resources.ascii import DiceBoard

print(" Cho-Han ".center(50,'*'))

print("This is a traditional Japansese dice game. The dealer will roll two dies in a cup and the player must guess if the sum is even(cho) or odd(han).")

money = 5000

while(money>0):
    while True:
        try:
            bet = input(f"You have {money} mon. How much would you like to bet?\n> ")
            bet = int(bet)
            if bet>money or bet<1:
                raise ValueError
            break
        except (ValueError,TypeError):
            print(f"Please enter a valid bet between 1 and {money}")
    
    print("The dealer swirls the cup and you hear the rattle of the dice.")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    parity = 'o' if (dice1+dice2)%2==1 else 'e'
    print("The dealer slams the cup on the floor, still covering the dice and asks for your bet.")

    inp = input(" CHO (even) or HAN (odd) ?".center(50)+"\n> ")

    while(True):
        if inp.lower() in ["cho","even",'c','e']:
            inp = 'e'
            break
        elif inp.lower() in ["han","odd",'h','o']:
            inp = 'o'
            break
        else:
            inp = input("Please enter a valid input (Cho or Han)\n")
    
    print("The dealer lifts the cup to reveal: ")
    board = DiceBoard()
    for i in board.adj_dice([dice1,dice2]):
        print(i)
    print(f"Sum = {dice2+dice1}")

    if inp==parity:
        print(f"You WON!! You take {2*bet} mon.")
        money+=bet
        print(f"The house collects {bet // 10} mon fee.")
        money-=bet//10
    else:
        print(f"You Lost the bet.")
        money-=bet
    input("Press enter to continue...")

else:
    print("You are broke now".center(50))
    print("YOU LOSE".center(50))