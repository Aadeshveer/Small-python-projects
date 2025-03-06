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
                    rank = card%13
            print(f"|{rank}  | ",end="")
    print("")
    # middle symbol line
    for card in cards:
        symbol='\0'
        if card == 52:
            print("|###| ")
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
            print("|_10| ")
        elif card == 52:
            print("|_##| ")
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
                    rank = card%13
            print(f"|__{rank}| ",end="")

# returns a valid card
def get_card():
    x = random.randint(0,51)
    return x

# returns the card in words
def card_in_words(card):
    str = ""
    match card%13:
        case 0:
            str+='A'
        case 12:
            str+='K'
        case 11:
            str+='Q'
        case 10:
            str+='J'
    str += " of "
    match card//13:
        case 0:
            str += chr(9829) # Hearts
        case 1:
            str += chr(9830) # Diamonds
        case 2:
            str += chr(9824) # Spades
        case 3:
            str += chr(9827) # Clubs
        case _:
            raise "Out of range"
    return str
    

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
while(True):
    print(f"Money : {money}")
    bet = input(f"How much money do you bet? (1-{money} or QUIT)\n> ")
    if bet.lower() == "quit":
        break
    else:
        print(f"\nBet: {bet}\n")
        # TODO: implement main game loop