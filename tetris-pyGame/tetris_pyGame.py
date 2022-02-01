
# Tetris - Semester Assignment
# Author: David Hřivna, I. year
# Winter semester 2021/2022
# Subject: NPRG30

# Import and initialize the pygame library
from math import fabs
import random
import pygame
from pygame.constants import SYSTEM_CURSOR_IBEAM 
from Square import Square

# This method is used to check validity of the brick move. Checks for collisions, full rows, loss.
def checkMove():
    global nextBrick
    global brick
    global ground 
    global groundHeight 
    global groundWidth
    global brickType
    global rotStatus
    global menuString
    global paused
    wasCollision = False
    for s in brick: 
        if s.index[1]+1 == groundHeight or ground[s.index[1]+1][s.index[0]]!= None:
            wasCollision = True
    if wasCollision:
        for s in brick: 
            ground[s.index[1]][s.index[0]] = s
            rotStatus = 0
        brickType = nextBrick
        brick = generate(nextBrick)
        nextBrick = random.randint(1,7)
        for y in range(groundHeight):
                for x in range(groundWidth):
                    if ground[y][x] != None:
                        print("1", end="")
                    else: 
                        print("0", end="")
                print()
        print()
    else: 
        for s in brick:
            s.y += s.size
            s.index[1]+=1
    for i in range(groundHeight-1,-1,-1):
        wasFull = True
        for x in range(groundWidth):
            if ground[i][x]== None:
                wasFull = False
        if wasFull: 
            for j in range(i,0,-1):
                ground[j] = ground[j-1]
                for s in ground[j]:
                    if s != None: 
                        s.y += s.size 
                        s.recalculateIndex()
            i += 1
            for y in range(groundHeight):
                for x in range(groundWidth):
                    if ground[y][x] != None:
                        print("1", end="")
                    else: 
                        print("0", end="")
                print()
            print()
    
    lost = False
    for x in ground[0]:
        if x != None:
            lost = True
    if lost:
        print("you lost")
        menuString = "You lost!"
        paused = True
        ground = [[None]*groundWidth for i in range(groundHeight)]
        
        return 

# Create methods - generating individual bricks
def createOne():
    # |0|1|2|3|
    return [Square(squareSize,squareSize,squareSize),Square(2*squareSize,squareSize,squareSize),Square(3* squareSize,squareSize,squareSize),Square(4* squareSize,squareSize,squareSize)] 
def createTwo(): 
    # |0|1|2|
    #     |3|
    return [Square(squareSize,squareSize,squareSize), Square(2*squareSize,squareSize,squareSize), Square(3*squareSize,squareSize,squareSize), Square(3*squareSize,2*squareSize,squareSize)]
def createThree(): 
    # |0|1|2|
    #   |3|
    return [Square(squareSize,squareSize,squareSize), Square(2*squareSize,squareSize,squareSize), Square(3*squareSize,squareSize,squareSize), Square(2*squareSize,2*squareSize,squareSize)]
def createFour():
    # |0|1|
    # |1|3|
    return [Square(squareSize,squareSize,squareSize), Square(2*squareSize,squareSize,squareSize), Square(squareSize,2*squareSize,squareSize), Square(2*squareSize,2*squareSize,squareSize)] 
def createFive(): 
    # |0|1|2|
    # |3|
    return [Square(squareSize,squareSize,squareSize), Square(2*squareSize,squareSize,squareSize), Square(3*squareSize,squareSize,squareSize), Square(squareSize,2*squareSize,squareSize)] 
def createSix(): 
    # |0|1|
    #   |2|3|
    return [Square(squareSize,squareSize,squareSize), Square(2*squareSize,squareSize,squareSize), Square(2*squareSize,2*squareSize,squareSize), Square(3*squareSize,2*squareSize,squareSize)] 
def createSeven(): 
    #   |1|3|
    # |0|2|
    return [Square(squareSize,2*squareSize,squareSize), Square(2*squareSize,squareSize,squareSize), Square(2*squareSize,2*squareSize,squareSize), Square(3*squareSize,squareSize,squareSize)]

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
        if block[0].x < squareSize:
            for s in block:
                s.x += squareSize
        elif block[3].x > squareSize*(groundWidth):
            for s in block:
                s.x += squareSize*(groundWidth) - block[3].x
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
        if block[0].x > squareSize*(groundWidth):
            for s in block:
                s.x -= squareSize
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
        if block[0].x < squareSize:
            for s in block:
                s.x += squareSize
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
        if block[0].x > squareSize*(groundWidth):
            for s in block:
                s.x -= squareSize
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
        if block[0].x < squareSize:
            for s in block:
                s.x += squareSize
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
        if block[0].x > squareSize*(groundWidth):
            for s in block:
                s.x -= squareSize
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
        if block[0].x < squareSize:
            for s in block:
                s.x += squareSize
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
        if block[0].x < squareSize:
            for s in block:
                s.x += squareSize
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
        if block[0].x < squareSize:
            for s in block:
                s.x += squareSize
    for s in block:
        s.recalculateIndex()

