class Display:
    '''
    A class to represent a segmented Display
    '''

    def __init__(self,display_lst=None):
        '''
        display_lst is the list of numbers to be represented in display
        '''
        self.display_lst = display_lst if display_lst is not None else []

    def __str__(self):
        '''
        prints the rendered display
        '''
        return self.get_string()

    def set_display(self,lst):
        '''
        Set the display_lst to different numbers
        '''
        self.display_lst = lst

    def get_string(self):
        '''
        Returns the rendered display as a string
        '''
        lst = []
        for i,j in enumerate(self.display_lst):
            lst.append(self.__top_part(j//10))
            lst.append(' ')
            lst.append(self.__top_part(j%10))
            if i!=len(self.display_lst)-1:
                lst.append("   ")
        lst.append("\n")
        for i,j in enumerate(self.display_lst):
            lst.append(self.__mid_part(j//10))
            lst.append(' ')
            lst.append(self.__mid_part(j%10))
            if i!=len(self.display_lst)-1:
                lst.append(" * ")
        lst.append("\n")
        for i,j in enumerate(self.display_lst):
            lst.append(self.__bottom_part(j//10))
            lst.append(' ')
            lst.append(self.__bottom_part(j%10))
            if i!=len(self.display_lst)-1:
                lst.append(" * ")
        return ''.join(lst)
    
    def __top_part(self,n):
        n%=10
        if n in [1,4]:
            return "   "
        else:
            return " _ "
    
    def __mid_part(self,n):
        n%=10
        if n in [1,7]:
            return "  |"
        elif n in [4,8,9]:
            return "|_|"
        elif n in [5,6]:
            return "|_ "
        elif n in [2,3]:
            return " _|"
        else:
            return "| |"
    
    def __bottom_part(self,n):
        n%=10
        if n in [1,4,7]:
            return "  |"
        elif n in [3,5,9]:
            return " _|"
        elif n in [6,8,0]:
            return "|_|"
        else:
            return "|_ "
