import pygame, sys
from pygame.locals import *
import random

gameBeginning = True

WINWIDTH = 800
WINHEIGHT = 500
CAPTION = "ai"

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PINK = (251,198,207)

spawnPositions = [(50,0),(100,0), (150,0)]

pygame.init()
fpsClock = pygame.time.Clock()
mySurface = pygame.display.set_mode((WINWIDTH, WINHEIGHT),0,32)

pathwaysList = [1,2,3]
pathSuccesses = []
pathFails = []
pathChances = []

magazine = []
enemies = []

speed = 1 ##

pathwayMultipliers = [1,1,1]
left = False
count = 0
futurePathways = [] # will be appended to


class Entity(object):
    def __init__(self, name, x):
        self.name = name
        self.x = x

    def changeX(self, x, new_x):
        if (self.x < 750 and new_x < 750) and (self.x > 0 and new_x > 0):
            self.x = new_x

        return self.x

class enemy(Entity):
    def __init__(self, name, pathway, dead, x, y, flag):
        super(enemy, self).__init__(name, x)
        self.pathway = pathway
        self.dead = dead
        self.y = y
        self.flag = True

    def changeY(self, y, new_y):
        self.y = new_y
        return self.y

    def changePathway(self, pathway, new_pathway):
        new_pathway = pathways(pathSuccesses)
        self.pathway = new_pathway
        return pathway


#######################################################################

def pathway1(enemyCHOSEN, pathwayMultipliers): #specific to enemy 1 ## straight down middle
    if enemyCHOSEN.y < 400:
        enemyCHOSEN.changeY(enemyCHOSEN.y, enemyCHOSEN.y + (speed*pathwayMultipliers[0]))
    if enemyCHOSEN.y > 375:
        enemyCHOSEN.pathway = -1
        pathSuccesses.append(1)
        enemyCHOSEN.flag = False
        enemyCHOSEN.y = 0

def pathway2(enemyCHOSEN, left, pathwayMultipliers):
    enemyCHOSEN.changeY(enemyCHOSEN.y, enemyCHOSEN.y + (speed*pathwayMultipliers[1]))
    if enemyCHOSEN.x < 200:
        left = False
    if enemyCHOSEN.x > 600:
        left = True
    if left:
        enemyCHOSEN.changeX(enemyCHOSEN.x, enemyCHOSEN.x-(speed*pathwayMultipliers[1]))
    else:
        enemyCHOSEN.changeX(enemyCHOSEN.x, enemyCHOSEN.x+(speed*pathwayMultipliers[1]))
    if enemyCHOSEN.y > 375:
        enemyCHOSEN.pathway = -1
        pathSuccesses.append(2)
        enemyCHOSEN.flag = False
        enemyCHOSEN.y = 0

    return left
       

def pathway3(enemyCHOSEN, pathwayMultipliers):
    if enemyCHOSEN.y < 400 and enemyCHOSEN.x < 800:
        enemyCHOSEN.changeY(enemyCHOSEN.y, enemyCHOSEN.y+(speed*pathwayMultipliers[2]))
        enemyCHOSEN.changeX(enemyCHOSEN.x, enemyCHOSEN.x+(speed*pathwayMultipliers[2]))
    if enemyCHOSEN.y > 375:
        enemyCHOSEN.pathway = -1
        pathSuccesses.append(3)
        enemyCHOSEN.flag = False
        enemyCHOSEN.y = 0
           
#######################################################################

class bullet(object):
    def __init__(self, x, y):
        self.x, self.y = x,y
        self.flag = False

    def move(self):
        if self.flag:
            self.y -= 10
            if self.y <= 0:
                self.y = 300
                self.flag = False
               
    def drawToScreen(self):
        if self.flag:
            bulletSurface = pygame.Surface((5,10))
            bulletSurface.fill(RED)
            mySurface.blit(bulletSurface, (self.x,self.y))

#####################################################################

def resetFromDeath(enemyCHOSEN, futurePathways):
    if not enemyCHOSEN.flag or enemyCHOSEN.dead:
        enemyCHOSEN.x, enemyCHOSEN.y = random.randint(50,726), 0 ###################### resets to path 1
        enemyCHOSEN.changePathway(enemyCHOSEN.pathway, futurePathways[0])
        futurePathways.pop(0)
        #new_pathway = pathways(pathSuccesses)
        #enemyCHOSEN.pathway = enemyCHOSEN.changePathway(enemyCHOSEN.pathway, new_pathway)
        enemyCHOSEN.flag = True
        enemyCHOSEN.dead = False
       
    return enemyCHOSEN, futurePathways


