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
            print("|10 | ")
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
