print(" Carrot in a box ".center(40,'*'))

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
        s+=state[1].center(11)+'\n'
    s+=p1.center(11)+'   '+p2.center(11)
    return s

player1 = input("Human Player 1, Enter your name: ")
player2 = input("Human Player 2, Enter your name: ")