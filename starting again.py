import pygame
import sys
import sqlite3

#start it all over from the beginning
pygame.init()
tablesize = 17
titleFont = pygame.font.Font('Feather Bold.ttf', 80)
font = pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 30)
width = 393
height = 852
bgColour = (22,19,36)
caption = 'login'
emptyTextBoxColour = (38,32,54)
emptyTextColour = (189,174,232)
surface = screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
surface.fill(color=bgColour)
pygame.display.set_caption(caption)

def events():
    text = ''
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            if len(text)>0:
                text = text[:-1]
        else:
            text += event.unicode
    print(text)

class buttonNextPage:
  def __init__(self, boxcolour, textcolour, coords, text, surface, font, boxshadcolour, width, buttonsize):
    self.boxcolour = boxcolour
    self.textcolour = textcolour
    self.coords = coords
    self.text = text
    self.surface = surface
    self.font = font
    self.boxshadcolour = boxshadcolour
    self.width = width
    self.buttonsize = buttonsize

  def drawText(self):
    buttonText = self.font.render(str(self.text), False, self.textcolour)
    buttonRect = buttonText.get_rect()
    print((self.buttonsize[1]-self.font.size(self.text)[1])/2)
    buttonRect.topleft = (self.width/2 - self.font.size(self.text)[0]/2, self.coords[1]+(self.buttonsize[1]-self.font.size(self.text)[1])/4)
    self.surface.blit(buttonText, buttonRect)
  
  def drawButton(self):
    buttonBase = pygame.Rect(self.coords[0]-15, self.coords[1]-3.75,self.buttonsize[0],self.buttonsize[1])
    pygame.draw.rect(self.surface,self.boxcolour,buttonBase)

  def drawShadow(self):
    buttonBase = pygame.Rect(self.coords[0]-15, self.coords[1]+3.75,self.buttonsize[0],self.buttonsize[1])
    pygame.draw.rect(self.surface,self.boxshadcolour,buttonBase)


def front():
   sbuttcol = (119,73,248)
   sbutttextcol = (38,32,54)
   sbuttshadcol = (85,24,214)
   buttonsize = (318,42)
   buttonfont = pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 18)
   text = 'SIGN UP'
   startB = buttonNextPage(sbuttcol, sbutttextcol,(52.5,725),text, surface, buttonfont,sbuttshadcol, width, buttonsize)
   startB.drawShadow()
   startB.drawButton()
   startB.drawText()

table = [['','',0] for i in range(tablesize)]

while True:
    events()
    front()
    pygame.display.flip()