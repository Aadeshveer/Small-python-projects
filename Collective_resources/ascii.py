import random

class DiceBoard:
    '''
    Has various ascii art drawings 
    '''
    def __init__(self):
        pass

    def dice_string(self,n: int=random.randint(1,6),modern=True):
        '''
        Returns a list of strings that form an ASCII representation of a dice face when printed line by line.
        Size of list is 5 and each string has 11 characters
        By default modern is set to true and it returns a side of dice made using extended ascii characters. 
        If modern is set to false it returns a side of dice made using traditional ascii characters
        '''
        lst = []
        if n == None:
            n = random.randint(1,6)
        if n not in [1,2,3,4,5,6]:
            raise ValueError("Input should be an integer from 1 to 6")
        if modern:
            dot = '●'
            upper_left_corner = '┌'
            upper_right_corner = '┐'
            lower_left_corner = '└'
            lower_right_corner = '┘'
            vertical = '│'
            horizontal = '─'
        else:
            dot = 'O'
            upper_left_corner = '+'
            upper_right_corner = '+'
            lower_left_corner = '+'
            lower_right_corner = '+'
            vertical = '|'
            horizontal = '-'
        ul = dot if n != 1 else ' ' 
        ur = dot if n > 3 else ' ' 
        cl = dot if n == 6 else ' ' 
        cr = dot if n == 6 else ' ' 
        cc = dot if n%2==1 else ' ' 
        ll = dot if n > 3 else ' ' 
        lr = dot if n != 1 else ' ' 
        lst.append(upper_left_corner+horizontal*9+upper_right_corner)
        lst.append(vertical+' '+ul+' '*5+ur+' '+vertical)
        lst.append(vertical+' '+cl+'  '+cc+'  '+cr+' '+vertical)
        lst.append(vertical+' '+ll+' '*5+lr+' '+vertical)
        lst.append(lower_left_corner+horizontal*9+lower_right_corner)
        return lst
    
    def adj_dice(self,n_lst,modern=True):
        '''
        Returns a list of 5 strings which when printed with newline in between print the facs of dice with value of n_list
        Size of list is 5 and each string has 11*n characters
        By default modern is set to true and it returns a side of dice made using extended ascii characters. 
        If modern is set to false it returns a side of dice made using traditional ascii characters
        '''
        result = []
        dice_lst = [self.dice_string(i,modern=modern) for i in n_lst]
        for i in range(5):
            result.append("".join([dice_lst[j][i] for j in range(len(dice_lst))]))
        return result
    