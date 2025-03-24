import random

class DiceBoard:
    '''
    Has various ascii art drawings 
    '''
    def __init__(self,modern=True):
        '''
        If modern is set to false it returns a side of dice made using traditional ascii characters
        '''
        self.modern = modern
        if modern:
            self.dot = '●'
            self.upper_left_corner = '┌'
            self.upper_right_corner = '┐'
            self.lower_left_corner = '└'
            self.lower_right_corner = '┘'
            self.vertical = '│'
            self.horizontal = '─'
        else:
            self.dot = 'O'
            self.upper_left_corner = '+'
            self.upper_right_corner = '+'
            self.lower_left_corner = '+'
            self.lower_right_corner = '+'
            self.vertical = '|'
            self.horizontal = '-'
    def dice_string(self,n: int=random.randint(1,6)):
        '''
        Returns a list of strings that form an ASCII representation of a dice face when printed line by line.
        Size of list is 5 and each string has 11 characters
        By default modern is set to true and it returns a side of dice made using extended ascii characters. 
        '''
        lst = []
        if n == None:
            n = random.randint(1,6)
        if n not in [1,2,3,4,5,6]:
            raise ValueError("Input should be an integer from 1 to 6")
        ul = self.dot if n != 1 else ' ' 
        ur = self.dot if n > 3 else ' ' 
        cl = self.dot if n == 6 else ' ' 
        cr = self.dot if n == 6 else ' ' 
        cc = self.dot if n%2==1 else ' ' 
        ll = self.dot if n > 3 else ' ' 
        lr = self.dot if n != 1 else ' ' 
        lst.append(self.upper_left_corner+self.horizontal*9+self.upper_right_corner)
        lst.append(self.vertical+' '+ul+' '*5+ur+' '+self.vertical)
        lst.append(self.vertical+' '+cl+'  '+cc+'  '+cr+' '+self.vertical)
        lst.append(self.vertical+' '+ll+' '*5+lr+' '+self.vertical)
        lst.append(self.lower_left_corner+self.horizontal*9+self.lower_right_corner)
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
    
    def random_square(self,width,height,num_list,boundry=True,modern=True):
        '''
        Returns a list of strings(given by height(+2 if bordered)) with width as number of characters(+2 if bordered)
        When printed line by line form a board with random position of dices showing number in num_list
        Boundry condition will result in making of a bounndry around the board(extra from given dimesions)
        Please make sure that width give is at least 11*num_of_dices+10 and height at least 5*num_of_dice+4
        '''
        if width < 11*(len(num_list))+10 or height < 5*(len(num_list))+4:
            raise ValueError("The width must be at least 11*num_of_dice+10 and height must be at least 5*num_of_dice+4")
        result = []
        position = []
        x = 0
        while True:
            if x>1000:
                raise RuntimeError('It took too long for the board to generate please increase the size of board or decrease the number of dice')
            possible_positions = list([(i,j) for i in range(width) for j in range(height)])
            for _ in range(len(num_list)):
                num = 0
                retry = False
                while True:
                    num+=1
                    x, y = random.choice(possible_positions)
                    if all((x+i,y+j) in possible_positions for i in range(11) for j in range(5)):
                        break
                    if num>1000:
                        retry = True
                        break
                if retry:
                    break
                position.append((x,y))
                for i in range(11): 
                    for j in range(5):
                        possible_positions.remove((x+i,y+j))
            else:
                break
            x+=1

        dice_lst = [self.dice_string(i) for i in num_list]

        if boundry:
            result.append(self.upper_left_corner + width*self.horizontal+self.upper_right_corner)

        for i in range(height):
            row = width*' '
            for ctr in range(len(num_list)):
                x, y = position[ctr]
                if y <= i < y+5:
                    row = row[:x] + dice_lst[ctr][i-y] + row[x+11:]
            if boundry:
                row = self.vertical + row
                row += self.vertical
            result.append(row)
        if boundry:
            result.append(self.lower_left_corner+width*self.horizontal+self.lower_right_corner)
        return result
    