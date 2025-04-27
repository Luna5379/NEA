# login.py = login/sign up screens, Grade A skills: hash tables
import csv
import pygame
import sys
import sqlite3

pygame.init()
connection = sqlite3.connect('nea.db')
cursor = connection.cursor()
first = True
tablesize = 151
width = 393
height = 852
bgColour = (22,19,36)
caption = 'login'
surface = screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
surface.fill(color=bgColour)
pygame.display.set_caption(caption)
text = ''
logo = True
hashInterval = 3

textBools = {
   "getUser" : False,
   "getPass" : False
}
textStrings = {
   "username" : '',
   "password" : ''
}
typeCheck = {
   "typeUser" : False,
   "typePass" : False
}

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
  def __init__(self, boxColour, colour, coords, surface, font, outline, width, buttonsize):
    self.boxColour = boxColour
    self.colour = colour
    self.coords = coords
    self.surface = surface
    self.font = font
    self.outline = outline
    self.width = width
    self.buttonsize = buttonsize
  
  def drawBox(self):
    buttonBase = pygame.Rect(self.coords[0]-15, self.coords[1]-3.75,self.buttonsize[0],self.buttonsize[1])
    pygame.draw.rect(self.surface,self.boxColour,buttonBase, border_radius = 5)
    return buttonBase
  
  def drawText(self,text):
    buttonText = self.font.render(str(text), False, self.colour)
    buttonRect = buttonText.get_rect()
    buttonRect.topleft = (self.coords[0]-7.5, self.coords[1]+6)
    self.surface.blit(buttonText, buttonRect)

  def drawOutline(self):
    buttonBase = pygame.Rect(self.coords[0]-17.25, self.coords[1]-7,self.buttonsize[0]+5,self.buttonsize[1]+5)
    pygame.draw.rect(self.surface,self.outline,buttonBase, border_radius = 5)
  
  def checkClicked(self,buttonBase):
    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] and buttonBase.collidepoint(pos):
      typing = True
      return typing 
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
def events(text):
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
    return text
def encrypt(text): #should i do this before the hashing or after the hashing?
  coded = ''
  for i in range(len(text)):
    coded += chr(ord(text[i]) + 1)
  return coded

def msquare(tablesize, text): #exception handling: make it so you can't just enter, maybe have password length rules? if not make sure final index is at least 4 characters long
  passw = encrypt(text)
  hash = ''
  square = ''
  tableindex = 0
  for j in passw:
    hash += str(ord(j))
  square = str(int(hash) * int(hash))
  square = square[len(square)//2:(len(square)//2)+4]
  tableindex = (int(square))%tablesize
  return(passw, tableindex)
def hashTable(tablesize):
  table = [[] for i in range(tablesize)]
  tableCSV = open('hashes.csv', 'r')
  csvReader = csv.reader(tableCSV, delimiter= ',')
  for row in csvReader:
     idx = row[0]
     passy = row[1]
     idx = int(idx)
     table[idx] = [idx,passy]
  tableCSV.close()
  return table
def match(i, passw):
   inTable = False
   checked = False
   original = i
   if table[i] == [i, passw]:
      inTable = True
   while not inTable and not checked:
      i += hashInterval
      if table[i] == [i, passw]:
        inTable = True
      if i == original:
         checked = True
   if inTable:
      return inTable, i
   else:
      return not checked, i
def login():
   loggedin = False
   surface.fill(color=bgColour)
   welcome = heading(surface, pygame.font.Font('Feather Bold.ttf', 32), 'Welcome Back', (243,241,251), (45,98))
   welcome.drawText()
   usernameBox = textBox((38,32,54),(189,174,232),(62,173),surface,pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 22), (61,55,79), width, (298,47))
   usernameBox.drawOutline()
   uB = usernameBox.drawBox()
   passwordBox = textBox((38,32,54), (189,174,232), (62,243), surface, pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 22), (61,55,79), width, (298,47))
   passwordBox.drawOutline()
   pB = passwordBox.drawBox()
   click1 = usernameBox.checkClicked(uB)
   if click1:
     typeCheck['typeUser'] = True
     textBools['getUser'] = True
     textBools['getPass'] = False
   if typeCheck['typeUser']:
        usernameBox.drawText(textStrings['username'])
   else:
        usernameBox.drawText('Username')
     
   click2 = passwordBox.checkClicked(pB)
   if click2:
     typeCheck['typePass'] = True
     textBools['getUser'] = False
     textBools['getPass'] = True
   if typeCheck['typePass']:
     ps = ''
     for i in range(len(textStrings['password'])):
         ps += '*'
     passwordBox.drawText(ps)
   else:
     passwordBox.drawText('Password')
   startB = buttonNextPage((119,73,248), (38,32,54), (52.5,317), 'CONTINUE', surface, pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18), (85,24,214), width, (318,42))
   bbs = startB.drawShadow()
   bb = startB.drawButton()
   startB.drawText()
   logo = startB.checkClicked(bb,bbs)
   if logo == False:
      passw, i = msquare(tablesize, textStrings['password'])
      params = [str(textStrings['username'])]
      cursor.execute("""SELECT Hash FROM profile WHERE Username = ?""", params)
      hashy = cursor.fetchone()
      hasho = hashy[0]
      matching, i = match(i, passw)
      if matching and i == hasho: #doesnt work if exact same password
         loggedin = True
   return logo, loggedin

while True:
    if first:
      table = hashTable(tablesize)
      first = False
    if textBools['getUser']:
        textStrings['username'] = events(textStrings['username'])
    elif textBools['getPass']:
        textStrings['password'] = events(textStrings['password'])
    else:
        text = events(text)
    if logo:
      logo, loggedin = login()
    if loggedin:
       print("yay")
    pygame.display.flip()
    connection.commit()