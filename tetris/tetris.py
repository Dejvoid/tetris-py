
# Tetris
# Autor: David Hřivna, I. ročník
# zimní semestr 2021/2
# Programování 1 NPRG030

from tkinter import * 
import random
import time 
import threading
from tkinter import messagebox

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

### 
# Control Methods
###
def leftArrow(args): # Moves the brick to the left if possible
    wasCollision = False
    for s in brick: 
        if s.index[0]-1 < 0 or ground[s.index[1]][s.index[0]-1]:
            wasCollision = True
    if not wasCollision:
        for s in brick:
            s.x -= s.size
            s.index[0] -= 1
    redraw()
def rightArrow(args): # Moves the brick to the right if possible
    wasCollision = False
    for s in brick:
        if s.index[0]+1 >= groundWidth or ground[s.index[1]][s.index[0]+1]:
            wasCollision = True
    if not wasCollision:
        for s in brick:
            s.x += s.size
            s.index[0] += 1
    redraw()
def keyDown(e): # Checks for DownArrow key and speeds up "gravity" on press
    global speed
    if e.keycode == 40:
        speed = 0.05
def keyUp(e): # Checks for DownArrow key and slows down "gravity" on release
    global speed
    if e.keycode == 40:
        speed = 0.5
def upArrow(args): # On UpArrow key pressed rotates the brick
    global brickType
    rotate(brickType) 
def buttonPressed(): # Start button function (Game start)
    global ground
    global speed
    ground = [[None]*groundWidth for i in range(groundHeight)] # 
    t = threading.Thread(None, timerTick)
    speed = 0.5
    spawnBrick()
    t.start() # start of "game loop"
    b["state"] = "disabled"
###

###
# Graphics Functions
###
def redraw(): # Draws individual squares on canvas
    global brick
    canvas.delete("all")
    canvas.create_line(10,10,10,210,width=2, fill= "black")
    canvas.create_line(10,10,110,10,width=2, fill= "black")
    canvas.create_line(10,210,110,210,width=2, fill= "black")
    canvas.create_line(110,10,110,210,width=2, fill= "black")
    for line in ground:
        for s in line:
            if s != None:
                canvas.create_rectangle(s.x,s.y,s.x+s.size,s.y+s.size, fill = "black")
    for s in brick:
        canvas.create_rectangle(s.x,s.y,s.x+s.size,s.y+s.size, fill = "red")
    canvas.update()
### 

###
# SwitcherMethods
###
# Create methods - generating individual bricks
def createOne():
    # |0|1|2|3|
    return [Square(10,10,10),Square(20,10,10),Square(30,10,10),Square(40,10,10)] 
def createTwo(): 
    # |0|1|2|
    #     |3|
    return [Square(10,10,10), Square(20,10,10), Square(30,10,10), Square(30,20,10)]
def createThree(): 
    # |0|1|2|
    #   |3|
    return [Square(10,10,10), Square(20,10,10), Square(30,10,10), Square(20,20,10)]
def createFour():
    # |0|1|
    # |1|3|
    return [Square(10,10,10), Square(20,10,10), Square(10,20,10), Square(20,20,10)] 
def createFive(): 
    # |0|1|2|
    # |3|
    return [Square(10,10,10), Square(20,10,10), Square(30,10,10), Square(10,20,10)] 
def createSix(): 
    # |0|1|
    #   |2|3|
    return [Square(10,10,10), Square(20,10,10), Square(20,20,10), Square(30,20,10)] 
def createSeven(): 
    #   |1|3|
    # |0|2|
    return [Square(10,20,10), Square(20,10,10), Square(20,20,10), Square(30,10,10)]

# Rotate methods - rotates individual bricks
def rotateOne(status, block): 
    if status % 2 ==0:
        block[0].x += block[3].size
        block[0].y += block[3].size
        block[2].x -= block[2].size
        block[2].y -= block[2].size
        block[3].x -= block[2].size * 2
        block[3].y += block[2].size * 2
    else: 
        block[0].x -= block[3].size
        block[0].y -= block[3].size
        block[1] = block[1]
        block[2].x += block[2].size
        block[2].y += block[2].size
        block[3].x += block[2].size * 2
        block[3].y -= block[2].size * 2
        if block[0].x < 10:
            for s in block:
                s.x += 10
        elif block[3].x > 10*(groundWidth):
            for s in block:
                s.x += 10*(groundWidth) - block[3].x
    for s in block:
            s.recalculateIndex()
