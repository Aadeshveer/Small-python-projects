import random
import time


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
                print(self.get_str())
                self.iterate()
                time.sleep(self.delay)
        except KeyboardInterrupt:
            print("\nExiting...")
            exit(0)