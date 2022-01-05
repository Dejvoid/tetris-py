
from tkinter import * 
import random
import time 
import threading


class Square: 
    def __init__(self, x, y,size) -> None:
        self.x = x
        self.y = y 
        self.size = size
        self.index = [x//size-1,y//size-1]
    def recalculateIndex(self): 
        self.index = [self.x//self.size-1,self.y//self.size-1]
### 
# Control Methods
###
def leftArrow(args): 
    wasCollision = False
    if len(squares) >0:
        for i in range(-offset,0):
            s = squares[i]
            if s.index[0]-1 < 0 or ground[s.index[1]][s.index[0]-1]:
                wasCollision = True
        if not wasCollision:
            for i in range(-offset,0):
                squares[i].x -= squares[i].size
                squares[i].index[0] -= 1
    redraw()

def rightArrow(args): 
    wasCollision = False
    if len(squares) >0:
        for i in range(-offset,0):
            s = squares[i]
            if s.index[0]+1 >= groundWidth or ground[s.index[1]][s.index[0]+1]:
                wasCollision = True
        if not wasCollision:
            for i in range(-offset,0):
                squares[i].x += squares[i].size
                squares[i].index[0] += 1
    redraw()

def keyDown(e):
    global speed
    if e.keycode == 40:
        speed = 0.1

def keyUp(e): 
    global speed
    if e.keycode == 40:
        speed = 0.5

def upArrow(args): 
    global brickType
    rotate(brickType) 

###

###
# Program Functions
###
def redraw():
    global offset
    canvas.delete("all")
    if len(squares) >0:
        for s in squares:
            canvas.create_rectangle(s.x,s.y,s.x+s.size,s.y+s.size, fill = "black")
        sq = squares[-1]
        # for sq in activeSquares: 
        for sq in squares[-offset:]:
            canvas.create_rectangle(sq.x,sq.y,sq.x+sq.size,sq.y+sq.size, fill = "red")
    canvas.update()
   
#   0123 - TYPE 1
#
#   012 - TYPE 2
#     3
#
#   012 - TYPE 3
#    3
#
#   01 - TYPE 4
#   23
#
#   123 - TYPE 5
#   4
#
#   01 - TYPE 6
#    23
#
#    13 - TYPE 7
#   02    

###
# SwitcherMethods
###

def createOne():
    return [Square(10,10,10),Square(20,10,10),Square(30,10,10),Square(40,10,10)] 
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
    return [Square(10,20,10), Square(20,10,10), Square(20,20,10), Square(30,10,10)]

def rotateOne(status, block): 
    if status % 2 ==0:
        block[0].x += block[3].size
        block[0].y += block[3].size
        block[2].x -= block[2].size
        block[2].y -= block[2].size
        block[3].x -= block[2].size * 2
        block[3].y += block[2].size * 2
        for s in block:
            s.recalculateIndex()
        
    else: 
        block[0].x -= block[3].size
        block[0].y -= block[3].size
        block[1] = block[1]
        block[2].x += block[2].size
        block[2].y += block[2].size
        block[3].x += block[2].size * 2
        block[3].y -= block[2].size * 2
        for s in block:
            s.recalculateIndex()


def rotateTwo(status, block): 
    size = block[0].size
    if status == 0:
        block[3].x -= 2 * size
        #block[3].y
        block[2].x -= size
        block[2].y += size
        block[0].x += size
        block[0].y -= size
        for s in block:
            s.recalculateIndex()

    elif status ==1: 
        #block[3].x += size
        block[3].y -= 2* size
        block[2].x -= size
        block[2].y -= size
        block[0].x += size 
        block[0].y += size
        for s in block:
            s.recalculateIndex()

    elif status == 2: 
        block[3].x += 2 * size
        #block[3].y 
        block[2].x += size 
        block[2].y -= size
        block[0].x -= size
        block[0].y += size
        for s in block:
            s.recalculateIndex()

    else: 
        #block[3].x 
        block[3].y += 2 * size
        block[2].x += size 
        block[2].y += size
        block[0].x -= size
        block[0].y -= size
        for s in block:
            s.recalculateIndex()

def rotateThree(status, block): 
    size = block[0].size
    if status == 0:
        block[3].x -= size
        block[3].y -= size
        block[2].x -= size
        block[2].y += size
        block[0].x += size
        block[0].y -= size
        for s in block:
            s.recalculateIndex()

    elif status ==1: 
        block[3].x += size
        block[3].y -= size
        block[2].x -= size
        block[2].y -= size
        block[0].x += size
        block[0].y += size
        for s in block:
            s.recalculateIndex()

    elif status == 2: 
        block[3].x += size
        block[3].y += size
        block[2].x += size
        block[2].y -=size 
        block[0].x -= size
        block[0].y += size
        for s in block:
            s.recalculateIndex()

    else: 
        block[3].x -= size
        block[3].y += size
        block[2].x += size
        block[2].y += size
        block[0].x -= size
        block[0].y -= size
        for s in block:
            s.recalculateIndex()

def rotateFour(status, block): 
    return
def rotateFive(status, block): 
    size = block[0].size
    if status == 0:
        #block[3].x
        block[3].y -= 2 * size
        block[2].x -= size
        block[2].y += size
        #block[1].x 
        #block[1].y
        block[0].x += size
        block[0].y -= size
        for s in block:
            s.recalculateIndex()

    elif status ==1: 
        block[3].x += 2 * size
        #block[3].y
        block[2].x -= size
        block[2].y -= size
        #block[1].x
        #block[1].y
        block[0].x += size
        block[0].y += size
        for s in block:
            s.recalculateIndex()

    elif status == 2: 
        #block[3].x
        block[3].y += 2 * size
        block[2].x += size
        block[2].y -= size
        #block[1].x
        #block[1].y
        block[0].x -= size
        block[0].y += size
        for s in block:
            s.recalculateIndex()

    else: 
        block[3].x -= 2 * size
        #block[3].y
        block[2].x += size
        block[2].y += size
        #block[1].x
        #block[1].y
        block[0].x -= size
        block[0].y -= size
        for s in block:
            s.recalculateIndex()

def rotateSix(status, block): 
    size = block[0].size
    if status % 2 ==0:
        block[3].x -= size
        #block[3].y 
        #block[2].x  
        block[2].y -= size 
        block[1].x += size
        #block[1].y
        block[0].x += 2* size
        block[0].y -= size
        for s in block:
            s.recalculateIndex()

    else: 
        block[3].x += size
        #block[3].y 
        #block[2].x  
        block[2].y += size 
        block[1].x -= size
        #block[1].y
        block[0].x -= 2* size
        block[0].y += size 
        for s in block:
            s.recalculateIndex()

def rotateSeven(status, block): 
    size = block[0].size
    if status % 2 ==0:
        #block[3].x
        block[3].y += size
        #block[2].x
        block[2].y -= size
        block[1].x += size
        #block[1].y
        block[0].x += size
        block[0].y -= 2 * size
        for s in block:
            s.recalculateIndex()

    else: 
        #block[3].x
        block[3].y -= size
        #block[2].x
        block[2].y += size
        block[1].x -= size
        #block[1].y
        block[0].x -= size
        block[0].y += 2 * size
        for s in block:
            s.recalculateIndex()

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
    newSq(rotStatus, squares[-offset:])
    print(rotStatus)
    rotStatus += 1
    
    if rotStatus >= 4:
        rotStatus = 0
    
    


def buttonPressed(): 
    global offset
    global nextBrick
    global rotStatus
    global brickType
    rotStatus = 0
    brickType = nextBrick
    brickSq, offset = generate(nextBrick)
    nextBrick = random.randint(1,7)
    for s in brickSq:
        squares.append(s)
    redraw()

def timerTick(): 
    global speed
    while True:
        if len(squares) >0:
            wasCollision = False
            for s in squares[-offset:]:
                if s.index[1]+1 == groundHeight or ground[s.index[1]+1][s.index[0]]:
                    wasCollision = True
            if wasCollision:
                for s in squares[-offset:]:
                    ground[s.index[1]][s.index[0]] = True
                buttonPressed()
            else: 
                for s in squares[-offset:]:
                    s.y += s.size
                    s.index[1]+=1
            redraw()
            time.sleep(speed)

###

groundWidth = 10 
groundHeight = 20
speed = 0.5

form = Tk()
ground = [[False]*groundWidth for i in range(groundHeight)]

b = Button(form, text="Start", command = buttonPressed)
b.pack()
canvas = Canvas(form, width=500, height = 500)
form.bind("<Left>", leftArrow)
form.bind("<Right>", rightArrow)
form.bind("<KeyPress>", keyDown)
form.bind("<KeyRelease>", keyUp)
form.bind("<Up>", upArrow)
canvas.pack()
squares = []
t = threading.Timer(0.5,timerTick)
t = threading.Thread(None, timerTick)
#t.run()
t.start()
brickType = random.randint(1,7)
nextBrick = random.randint(1,7)
rotStatus = 0
form.mainloop()