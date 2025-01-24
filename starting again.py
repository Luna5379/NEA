import pygame
import sys
import sqlite3

pygame.init()
tablesize = 17
width = 393
height = 852
bgColour = (22,19,36)
caption = 'login'
surface = screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
surface.fill(color=bgColour)
pygame.display.set_caption(caption)
fronty = True
login1y = False

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
    buttonRect.topleft = (self.width/2 - self.font.size(self.text)[0]/2, self.coords[1]+(self.buttonsize[1]+3.75-self.font.size(self.text)[1])/4)
    self.surface.blit(buttonText, buttonRect)
  
  def drawButton(self):
    buttonBase = pygame.Rect(self.coords[0]-15, self.coords[1]-3.75,self.buttonsize[0],self.buttonsize[1])
    pygame.draw.rect(self.surface,self.boxcolour,buttonBase, border_radius = 10)
    return buttonBase

  def drawShadow(self):
    buttonBaseShad = pygame.Rect(self.coords[0]-15, self.coords[1]+3.75,self.buttonsize[0],self.buttonsize[1])
    pygame.draw.rect(self.surface,self.boxshadcolour,buttonBaseShad, border_radius = 10)
    return buttonBaseShad

  def checkClicked(self,buttonBase,buttonBaseShad):
    pos = pygame.mouse.get_pos()
    click = True
    if pygame.mouse.get_pressed()[0] and (buttonBase.collidepoint(pos) or buttonBaseShad.collidepoint(pos)):
       click = False
    return click

class heading:
  def __init__(self, surface, font, text, colour, coords):
      self.surface = surface
      self.font = font
      self.text = text
      self.colour = colour
      self.coords = coords

  def drawText(self):
      headingText = self.font.render(str(self.text), False, self.colour)
      headingRect = headingText.get_rect()
      headingRect.topleft = (self.coords[0],self.coords[1])
      self.surface.blit(headingText, headingRect)

class textBox:
    def __init__(self, boxColour, colour, text, coords, surface, font, outline, width, buttonsize):
      self.boxColour = boxColour
      self.colour = colour
      self.text = text
      self.coords = coords
      self.surface = surface
      self.font = font
      self.outline = outline
      self.width = width
      self.buttonsize = buttonsize
    
    def drawBox():
      pass
    
    def drawInitialText():
      pass
    
    def drawText():
       pass
    
    def drawOutline():
       pass
      
def front():
   surface.fill(color=bgColour)
   sbuttcol = (119,73,248)
   sbutttextcol = (38,32,54)
   sbuttshadcol = (85,24,214)
   buttonsize = (318,42)
   buttonfont = pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18)
   text = 'SIGN UP'
   startB = buttonNextPage(sbuttcol, sbutttextcol,(52.5,725),text, surface, buttonfont,sbuttshadcol, width, buttonsize)
   bbs = startB.drawShadow()
   bb = startB.drawButton()
   startB.drawText()
   fronto = startB.checkClicked(bb,bbs)
   logo1 = False
   if fronto == False:
      logo1 = True
   return fronto, logo1

def login1():
  surface.fill(color=bgColour)
  emptyTextBoxColour = (38,32,54)
  emptyTextColour = (189,174,232)
  headingColour = (243,241,251)
  headingFont = pygame.font.Font('Feather Bold.ttf', 32)
  text = 'Create your Profile'
  coords = (42, 40)
  l1h = heading(surface, headingFont, text, headingColour, coords)
  l1h.drawText()
  
table = [['','',0] for i in range(tablesize)]

while True:
    events()
    if fronty:
      fronty, login1y = front()
    elif login1y:
       login1()
    pygame.display.flip()