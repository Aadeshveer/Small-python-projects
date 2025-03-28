import random
import time
import sys


class BitStream():
    '''
    Generates a matrix like stream of running 0s and 1s
    '''
    bits = ['0','1']

    def __init__(self, fraction = 0.2, width = 120, delay = 0.05):
        '''
        fraction is fraction of width that should be initially be filled
        width is the width of stream in num of characters
        delay is delay between subsequent frames 
        '''
        self.frac = fraction
        self.width = width
        self.delay = delay
        self.line = []
        for _ in range(self.width):
            self.line.append((random.choice(self.bits)) if random.random()<self.frac else ' ')
    
    def __str__(self):
        '''
        Gives the last line of stream
        '''
        return self.get_str()

    def set_bits(self,x):
        self.bits = x

    def get_str(self):
        '''
        Returns the last line of stream
        '''
        return ''.join(self.line)

    def iterate(self):
        '''
        processes the next bit stream line
        '''
        for i in range(self.width):
            # In order to make the view like bit strings flying up the lines with a bit must contain it for some length which is taken care by following if statement
            if random.randint(1,6)!=1:
                continue
            if self.line[i]==' ':
                if random.random() < self.frac:
                    continue
                self.line[i] = random.choice(self.bits)
            else:
                self.line[i] = ' '

    def loop(self):
        '''
        Runs the code together to make the final effect
        '''
        try:
            while True:
                sys.stdout.write(self.get_str() + "\n")
                sys.stdout.flush()
                self.iterate()
                time.sleep(self.delay)
        except KeyboardInterrupt:
            print("\nExiting...")

class DNAVisualization():
    '''
    Makes a running animation of DNA strand scrolling up
    '''
    Pairs_lst = [
        ( 'A' , 'T' ),
        ( 'T' , 'A' ),
        ( 'G' , 'C' ),
        ( 'C' , 'G' )
    ]

    template=[
    '     ##    ',
    '    #{}-{}#  ',
    '   #{}---{}# ',
    '  #{}-----{}#',
    ' #{}------{}#',
    '#{}------{}# ',
    '#{}-----{}#  ',
    ' #{}---{}#   ',
    ' #{}-{}#     ',
    '  ##       ',
    ' #{}-{}#     ',
    ' #{}---{}#   ',
    '#{}-----{}#  ',
    '#{}------{}# ',
    ' #{}------{}#',
    '  #{}-----{}#',
    '   #{}---{}# ',
    '    #{}-{}#  '
    ]

    def __init__(self,width=60,delay=0.1):
        self.width=width
        self.delay=delay
        self.ctr = 0
        self.line = self.template[self.ctr].center(self.width)

    def __str__(self):
        '''
        prints the last line of stream
        '''
        return self.get_str()
    
    def get_str(self):
        '''
        Returns a string with DNA Visualization in center
        '''
        return self.line
    
    def iterate(self):
        '''
        Changes the new line to next one
        '''
        self.ctr+=1
        new_pair = random.choice(self.Pairs_lst)
        self.line = self.template[self.ctr%len(self.template)].format(new_pair[0],new_pair[1]).center(self.width)

    def loop(self):
        '''
        Infinitely loop through the printing system to generate the effect
        '''
        try:
            while True:
                sys.stdout.write(self.get_str() + "\n")
                sys.stdout.flush()
                self.iterate()
                time.sleep(self.delay)
        except KeyboardInterrupt:
            print("\nExiting...")