def rotateTwo(status, block): 
    size = block[0].size
    if status == 0:
        block[3].x -= 2 * size
        block[2].x -= size
        block[2].y += size
        block[0].x += size
        block[0].y -= size
    elif status ==1: 
        block[3].y -= 2* size
        block[2].x -= size
        block[2].y -= size
        block[0].x += size 
        block[0].y += size
        if block[0].x > 10*(groundWidth):
            for s in block:
                s.x -= 10
    elif status == 2: 
        block[3].x += 2 * size
        block[2].x += size 
        block[2].y -= size
        block[0].x -= size
        block[0].y += size
    else: 
        block[3].y += 2 * size
        block[2].x += size 
        block[2].y += size
        block[0].x -= size
        block[0].y -= size
        if block[0].x < 10:
            for s in block:
                s.x += 10
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
    elif status ==1: 
        block[3].x += size
        block[3].y -= size
        block[2].x -= size
        block[2].y -= size
        block[0].x += size
        block[0].y += size
        if block[0].x > 10*(groundWidth):
            for s in block:
                s.x -= 10
    elif status == 2: 
        block[3].x += size
        block[3].y += size
        block[2].x += size
        block[2].y -=size 
        block[0].x -= size
        block[0].y += size
    else: 
        block[3].x -= size
        block[3].y += size
        block[2].x += size
        block[2].y += size
        block[0].x -= size
        block[0].y -= size
        if block[0].x < 10:
            for s in block:
                s.x += 10
    for s in block:
            s.recalculateIndex()
def rotateFour(status, block): 
    return
def rotateFive(status, block): 
    size = block[0].size
    if status == 0:
        block[3].y -= 2 * size
        block[2].x -= size
        block[2].y += size
        block[0].x += size
        block[0].y -= size
    elif status ==1: 
        block[3].x += 2 * size
        block[2].x -= size
        block[2].y -= size
        block[0].x += size
        block[0].y += size
        if block[0].x > 10*(groundWidth):
            for s in block:
                s.x -= 10
    elif status == 2: 
        block[3].y += 2 * size
        block[2].x += size
        block[2].y -= size
        block[0].x -= size
        block[0].y += size
    else: 
        block[3].x -= 2 * size
        block[2].x += size
        block[2].y += size
        block[0].x -= size
        block[0].y -= size
        if block[0].x < 10:
            for s in block:
                s.x += 10
    for s in block:
        s.recalculateIndex()
def rotateSix(status, block): 
    size = block[0].size
    if status % 2 ==0:
        block[3].x -= size
        block[2].y -= size 
        block[1].x += size
        block[0].x += 2* size
        block[0].y -= size
    else: 
        block[3].x += size
        block[2].y += size 
        block[1].x -= size
        block[0].x -= 2* size
        block[0].y += size 
        if block[0].x < 10:
            for s in block:
                s.x += 10
    for s in block:
            s.recalculateIndex()
def rotateSeven(status, block): 
    size = block[0].size
    if status % 2 ==0:
        block[3].y += size
        block[2].y -= size
        block[1].x += size
        block[0].x += size
        block[0].y -= 2 * size
    else: 
        block[3].y -= size
        block[2].y += size
        block[1].x -= size
        block[0].x -= size
        block[0].y += 2 * size
        if block[0].x < 10:
            for s in block:
                s.x += 10
    for s in block:
        s.recalculateIndex()
### 

###
# Game Logic functions 
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
    return brickSquares()
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
    newSq(rotStatus, brick)
    print(rotStatus)
    rotStatus += 1
    
    if rotStatus >= 4:
        rotStatus = 0
def spawnBrick():
    global nextBrick
    global rotStatus
    global brickType
    global brick
    rotStatus = 0
    brickType = nextBrick
    brick = generate(nextBrick)
    nextBrick = random.randint(1,7)
    redraw()
def timerTick(): # Game loop function
    global speed
    while True:
        wasCollision = False
        for s in brick: 
            if s.index[1]+1 == groundHeight or ground[s.index[1]+1][s.index[0]]!= None:
                wasCollision = True
        if wasCollision:
            for s in brick: 
                ground[s.index[1]][s.index[0]] = s
            spawnBrick()
        else: 
            for s in brick:
                s.y += s.size
                s.index[1]+=1
        for i in range(groundHeight-1,-1,-1):
            wasFull = True
            for x in ground[i]:
                if x== None:
                    wasFull = False
            if wasFull:
                for j in range(i,0,-1):
                    ground[j] = ground[j-1]
                    for s in ground[j]:
                        if s != None: 
                            s.y += s.size 
                            s.recalculateIndex()
                i += 1
        lost = False
        for x in ground[0]:
            if x != None:
                lost = True
        if lost:
            print("you lost")
            messagebox.showwarning("You lost!", "You lost! \nPress start to play again")
            b["state"] = "normal"
            return 
        redraw()
        time.sleep(speed)
###

# Start point of program/initialization
groundWidth = 10 
groundHeight = 20
speed = 0.5
brick = [] # represents brick moved by user
form = Tk()
form.title("Tetris")
ground = [[None]*groundWidth for i in range(groundHeight)] # representation of playground
b = Button(form, text="Start", command = buttonPressed)
b.pack()
canvas = Canvas(form, width=500, height = 500)
form.bind("<Left>", leftArrow)
form.bind("<Right>", rightArrow)
form.bind("<KeyPress>", keyDown)
form.bind("<KeyRelease>", keyUp)
form.bind("<Up>", upArrow)
canvas.pack()
brickType = random.randint(1,7)
nextBrick = random.randint(1,7)
rotStatus = 0 # rotation of brick
form.mainloop()