import pygame, sys
import sqlite3

pygame.init()
titleFont = pygame.font.Font('Feather Bold.ttf', 80)
font = pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 30)
width = 393
height = 852
caption = "login"
bgColour = (22,19,36)
emptyTextBoxColour = (38,32,54)
emptyTextColour = (189,174,232)
mySurface = None
tablesize = 17

table = [['','',0] for i in range(tablesize)]

class buttonNextPage:
  def __init__(self, boxcolour, textcolour, coords, text, page, surface, font):
    self.boxcolour = boxcolour
    self.textcolour = textcolour
    self.coords = coords
    self.text = text
    self.page = page
    self.surface = surface
    self.font = font

  def drawText(self):
    buttonText = self.font.render(str(self.text), False, self.textcolour)
    buttonRect = buttonText.get_rect()
    buttonRect.topleft = (self.coords)
    self.surface.blit(buttonText, buttonRect)
  
  def drawButton(self):
    buttonBase = pygame.Rect(self.coords[0],self.coords[1],140,40)
    pygame.draw.rect(self.surface,self.boxcolour,buttonBase)

class textBox:
  def __init__(self, boxcolour, textcolour, coords, page, surface, font, text):
    self.boxcolour = boxcolour
    self.textcolour = textcolour
    self.coords = coords
    self.page = page
    self.surface = surface
    self.font = font
    self.text = text
    
  def drawButton(self):
    buttonBase = pygame.Rect(self.coords[0],self.coords[1],140,40)
    pygame.draw.rect(self.surface,self.boxcolour,buttonBase)

def initialise(windowWidth, windowHeight, windowName, windowColour):
  global mySurface
  pygame.init()
  mySurface = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
  pygame.display.set_caption(windowName)
  mySurface.fill(color=windowColour)

def encrypt(text): #should i do this before the hashing or after the hashing?
  coded = ''
  for i in range(len(text)):
    coded += chr(ord(text[i]) + 1)
  return coded

def msquare(tablesize): #exception handling: make it so you can't just enter, maybe have password length rules? if not make sure final index is at least 4 characters long
  passw = encrypt(input("pass"))
  hash = ''
  square = ''
  tableindex = 0
  for j in passw:
    hash += str(ord(j))
  print(hash)
  square = str(int(hash) * int(hash))
  square = square[len(square)//2:(len(square)//2)+4]
  print(square)
  tableindex = (int(square))%tablesize
  print(hash, square, tableindex)

  
def events():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEY

def render():
  buttonnp.drawButton()
  buttonnp.drawText()
  # pygame.draw.rect(mySurface, emptyTextBoxColour, (55,100,250,40))
  # box1 = font.render('Email', True, emptyTextColour)
  # mySurface.blit(box1, (65,100))
  # pygame.draw.rect(mySurface, emptyTextBoxColour, (55,160,250,40))  
  # box2 = font.render('Password', True, emptyTextColour)
  # mySurface.blit(box2, (65,160))
  # pygame.display.update()

down = False
up = True
clicked = False

initialise(width, height, caption, bgColour)
buttonnp = buttonNextPage((255,255,255), (255,0,0), (50,50), "hash", "page", mySurface, font)
while True:
  clicked = False
  render()
  pos = pygame.mouse.get_pos()
  buttons = pygame.mouse.get_pressed()
  if up and buttons[0]:
    up = False
    down = True
  elif (not buttons[0]) and down:
    up = True
    clicked = True
    down = False
#  print(buttons[0])
#  print(up,down,clicked)
  if clicked:
    print("Clicked")
    print(table)
    msquare(tablesize)
  events()
  pygame.display.flip()

#complete hash table
#complete login
