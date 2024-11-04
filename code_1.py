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

def initialise(windowWidth, windowHeight, windowName, windowColour):
  global mySurface
  pygame.init()
  mySurface = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
  pygame.display.set_caption(windowName)
  mySurface.fill(color=windowColour)

def render():
  pygame.draw.rect(mySurface, emptyTextBoxColour, (55,100,250,40))
  box1 = font.render('Email', True, emptyTextColour)
  mySurface.blit(box1, (65,100))
  pygame.draw.rect(mySurface, emptyTextBoxColour, (55,160,250,40))  
  box2 = font.render('Password', True, emptyTextColour)
  mySurface.blit(box2, (65,160))
  pygame.display.update()

connection = sqlite3.connect('tablez.db')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS TABLEZ")
table = """CREATE TABLE TABLEZ (
           Email VARCHAR(255) NOT NULL,
           First_Name CHAR(25) NOT NULL,
           Last_Name CHAR(25),
           Score INT
        ); """
cursor.execute(table)
print("heart")
connection.close()

initialise(width, height, caption, bgColour)
while True:
  render()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

