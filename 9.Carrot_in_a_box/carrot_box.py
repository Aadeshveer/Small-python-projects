import os
import random


def string_box(state,p1,p2):
    s = ""
    if state[0]=='closed':
        s+= '  ' + '_'*10 +' '
    else:
        if state[1]=='carrot':
            s+= '   ' + '_'*3 +'VV' +'_'*4+'\n'
            s+= '  |' + ' '*3 +'VV' +' '*4+'|\n'
            s+= '  |' + ' '*3 +'VV' +' '*4+'|\n'
            s+= '  |' + '_'*3 +'||' +'_'*4+'|'
        else:
            s+='   ' + '_'*9 +'\n'
            s+='  |' + ' '*9 +'|\n'
            s+='  |' + ' '*9 +'|\n'
            s+='  |' + '_'*9 +'|'
    s+='   ' + '_'*10 + '\n'
    s+=' /' + ((' '*4 + '||' + ' '*3) if(state[0]=='open' and state[1]=='carrot') else ' '*9) + '/|  /' + ' '*9 + '/|\n'
    s+='+' + '-'*9 + '+ | +' + '-'*9 + '+ |\n'
    s+='|' + "RED".center(9) + '| | |' + "GREEN".center(9) + '| |\n'
    s+='|' + "BOX".center(9) + '| / |' + "BOX".center(9) + '| /\n'
    s+='+' + '-'*9 + '+/  +' + '-'*9 + '+/\n'
    if state[0]=='open':
        s+=('('+state[1].upper()+'!)').center(11)+'\n'
    s+=p1.center(11)+'   '+p2.center(11)
    return s

os.system('cls' if os.name == 'nt' else 'clear')
print(" Carrot in a box ".center(40,'*'))
player1 = input("Human Player 1, Enter your name: ")
player2 = input("Human Player 2, Enter your name: ")

state = ('closed',random.choice(['carrot','empty']))

print("HERE ARE THE TWO BOXES")
print(string_box(state,player1,player2))
print(f"{player1}, you have a RED box in front of you.\n{player2}, you have a GREEN box in front of you.")
input(f"When {player2} has closed their eyes, press Enter...")

os.system('cls' if os.name == 'nt' else 'clear')
print(f"{player1}, here is the inside of your box:")
state=('open',state[1])
print(string_box(state,player1,player2))
input("Press Enter to continue...")

os.system('cls' if os.name == 'nt' else 'clear')
print(f"Now {player2} will choose the box he wants:")
state=('closed',state[1])
print(string_box(state,player1,player2))
input("Press Enter to view the inside of box1...")

os.system('cls' if os.name == 'nt' else 'clear')
print(string_box(('open',state[1]),player1,player2))