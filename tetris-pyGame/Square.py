# Class representation of squares of the individual bricks
class Square: 
    def __init__(self, x, y,size) -> None:
        # Variables used for graphics
        self.x = x 
        self.y = y 
        self.size = size 

        # Variable used for in array representation
        self.index = [x//size-1,y//size-1] 

    def recalculateIndex(self): # used to recalculate position within array
        self.index = [self.x//self.size-1,self.y//self.size-1]


