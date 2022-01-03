
from tkinter import * 
import random
import time 
import threading

#class BrickType(Enum): 
#    TYPE1 = 1 
#    TYPE2 = 2 
#    TYPE3 = 3 
#    TYPE4 = 4 
#    TYPE5 = 5
#    TYPE6 = 7
#    TYPE7 = 7


class Square: 
    def __init__(self, x, y,size) -> None:
        self.x = x
        self.y = y 
        self.size = size
        self.index = [x//size-1,y//size-1]
### 
# Control Methods
###
def leftArrow(args): 
    if len(squares) >0:
        s = squares[-offset]
        if s.index[0]-1 >= 0:
            for sq in squares[-offset:]:
                sq.x -= sq.size
                sq.index[0] -= 1
    canvas.delete("all")
    redraw()

def rightArrow(args): 
    if len(squares) >0:
        s = squares[-1]
        if s.index[0]+1 < groundWidth:
            for sq in squares[-offset:]:
                sq.x += sq.size
                sq.index[0] += 1
    canvas.delete("all")
    redraw()

def downArrow(args): 
    return 

def rotate(args): 
    return 
###

###
# Program Functions
###
def redraw():
    global offset
    if len(squares) >0:
        for s in squares:
            canvas.create_rectangle(s.x,s.y,s.x+s.size,s.y+s.size, fill = "black")
        sq = squares[-1]
        # for sq in activeSquares: 
        for sq in squares[-offset:]:
            canvas.create_rectangle(sq.x,sq.y,sq.x+sq.size,sq.y+sq.size, fill = "red")
    canvas.update()
   
#   ##### - TYPE 1
#
#   ### - TYPE 2
#     #
#
#   ### - TYPE 3
#    #
#
#   ## - TYPE 4
#   ##
#
#     # - TYPE 5
#   ###
#
#   ## - TYPE 6
#    ##
#
#    ## - TYPE 7
#   ##    

###
# SwitcherMethods
###

def createOne():
    return [Square(10,10,10),Square(20,10,10),Square(30,10,10),Square(40,10,10),Square(50,10,10)] 
def createTwo(): 
    return [Square(10,10,10), Square(20,10,10), Square(30,10,10), Square(30,20,10)]
def createThree(): 
    return [Square(10,10,10), Square(20,10,10), Square(30,10,10), Square(20,20,10)]
def createFour(): 
    return [Square(10,10,10), Square(20,10,10), Square(10,20,10), Square(20,20,10)] 
def createFive(): 
    return [Square(10,10,10), Square(20,10,10), Square(30,10,10), Square(10,20,10)] 
def createSix(): 
    return [Square(10,10,10), Square(20,10,10), Square(20,20,10), Square(30,20,10)] 
def createSeven(): 
    return [Square(10,10,10), Square(20,10,10), Square(20,20,10), Square(10,20,10)]

def rotateOne(status): 
    return 
def rotateTwo(status): 
    return 
def rotateThree(status): 
    return 
def rotateFour(status): 
    return 
def rotateFive(status): 
    return 
def rotateSix(status): 
    return 
def rotateSeven(status): 
    return 
### 

def generate(brickType): 
    switcher ={ 
        1: createOne, 
        2: createTwo, 
        3: createThree, 
        4: createFour, 
        5: createFive, 
        6: createSix, 
        7: createSeven
        }
    brickSquares = switcher.get(brickType, lambda: "InvalidBrick")
    return brickSquares(), len(brickSquares())



def rotate(brickType):
    global rotStatus
    switcher ={ 
        1: rotateOne, 
        2: rotateTwo, 
        3: rotateThree, 
        4: rotateFour, 
        5: rotateFive, 
        6: rotateSix, 
        7: rotateSeven
        }
    newSq = switcher.get(brickType, lambda: "invalid")
    #squares[-offset:]  = newSq(rotStatus)
    if rotStatus < 4:
        rotStatus += 1
    else: 
        rotStatus = 0


def buttonPressed(): 
    global offset
    global nextBrick
    # if ground contains full line -> delete squares in line
    brickSq, offset = generate(nextBrick)
    nextBrick = random.randint(1,7)
    for s in brickSq:
        squares.append(s)
    redraw()

def timerTick(): 
    while True:
        if len(squares) >0:
            wasCollision = False
            for s in squares[-offset:]:
                if s.index[1]+1 == groundHeight or ground[s.index[1]+1][s.index[0]]:
                    ground[s.index[1]][s.index[0]] = True
                    wasCollision = True
            if wasCollision:
                buttonPressed()
            else: 
                for s in squares[-offset:]:
                    s.y += s.size
                    s.index[1]+=1
            canvas.delete("all")
            redraw()
            time.sleep(0.5)

###

groundWidth = 10 
groundHeight = 25

form = Tk()
ground = [[False]*groundWidth for i in range(groundHeight)]

b = Button(form, text="Start", command = buttonPressed)
b.pack()
canvas = Canvas(form, width=500, height = 500)
form.bind("<Left>", leftArrow)
form.bind("<Right>", rightArrow)
form.bind("<Down>",downArrow)
form.bind("<Up>", rotate)
canvas.pack()
squares = []
t = threading.Timer(0.5,timerTick)
t = threading.Thread(None, timerTick)
#t.run()
t.start()
nextBrick = random.randint(1,7)
rotStatus = 0
form.mainloop()