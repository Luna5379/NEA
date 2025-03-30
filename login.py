# login.py = login/sign up screens, Grade A skills: hash tables
import csv
import pygame
import sys
import sqlite3

pygame.init()
first = True
tablesize = 17
width = 393
height = 852
bgColour = (22,19,36)
caption = 'login'
surface = screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
surface.fill(color=bgColour)
pygame.display.set_caption(caption)
text = ''
fronty = [True, (119,73,248), (38,32,54), (85,24,214), (318,42), pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18), 'SIGN UP']
login1y = [False, (38,32,54), (189,174,232), (243,241,251), pygame.font.Font('Feather Bold.ttf', 32), 'Create your Profile', 'Email',
            'Password', 'Confirm Password', (45, 98), (62,173), (62, 243), (62, 313), 
            pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 22), (61,55,79), (298,47), '', '', '', False, False, False, False, False, False,
            False, False, False, (119,73,248), (38,32,54), (85,24,214), (318,42), pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18), 'CREATE ACCOUNT']
login2y = [False, (38,32,54), (189,174,232), (243,241,251), pygame.font.Font('Feather Bold.ttf', 32), 'Fill in your details', 'Name', 'Username', 'Gender',
            'Date of Birth', 'Phone Number', (45, 98), (62,173), (62, 243), (62, 313), (62,383), (62,453),  
            pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 22), (61,55,79), (298,47), '', '', '', '', '', False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, (119,73,248), (38,32,54), (85,24,214), (318,42), pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18), 'GET STARTED']

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

def events(text):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        updateTable = open('hashes.csv', 'w', newline='')
        tableWriter = csv.writer(updateTable, delimiter = ',')
        for i in range(len(table)-1):
          print(table[i])
          if table[i] != []:
            print("passed")
            tableWriter.writerow(table[i])
        updateTable.close()
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            if len(text)>0:
                text = text[:-1]
        else:
            text += event.unicode
    return text
    
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
def front():
   surface.fill(color=bgColour)
   startB = buttonNextPage(fronty[1], fronty[2],(52.5,725),fronty[6], surface, fronty[5],fronty[3], width, fronty[4])
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
  l1h = heading(surface, login1y[4], login1y[5], login1y[3], login1y[9])
  l1h.drawText()
  l1b1 = textBox(login1y[1], login1y[2], login1y[10], surface, login1y[13], login1y[14], width, login1y[15])
  l1b1.drawOutline()
  l1b = l1b1.drawBox()
  l1b2 = textBox(login1y[1], login1y[2], login1y[11], surface, login1y[13], login1y[14], width, login1y[15])
  l1b2.drawOutline()
  l2b = l1b2.drawBox()
  l1b3 = textBox(login1y[1], login1y[2], login1y[12], surface, login1y[13], login1y[14], width, login1y[15])
  l1b3.drawOutline()
  l3b = l1b3.drawBox()
  login1y[19] = l1b1.checkClicked(l1b)
  if login1y[19]:
    login1y[22] = True
    login1y[25] = True
    login1y[26] = False
    login1y[27] = False
  if login1y[22]:
    l1b1.drawText(login1y[16])
  else:
    l1b1.drawText(login1y[6])
  login1y[20] = l1b2.checkClicked(l2b)
  if login1y[20]:
    login1y[23] = True
    login1y[25] = False
    login1y[26] = True
    login1y[27] = False
  if login1y[23]:
    ps = ''
    for i in range(len(login1y[17])):
      ps += '*'
    l1b2.drawText(ps)
  else:
    l1b2.drawText(login1y[7])
  login1y[21] = l1b3.checkClicked(l3b)
  if login1y[21]:
    login1y[24] = True
    login1y[25] = False
    login1y[26] = False
    login1y[27] = True
  if login1y[24]:
    ps = ''
    for i in range(len(login1y[18])):
      ps += '*'
    l1b3.drawText(ps)
  else:
    l1b3.drawText(login1y[8])
  startB = buttonNextPage(login1y[28], login1y[29],(52.5,387),login1y[33], surface, login1y[32],login1y[30], width, login1y[31])
  bbs = startB.drawShadow()
  bb = startB.drawButton()
  startB.drawText()
  logo1 = startB.checkClicked(bb,bbs)
  logo2 = False
  if logo1 == False and login1y[17] == login1y[18]:
    logo2 = True
    # cursor.execute("""INSERT INTO TABLEZ (Email, Name, UserName, Gender, DateOfBirth, PhoneNumber)
    #            VALUES ('"""+str(login1y[16])+"""', '', '', '', date('0'), 0);""")
    passw, i = msquare(tablesize, login1y[17])
    table[i] = [i, passw]
    print(table[i])
  #elif login1y[17] != login1y[18]:
    #print("passwords do not match")
  return logo1, logo2

def login2():
  surface.fill(color=bgColour)
  l2h = heading(surface, login2y[4], login2y[5], login2y[3], login2y[11])
  l2h.drawText()
  l2b1 = textBox(login2y[1], login2y[2], login2y[12], surface, login2y[17], login2y[18], width, login2y[19])
  l2b1.drawOutline()
  l1b = l2b1.drawBox()
  l2b2 = textBox(login2y[1], login2y[2], login2y[13], surface, login2y[17], login2y[18], width, login2y[19])
  l2b2.drawOutline()
  l2b = l2b2.drawBox()
  l2b3 = textBox(login2y[1], login2y[2], login2y[14], surface, login2y[17], login2y[18], width, login2y[19])
  l2b3.drawOutline()
  l3b = l2b3.drawBox()
  # login2y[19] = l2b1.checkClicked(l1b)
  # if login2y[19]:
  #   login2y[22] = True
  #   login2y[25] = True
  #   login2y[26] = False
  #   login2y[27] = False
  # if login2y[22]:
  #   l2b1.drawText(login1y[16])
  # else:
  #   l2b1.drawText(login1y[6])
  # login1y[20] = l2b2.checkClicked(l2b)
  # if login1y[20]:
  #   login1y[23] = True
  #   login1y[25] = False
  #   login1y[26] = True
  #   login1y[27] = False
  # if login1y[23]:
  #   l2b2.drawText(login1y[17])
  # else:
  #   l2b2.drawText(login1y[7])
  # login1y[21] = l2b3.checkClicked(l3b)
  # if login1y[21]:
  #   login1y[24] = True
  #   login1y[25] = False
  #   login1y[26] = False
  #   login1y[27] = True
  # if login1y[24]:
  #   l2b3.drawText(login1y[18])
  # else:
  #   l2b3.drawText(login1y[8])

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

while True:
    if first:
      table = hashTable(tablesize)
      first = False
    if login1y[25]:
      login1y[16] = events(login1y[16])
    elif login1y[26]:
      login1y[17] = events(login1y[17])
    elif login1y[27]:
      login1y[18] = events(login1y[18])
    elif login2y[25]:
      login2y[16] = events(login2y[16])
    elif login2y[26]:
      login2y[17] = events(login2y[17])
    elif login2y[27]:
      login2y[18] = events(login2y[18])
    else:
      text = events(text)
    if fronty[0]:
      fronty[0], login1y[0] = front()
    elif login1y[0]:
       login1y[0], login2y[0] = login1()
    elif login2y[0]:
       login2()
       #cursor.execute("""SELECT * FROM TABLEZ ORDER BY Name DESC""") #just for testing x
       #print(cursor.fetchall())
       #connection.commit()
    pygame.display.flip()