import random

# takes in a list of indices and prints the cards parallely
def print_card(cards):
    n = len(cards)
    # top line
    for i in range(n):
        print(" ___  ",end="")
    print("")
    # top rank line
    for card in cards:
        if card%13==9:
            print("|10 | ",end="")
        elif card == 52:
            print("|## | ",end="")
        else:
            rank='\0'
            match card%13:
                case 0:
                    rank = 'A'
                case 10:
                    rank = 'J'
                case 11:
                    rank = 'Q'
                case 12:
                    rank = 'K'
                case _:
                    rank = card%13+1
            print(f"|{rank}  | ",end="")
    print("")
    # middle symbol line
    for card in cards:
        symbol='\0'
        if card == 52:
            print("|###| ",end="")
        else:
            match card//13:
                case 0:
                    symbol = chr(9829) # Hearts
                case 1:
                    symbol = chr(9830) # Diamonds
                case 2:
                    symbol = chr(9824) # Spades
                case 3:
                    symbol = chr(9827) # Clubs
                case _:
                    raise "Out of range"
            print(f"| {symbol} | ",end="")
    print("")
    # bottom line and rank
    for card in cards:
        if card%13==9:
            print("|_10| ",end="")
        elif card == 52:
            print("|_##| ",end="")
        else:
            rank='\0'
            match card%13:
                case 0:
                    rank = 'A'
                case 10:
                    rank = 'J'
                case 11:
                    rank = 'Q'
                case 12:
                    rank = 'K'
                case _:
                    rank = card%13+1
            print(f"|__{rank}| ",end="")
    print("")

# returns a valid card
def get_card():
    x = random.randint(0,51)
    return x

# returns the card in words
def card_in_words(card):
    words = ""
    match card%13:
        case 0:
            words+='A'
        case 12:
            words+='K'
        case 11:
            words+='Q'
        case 10:
            words+='J'
        case _:
            words+=str(card%13)
    words += " of "
    match card//13:
        case 0:
            words += chr(9829) # Hearts
        case 1:
            words += chr(9830) # Diamonds
        case 2:
            words += chr(9824) # Spades
        case 3:
            words += chr(9827) # Clubs
        case _:
            raise "Out of range"
    return words
    
# calculates the sum for give set of cards
def summation(cards):
    sum = 0
    ace = 0
    for card in cards:
        if card%13>9:
            sum+=10
        elif card%13>0:
            sum+=card%13+1
        else:
            ace+=1
    while(ace>0 and 21-(sum+ace)>=10):
        ace-=1
        sum+=11
    if 52 in cards:
        return "???"
    return sum
    
# returns a boolean if player has a bust or blackjack
def check_bust(cards):
    return summation(cards)>21

# prints the hand of a character(dealer or player)  
def print_hand(dealer,player):
    print(f"DEALER: {summation(dealer)}")
    print_card(dealer)
    print(f"PLAYER: {summation(player)}")
    print_card(player)

money = 5000

print(" BLACK JACK ".center(40,"*"))
print('''
    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.\n\n''')
new = True
stand = False
bet = 0
while(True):
    if bet == 0:
        print(f"\nMoney : {money}")
        bet = input(f"How much money do you bet? (1-{money} or QUIT)\n> ")
        if bet.lower() == "quit":
            break
        else:
            bet = int(bet)
    else:
        print(f"\nBet: {bet}\n")
        if(new):
            dealer = []
            player = []
        new=False
        if dealer == []:
            dealer.append(get_card())
            dealer.insert(0,52)
            player.append(get_card())
            player.append(get_card())

        print_hand(dealer,player)
        move = input("(H)it, (S)tand, (D)ouble down\n> ")
        match move.lower():
            case 'h':
                player.append(get_card())
                print(f"You drew a {card_in_words(player[-1])}.")
                if check_bust(player):
                    print_hand(dealer,player)
                    print("You have a bust")
                    money -= bet
                    bet = 0
                    new = True
                    input("Press enter to continue")
            case 's':
                stand = True
            case 'd':
                # TODO: implement double down
                pass
        if stand:
            dealer.pop(0)
            while(summation(dealer)<17):
                dealer.append(get_card())
                print(f"Delaer drew a {card_in_words(dealer[-1])}")
                print_hand(dealer,player)
            if summation(dealer)>21 or summation(dealer)<summation(player):
                print("!!! YOU WIN !!!")
                print(f"Received {bet}")
                money+=bet
            elif summation(dealer) == summation(player):
                print("We have a Tie")
            else:
                print("You LOSE")
                print(f"You lost {bet}")
                money-=bet
            new = True
            bet = 0
            stand = False
            input("Press enter to continue")