def choosePaths(futurePathways, pathSuccesses, pathChances, pathwayMultipliers):
    if len(pathSuccesses) % 5 == 0 and len(pathSuccesses) > 1:
        pathChances = []
        for i in range(3):
            count = 0
            for j in range(len(pathSuccesses)):
                if pathwaysList[i] == pathSuccesses[j]:
                    count += 1
                   
            pathChances.append(((count/len(pathSuccesses)*100) // 1)) #sum(pathChances)- sum(pathSuccesses)*100)) 100-(sum(pathChances))-
            #print("pathway", pathwaysList[i], "has a", (count/sum(pathSuccesses)*100) // 1, "% chance of spawning")
            #if pathChances[i] < 0:
             #   pathChances[i] = 0.0
    if 1 not in pathSuccesses:
        pathwayMultipliers[0] += 0.5
        pathSuccesses.append(1)
    if 2 not in pathSuccesses:
        pathwayMultipliers[1] += 0.5
        pathSuccesses.append(2)
    if 3 not in pathSuccesses:
        pathwayMultipliers[2] += 0.5
        pathSuccesses.append(3)
    return pathChances, pathSuccesses, pathwayMultipliers
       

def shootBullet(keyValue, magazine, enemy1, enemy2, enemy3, pathfails):
   
    if keyValue[2]:
        b = bullet(player.x+25, 425)
        b.flag = True
        magazine.append(b)

    index = 0

    for item in magazine:
        item.move()
        item.drawToScreen()
        if not item.flag:
            magazine.pop(index)
        index += 1


        for i in range(25):
            for j in range(25):

                if (item.x+i, item.y+j) == (enemy1.x, enemy1.y):
                    enemy1.dead = True
                    pathFails.append(enemy1.pathway)
                    if enemy1.pathway in pathSuccesses:
                        pathSuccesses.remove(enemy1.pathway)
                if (item.x+i, item.y+j) == (enemy2.x, enemy2.y):
                    enemy2.dead = True
                    pathFails.append(enemy2.pathway)
                    if enemy2.pathway in pathSuccesses:
                        pathSuccesses.remove(enemy2.pathway)
                if (item.x+i, item.y+j) == (enemy3.x, enemy3.y):
                    enemy3.dead = True
                    pathFails.append(enemy3.pathway)
                    if enemy3.pathway in pathSuccesses:
                        pathSuccesses.remove(enemy3.pathway)

    return enemy1, enemy2, enemy3, pathFails

def pathways(pathSuccesses): ##AI picking
    if pathSuccesses == []:
        new_pathway = random.randint(1,3)
    else:
        pathSuccesses.sort()
        new_pathway = random.choice(pathSuccesses) ##
       
    return new_pathway

def makePygameFont(message, size, colour, xPos, yPos):
    font = pygame.freetype.Font(None, size) # None = default font style. # 20 = the size
    text = font.render(message,colour) # text is now a tuple. index 0 = surface & index 1 = rect
    textpos = text[1] #textpos is the rectangle
    textpos.centerx = xPos # x position of text.
    textpos.centery = yPos # y position of text
    mySurface.blit(text[0],textpos)


def drawPositions(enemy1model, enemy2model, enemy3model, playerModel):
    if enemy1.flag:
        pygame.draw.rect(mySurface, RED, enemy1model)
    if enemy2.flag:
        pygame.draw.rect(mySurface, GREEN, enemy2model)
    if enemy3.flag:
        pygame.draw.rect(mySurface, BLUE, enemy3model)
    pygame.draw.rect(mySurface, PINK, playerModel)


enemy1 = enemy("1", -1, False, 50, 0, False) #name, pathway, dead, x, y
enemy2 = enemy("2", -1, False, 100, 0, False)
enemy3 = enemy("3", -1, False, 150, 0, False)
player = Entity("Player", 350)

enemy1model = pygame.Rect(enemy1.x, enemy1.y, 25,25)#x,y,w,h
enemy2model = pygame.Rect(enemy2.x, enemy2.y,25,25)
enemy3model = pygame.Rect(enemy3.x, enemy3.y,25,25)
playerModel = pygame.Rect(player.x,425,50,50)

def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def userInputs(keyValue, player):
    LEFT = 0
    RIGHT = 1
    SPACE = 2

    key = pygame.key.get_pressed()

    if key[K_LEFT]:
        keyValue[LEFT] = True
        player.x = player.changeX(player.x, player.x - 10)
       
    if key[K_RIGHT]:
        keyValue[RIGHT] = True
        player.x = player.changeX(player.x, player.x + 10)

    if key[K_SPACE]:
        keyValue[SPACE] = True

    return keyValue, player

print(vars(enemy1))

def updatePathFromNull(enemy1, enemy2, enemy3, futurePathways):
    if enemy1.pathway == -1:
        enemy1.changePathway(-1, futurePathways[0])
        futurePathways.pop(0)
    if enemy2.pathway == -1:
        enemy2.changePathway(-1, futurePathways[0])
        futurePathways.pop(0)
    if enemy3.pathway == -1:
        enemy3.changePathway(-1, futurePathways[0])
        futurePathways.pop(0)

    return enemy1, enemy2, enemy3, futurePathways

while True:
    #print(pathSuccesses)
    mySurface.fill(BLACK)
    keyValue = [False, False, False]
    events()
    oldX = player.x
    keyValue, player = userInputs(keyValue, player)
    if enemy1.y == 0:
        enemy1.flag = True
    if enemy2.y == 0:
        enemy2.flag = True
    if enemy3.y == 0:
        enemy3.flag = True
       
    if oldX != player.x: #if updates, change model
        playerModel = pygame.Rect(player.x,425,50,50)

    for i in range(3-len(futurePathways)):
        new_pathway = pathways(pathSuccesses)
        futurePathways.append(new_pathway)

    makePygameFont((f"NEXT PATHS: {futurePathways[0]} {futurePathways[1]} {futurePathways[2]}"),
                   15, RED, 700, 480)
       
    enemy1, enemy2, enemy3, futurePathways = updatePathFromNull(enemy1, enemy2, enemy3, futurePathways)

    if enemy1.pathway == 1:
        pathway1(enemy1, pathwayMultipliers)
    elif enemy1.pathway == 2:
        left = pathway2(enemy1, left, pathwayMultipliers)
    elif enemy1.pathway == 3:
        pathway3(enemy1, pathwayMultipliers)

    if enemy2.pathway == 1:
        pathway1(enemy2, pathwayMultipliers)
    elif enemy2.pathway == 2:
        left = pathway2(enemy2, left, pathwayMultipliers)
    elif enemy2.pathway == 3:
        pathway3(enemy2, pathwayMultipliers)

    if enemy3.pathway == 1:
        pathway1(enemy3, pathwayMultipliers)
    elif enemy3.pathway == 2:
        left = pathway2(enemy3, left, pathwayMultipliers)
    elif enemy3.pathway == 3:
        pathway3(enemy3, pathwayMultipliers)


    enemy1model = pygame.Rect(enemy1.x, enemy1.y, 25,25)#x,y,w,h
    enemy2model = pygame.Rect(enemy2.x, enemy2.y, 25,25)
    enemy3model = pygame.Rect(enemy3.x, enemy3.y, 25,25)
   

    enemy1, enemy2, enemy3, pathFails = shootBullet(keyValue, magazine, enemy1, enemy2, enemy3, pathFails)
    if enemy1.dead:
        enemy1, futurePathways = resetFromDeath(enemy1, futurePathways)
    if enemy2.dead:
        enemy2, futurePathways = resetFromDeath(enemy2, futurePathways)
    if enemy3.dead:
        enemy3, futurePathways = resetFromDeath(enemy3, futurePathways)

    drawPositions(enemy1model, enemy2model, enemy3model, playerModel)

    makePygameFont((f"ENEMIES KILLED: {pathFails[-5:]}"), 15, RED, 120, 480)
    pathChances, pathSuccesses, pathwayMultipliers = choosePaths(futurePathways, pathSuccesses, pathChances, pathwayMultipliers)
    makePygameFont(("% chance of spawning:"), 15, RED, 600, 245)
    if pathChances != []:
        makePygameFont((f"Pathway 1: {pathChances[0]} %"), 15, RED, 600, 260)
        makePygameFont((f"Pathway 2: {pathChances[1]} %"), 15, RED, 600, 285)
        makePygameFont((f"Pathway 3: {pathChances[2]} %"), 15, RED, 600, 300)
    else:
        makePygameFont(("Not calculated..."), 15, RED, 600, 260)
       

    pygame.display.flip()
    fpsClock.tick(50)