class Ducklings():
    '''
    Generates a running stream of ascii art ducklings
    '''
    DIRECTIONS = ['left','right']
    BODIES = [[' ({} )','  ^^ '],['({}  )',' ^ ^ ']]
    EYES = ['"',"''","^^",'``']
    MOUTHS = ['<','=']
    WINGS = ['<','V','^']
    def __init__(self, density = 5, width = 60, delay = 0.2):
        self.density = density
        self.width = width
        self.delay = delay
        self.line = " "*width
        self.__available_indices = [i for i in range(width-5)]
        self.__present_ducks = []

    def __str__(self):
        '''
        Prints last line of stream
        '''
        return self.get_str()
    
    def get_str(self):
        '''
        Returns the last line of stream
        '''
        return self.line

    def duck_gen(self, direction='right', body_type=0, eye_type=0, mouth_type=0, wing_position=0):
        '''
        Generates  a  duckling ASCII art
        
        Args:
            direction: can be 'left' or 'right'
            body_type: can be a non -ve index for BODIES list
            eye_type: can be a non -ve index for EYES list
            mouth_type: can be a non -ve index for MOUTHS list
            wing_position: can be a non -ve index for WINGS list

        returns:
            A list of strings which form the duckling when printed line by line

        raises:
            ValueError: If given arguments are not correct
        '''
        if direction not in self.DIRECTIONS:
            raise ValueError("Given direction argument is invalid")
        if body_type not in range(len(self.BODIES)):
            raise ValueError("Given body_type is invalid")
        if eye_type not in range(len(self.EYES)):
            raise ValueError("Given eye_type is invalid")
        if mouth_type not in range(len(self.MOUTHS)):
            raise ValueError("Given mouth_type is invalid")
        if wing_position not in range(len(self.WINGS)):
            raise ValueError("Given wing_position is invalid")
        
        return [
            self.__head_str(direction,eye_type,mouth_type),
            self.__body_str(direction,body_type,wing_position),
            self.__feet_str(direction,body_type)
            ]
    
    def __head_str(self,direction,eye_type,mouth_type):
        '''
        Generates the head string of duck
        '''
        eyes = self.EYES[eye_type]
        s = (' ' if len(eyes)==2 else '  ')+'('+eyes+self.MOUTHS[mouth_type]
        if direction=='left':
            s = self.__dir_inv(s)
        return s
    
    def __body_str(self,direction,body_type,wing_position):
        '''
        Generates the body string of duck
        '''
        s = self.BODIES[body_type][0].format(self.WINGS[wing_position])
        if direction=='left':
            s = self.__dir_inv(s)
        return s

    def __feet_str(self,direction,body_type):
        '''
        Generates the feet string
        '''
        s = self.BODIES[body_type][1]
        if direction=='left':
            s = self.__dir_inv(s)
        return s

    def __dir_inv(self, s):
        '''
        Reverses the string to change direction
        
        Args:
            s: the string to reverse
        
        returns:
            the inverted string
        '''
        translation = str.maketrans("<>()", "><)(")
        return s.translate(translation)[::-1]
    
    def __select_loc(self):
        '''
        Places a duckling at a random available location if possible
        '''
        if self.__available_indices:
            for _ in range(self.density):
                x = random.choice(self.__available_indices)
                if all((x + i) in self.__available_indices for i in range(5)):  # Ensure enough space
                    new_duck = [
                        x, 
                        0, 
                        self.duck_gen(
                            random.choice(self.DIRECTIONS),
                            random.randint(0, len(self.BODIES) - 1),
                            random.randint(0, len(self.EYES) - 1),
                            random.randint(0, len(self.MOUTHS) - 1),
                            random.randint(0, len(self.WINGS) - 1),
                        ),
                    ]
                    self.__present_ducks.append(new_duck)
                    for i in range(5):
                        if x + i in self.__available_indices:
                            self.__available_indices.remove(x + i)
                    break

    def __refresh_string(self):
        '''
        Refreshes the self.line to incorporate new ducklings
        '''
        lst = [" " for _ in range(self.width)]
        for i in range(len(self.__present_ducks)):
            for j in range(5):
                lst[self.__present_ducks[i][0]+j] = self.__present_ducks[i][2][self.__present_ducks[i][1]][j]
            self.__present_ducks[i][1]+=1
        for i in self.__present_ducks:
            if i[1] == 3:
                self.__available_indices+=[j+i[0] for j in range(5)]
                self.__present_ducks.remove(i)
            
        self.line = "".join(lst)

    def loop(self):
        '''
        Runs the screen saver
        '''
        try:
            while True:
                self.__select_loc()
                self.__refresh_string()
                sys.stdout.write(self.get_str() + "\n")
                sys.stdout.flush()
                time.sleep(self.delay)
        except KeyboardInterrupt:
            print("\nExiting...")