# Moves the brick to the left
def leftKey(brick, ground): 
    wasCollision = False
    for s in brick: 
        if s.index[0]-1 < 0 or ground[s.index[1]][s.index[0]-1]:
                wasCollision = True
    if not wasCollision:
        for s in brick:
            s.x -= s.size
            s.index[0] -= 1
# Moves the brick to the right
def rightKey(brick, ground):
    wasCollision = False
    for s in brick:
        if s.index[0]+1 >= groundWidth or ground[s.index[1]][s.index[0]+1]:
            wasCollision = True
    if not wasCollision:
        for s in brick:
            s.x += s.size
            s.index[0] += 1
# Initiates the rotation of the brick
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
    rotateBrick = switcher.get(brickType, lambda: "invalid")
    rotateBrick(rotStatus, brick)
    print(rotStatus)
    rotStatus += 1
    if rotStatus >= 4:
        rotStatus = 0
# Initiates generating the brick
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



# Program start point
pygame.init()
screen = pygame.display.set_mode([600, 800])
groundWidth = 10 # Number of squares in row
groundHeight = 20 # Number of squares in column
speed = 500 # higher value = slower
brick = [] # Represents brick manipulated by user
ground = [[None]*groundWidth for i in range(groundHeight)] # Represents all squares (bricks) in the game
brickType = random.randint(1,7)
nextBrick = random.randint(1,7) # Type of next brick
rotStatus = 0 # Status of rotation (used in rotation methods)
squareSize = 25 
paused = True

brick = generate(brickType)
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

controlsText = ["Controls:","UpArrow: Rotate","DownArrow: Speed Up", "LeftArrow: Move left", "RightArrow: Move right","ESC: Pause"]

running = True
counter = 0 # counter used in speed calculations
menuString = "Game paused"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP: # Up arrow -> Rotate brick
                rotate(brickType)
            if event.key == pygame.K_ESCAPE: # Escape -> pause/unpause the game
                if paused:
                    paused = False 
                else: 
                    paused = True
            if event.key == pygame.K_DOWN: 
                pass
    if pygame.key.get_pressed()[pygame.K_DOWN]: # Down arrow -> speed up
        speed = 50
    else: 
        speed = 500
    if pygame.key.get_pressed()[pygame.K_LEFT]: # Left arrow -> Move brick to the left
        if counter % 100 == 0: # Used to reduce speed
            leftKey(brick,ground) 
    if pygame.key.get_pressed()[pygame.K_RIGHT]: # Right arrow -> Move brick to the right
        if counter % 100 == 0: # Used to reduce speed
            rightKey(brick,ground) 

    if paused: # Shows the game is paused
        pygame.draw.rect(screen,(0,0,0), (squareSize,squareSize+groundHeight*squareSize//4,groundWidth*squareSize+100,groundHeight*squareSize//4))
        textsurface = myfont.render(menuString, False, (0, 255, 255))
        screen.blit(textsurface,(squareSize,squareSize+groundHeight*squareSize//4))
        textsurface2 = myfont.render('Press ESC to continue', False, (0, 255, 255))
        screen.blit(textsurface2,(squareSize,squareSize+groundHeight*squareSize//4+30))
        # Draws controlls
        for x in range(0,len(controlsText)*30,30):
            textsurface = myfont.render(controlsText[x//30], False, (0, 0, 0))
            screen.blit(textsurface,(squareSize+groundWidth*squareSize,squareSize+x))
    else: 
        if counter % speed== 0: # Applies "gravity" on brick in certain frames based on speed
            checkMove()
            counter = 0
        # Graphic interface
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (200,200,200), (squareSize, squareSize,groundWidth*squareSize, groundHeight*squareSize))
        # Draws the user-controlled brick
        for s in brick: 
            pygame.draw.rect(screen, (255,0,0), (s.x,s.y,s.size,s.size))
        # Draws the rest of the squares in game
        for y in range(groundHeight):
            for x in range(groundWidth): 
                if ground[y][x] != None:
                    s = ground[y][x]
                    pygame.draw.rect(screen,(0,0,0), (s.x,s.y,s.size,s.size))
        # Draws controlls
        for x in range(0,len(controlsText)*30,30):
            textsurface = myfont.render(controlsText[x//30], False, (0, 0, 0))
            screen.blit(textsurface,(squareSize+groundWidth*squareSize,squareSize+x))

    

    pygame.display.flip()
    counter += 1
pygame.quit()