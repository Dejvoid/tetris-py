
# Simple pygame program

# Import and initialize the pygame library
from math import fabs
import random
import pygame 
from Square import Square


def checkMove():
    global nextBrick
    global brick
    global ground 
    global groundHeight 
    global groundWidth
    global brickType
    global rotStatus
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
            for j in range(i,0,-1): # error nekde tady, kdyz hraju, tak to posouva spatne, takze prohraju, kdyz nemam
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
    lost = False
    for x in ground[0]:
        if x != None:
            lost = True
    if lost:
        print("you lost")
        messagebox.showwarning("You lost!", "You lost! \nPress start to play again")
        b["state"] = "normal"
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
### 

def leftKey(brick, ground): 
    wasCollision = False
    for s in brick: 
        if s.index[0]-1 < 0 or ground[s.index[1]][s.index[0]-1]:
                wasCollision = True
    if not wasCollision:
        for s in brick:
            s.x -= s.size
            s.index[0] -= 1
def rightKey(brick, ground):
    wasCollision = False
    for s in brick:
        if s.index[0]+1 >= groundWidth or ground[s.index[1]][s.index[0]+1]:
            wasCollision = True
    if not wasCollision:
        for s in brick:
            s.x += s.size
            s.index[0] += 1


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




pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([600, 800])

groundWidth = 10
groundHeight = 20
speed = 500 # higher value = slower
brick = []
ground = [[None]*groundWidth for i in range(groundHeight)]
brickType = random.randint(1,7)
nextBrick = random.randint(1,7)
rotStatus = 0 
squareSize = 25
paused = False

brick = generate(brickType)

# Run until the user asks to quit
running = True
counter = 0
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN: 
            #if event.key == pygame.K_LEFT:
            #    leftKey(brick, ground)
            #if event.key == pygame.K_RIGHT: 
            #    rightKey(brick,ground)
            if event.key == pygame.K_UP: 
                rotate(brickType)
            if event.key == pygame.K_ESCAPE: 
                if paused:
                    paused = False 
                else: 
                    paused = True
            if event.key == pygame.K_DOWN: 
                pass
    if pygame.key.get_pressed()[pygame.K_DOWN]: 
        speed = 50
    else: 
        speed = 500
    if pygame.key.get_pressed()[pygame.K_LEFT]: 
        if counter % 100 == 0:
            leftKey(brick,ground) 
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        if counter % 100 == 0:
            rightKey(brick,ground) 

    if paused:
        pygame.draw.rect(screen,(0,0,0), (0,0,100,100))
    else: 
        if counter % speed== 0:
            checkMove()
            counter = 0

        # Fill the background with white
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (200,200,200), (squareSize, squareSize,groundWidth*squareSize, groundHeight*squareSize))
        for s in brick: 
            pygame.draw.rect(screen, (255,0,0), (s.x,s.y,s.size,s.size))

        for y in range(groundHeight):
            for x in range(groundWidth): 
                if ground[y][x] != None:
                    s = ground[y][x]
                    pygame.draw.rect(screen,(0,0,0), (s.x,s.y,s.size,s.size))

        #pygame.draw.rect(screen, (255,0,0),(x,0,squareSize, squareSize))

    # Flip the display
    pygame.display.flip()
    # moveBrick
    #pygame.time.delay(speed)
    counter += 1


# Done! Time to quit.
pygame.quit()