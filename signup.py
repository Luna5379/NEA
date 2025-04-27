# signup.py = login/sign up screens, Grade A skills: hash tables
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
caption = 'signup'
surface = screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
surface.fill(color=bgColour)
pygame.display.set_caption(caption)
text = ''
hashInterval = 3
fronty = [True, (119,73,248), (38,32,54), (85,24,214), (318,42), pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18), 'SIGN UP']
textBools = {
  "getTextl11" : False,
  "getTextl12" : False,
  "getTextl13" : False,
  "getTextl21" : False,
  "getTextl22" : False,
  "getTextl23" : False,
  "getTextl24" : False,
  "getTextl25" : False,
  "getCode" : False
}
textStrings = {
  "textl11" : '',
  "textl12" : '',
  "textl13" : '',
  "textl21" : '',
  "textl22" : '',
  "textl23" : '',
  "textl24" : '',
  "textl25" : '',
  "ctext" : ''
}
typeCheck = {
   "typel11" : False,
   "typel12" : False,
   "typel13" : False,
   "typel21" : False,
   "typel22" : False,
   "typel23" : False,
   "typel24" : False,
   "typel25" : False,
   "typeC" : False
}
pageBools = {
   "front" : True,
   "signup1" : False,
   "signup2" : False,
   "teacherPage" : True,
   "studentPage" : True,
   "login" : False
}

popUps = {
   "student" : False,
   "teacher" : False
}

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

def hashStore(passw, i):
   if table[i] == []:
      table[i] = [i, passw]
   else:
      while table[i] != []:
         print("yay")
         i += hashInterval
         if i > tablesize:
            i = i % tablesize
      table[i] = [i, passw]
   return i

def events(text):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        updateTable = open('hashes.csv', 'w', newline='')
        tableWriter = csv.writer(updateTable, delimiter = ',')
        for i in range(len(table)-1):
          if table[i] != []:
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
class popUp:
    def __init__(self, popUpColour, surface, font, outline, width, popUpSize, inputColour, codeFont):
        self.popUpColour = popUpColour
        self.surface = surface
        self.font = font
        self.outline = outline
        self.width = width
        self.popUpSize = popUpSize
        self.inputColour = inputColour
        self.codeFont = codeFont
    
    def drawPopUpBase(self):
      popUpBase = pygame.Rect(196.5-self.popUpSize[0]/2, 213+self.popUpSize[1]/4,self.popUpSize[0],self.popUpSize[1])
      pygame.draw.rect(self.surface,self.popUpColour,popUpBase, border_radius = 5)

    def drawPopUpOutline(self):
      outlineBase = pygame.Rect(196.5-self.popUpSize[0]/2-2, 213+self.popUpSize[1]/4-2,self.popUpSize[0]+4,self.popUpSize[1]+4)
      pygame.draw.rect(self.surface,self.outline,outlineBase, border_radius = 5)

    def displayPopUpData(self, text, position):
      if position == None:
        popText = self.font.render(str(text), False, self.outline)
        popRect = popText.get_rect()
        popRect.topleft = (196.5-self.popUpSize[0]/2+3, 213+self.popUpSize[1]/4+6)
        self.surface.blit(popText, popRect)
      else:
        popText = self.font.render(str(text), False, self.outline)
        popRect = popText.get_rect()
        popRect.topleft = (196.5-self.popUpSize[0]/2+3, 213+self.popUpSize[1]/4+6+35*(position-1))
        self.surface.blit(popText, popRect)

    def userInput(self, code):
      outline1 = pygame.Rect(196.5-self.popUpSize[0]/2+22.5, 213+self.popUpSize[1]/4+77.5,70,125)
      pygame.draw.rect(self.surface,self.outline,outline1,border_radius = 5)
      outline2 = pygame.Rect(196.5-self.popUpSize[0]/2+97.5, 213+self.popUpSize[1]/4+77.5,70,125)
      pygame.draw.rect(self.surface,self.outline,outline2,border_radius = 5)
      outline3 = pygame.Rect(196.5-self.popUpSize[0]/2+172.5, 213+self.popUpSize[1]/4+77.5,70,125)
      pygame.draw.rect(self.surface,self.outline,outline3,border_radius = 5)
      outline4 = pygame.Rect(196.5-self.popUpSize[0]/2+247.5, 213+self.popUpSize[1]/4+77.5,70,125)
      pygame.draw.rect(self.surface,self.outline,outline4,border_radius = 5)
      box1 = pygame.Rect(196.5-self.popUpSize[0]/2+25, 213+self.popUpSize[1]/4+80,65,120)
      pygame.draw.rect(self.surface,self.inputColour,box1,border_radius = 5)
      box2 = pygame.Rect(196.5-self.popUpSize[0]/2+100, 213+self.popUpSize[1]/4+80,65,120)
      pygame.draw.rect(self.surface,self.inputColour,box2,border_radius = 5)
      box3 = pygame.Rect(196.5-self.popUpSize[0]/2+175, 213+self.popUpSize[1]/4+80,65,120)
      pygame.draw.rect(self.surface,self.inputColour,box3,border_radius = 5)
      box4 = pygame.Rect(196.5-self.popUpSize[0]/2+250, 213+self.popUpSize[1]/4+80,65,120)
      pygame.draw.rect(self.surface,self.inputColour,box4,border_radius = 5)
      code1 = self.codeFont.render(str(code[0]), False, self.outline)
      c1Rect = code1.get_rect()
      c1Rect.topleft = (196.5-self.popUpSize[0]/2+30, 213+self.popUpSize[1]/4+100)
      self.surface.blit(code1, c1Rect)
      code2 = self.codeFont.render(str(code[1]), False, self.outline)
      c2Rect = code2.get_rect()
      c2Rect.topleft = (196.5-self.popUpSize[0]/2+105, 213+self.popUpSize[1]/4+100)
      self.surface.blit(code2, c2Rect)
      code3 = self.codeFont.render(str(code[2]), False, self.outline)
      c3Rect = code3.get_rect()
      c3Rect.topleft = (196.5-self.popUpSize[0]/2+180, 213+self.popUpSize[1]/4+100)
      self.surface.blit(code3, c3Rect)
      code4 = self.codeFont.render(str(code[3]), False, self.outline)
      c4Rect = code4.get_rect()
      c4Rect.topleft = (196.5-self.popUpSize[0]/2+255, 213+self.popUpSize[1]/4+100)
      self.surface.blit(code4, c4Rect)

    def closePopUp(self): ########### if time left
       pass
def front():
   surface.fill(color=bgColour)
   startB = buttonNextPage(fronty[1], fronty[2],(52.5,665),fronty[6], surface, fronty[5],fronty[3], width, fronty[4])
   bbs = startB.drawShadow()
   bb = startB.drawButton()
   startB.drawText()
   logB = buttonNextPage(fronty[1], fronty[2],(52.5,725),'LOG IN', surface, fronty[5],fronty[3], width, fronty[4])
   lbs = logB.drawShadow()
   lb = logB.drawButton()
   logB.drawText()
   fronto1 = startB.checkClicked(bb,bbs)
   fronto2 = logB.checkClicked(lb,lbs)
   signo1 = False
   logo1 = False
   if fronto1 == False:
      signo1 = True
      return fronto1, signo1, logo1
   elif fronto2 == False:
      logo1 = True
      return fronto2, signo1, logo1
   else:
      return True, signo1, logo1

def signup1():
   surface.fill(color=bgColour)
   l1h = heading(surface, pygame.font.Font('Feather Bold.ttf', 32), 'Create your profile', (243,241,251), (45,98))
   l1h.drawText()
   l1b1 = textBox((38,32,54),(189,174,232),(62,173),surface,pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 22), (61,55,79), width, (298,47))
   l1b1.drawOutline()
   l1b = l1b1.drawBox()
   l1b2 = textBox((38,32,54), (189,174,232), (62,243), surface, pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 22), (61,55,79), width, (298,47))
   l1b2.drawOutline()
   l2b = l1b2.drawBox()
   l1b3 = textBox((38,32,54), (189,174,232), (62,313), surface, pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 22), (61,55,79), width, (298,47))
   l1b3.drawOutline()
   l3b = l1b3.drawBox()
   click1 = l1b1.checkClicked(l1b)
   if click1:
     typeCheck['typel11'] = True
     textBools['getTextl11'] = True
     textBools['getTextl12'] = False
     textBools['getTextl13'] = False
   if typeCheck['typel11']:
        l1b1.drawText(textStrings['textl11'])
   else:
        l1b1.drawText('Username')
     
   click2 = l1b2.checkClicked(l2b)
   if click2:
     typeCheck['typel12'] = True
     textBools['getTextl11'] = False
     textBools['getTextl12'] = True
     textBools['getTextl13'] = False
   if typeCheck['typel12']:
     ps = ''
     for i in range(len(textStrings['textl12'])):
         ps += '*'
     l1b2.drawText(ps)
   else:
     l1b2.drawText('Password')
   click3 = l1b3.checkClicked(l3b)
   if click3:
     typeCheck['typel13'] = True
     textBools['getTextl11'] = False
     textBools['getTextl12'] = False
     textBools['getTextl13'] = True
   if typeCheck['typel13']:
        ps = ''
        for i in range(len(textStrings['textl13'])):
            ps += '*'
        l1b3.drawText(ps)
   else:
     l1b3.drawText('Confirm Password')
   startB = buttonNextPage((119,73,248), (38,32,54), (52.5,387), 'CREATE ACCOUNT', surface, pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18), (85,24,214), width, (318,42))
   bbs = startB.drawShadow()
   bb = startB.drawButton()
   startB.drawText()
   logo1 = startB.checkClicked(bb,bbs)
   logo2 = False
   if logo1 == False and textStrings['textl12'] == textStrings['textl13']:
      logo2 = True
      passw, i = msquare(tablesize, textStrings['textl12']) # COLLISIONS
      i = hashStore(passw, i)
      params = [str(textStrings['textl11']),None,None,None,None,None,i,None,None]#try except for exception handling usernames must be different
      cursor.execute("""INSERT INTO profile
                    VALUES (?,?,?,?,?,?,?,?,?)""",params)
   return logo1, logo2

def signup2():
    textBools['getTextl11'] = False
    textBools['getTextl12'] = False
    textBools['getTextl13'] = False
    surface.fill(color=bgColour)
    l2h = heading(surface, pygame.font.Font('Feather Bold.ttf', 32), 'Fill in your details', (243,241,251), (45,98))
    l2h.drawText()
    l2b1 = textBox((38,32,54),(189,174,232),(62,173),surface,pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 22), (61,55,79), width, (298,47))
    l2b1.drawOutline()
    l21b = l2b1.drawBox()
    l2b2 = textBox((38,32,54), (189,174,232), (62,243), surface, pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 22), (61,55,79), width, (298,47))
    l2b2.drawOutline()
    l22b = l2b2.drawBox()
    l2b3 = textBox((38,32,54), (189,174,232), (62,313), surface, pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 22), (61,55,79), width, (298,47))
    l2b3.drawOutline()
    l23b = l2b3.drawBox()
    l2b4 = textBox((38,32,54), (189,174,232), (62,383), surface, pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 22), (61,55,79), width, (298,47))
    l2b4.drawOutline()
    l24b = l2b4.drawBox()
    l2b5 = textBox((38,32,54), (189,174,232), (62,453), surface, pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 22), (61,55,79), width, (298,47))
    l2b5.drawOutline()
    l25b = l2b5.drawBox()
    click1 = l2b1.checkClicked(l21b)
    if click1:
        typeCheck['typel21'] = True
        textBools['getTextl21'] = True
        textBools['getTextl22'] = False
        textBools['getTextl23'] = False
    if typeCheck['typel21']:
            l2b1.drawText(textStrings['textl21'])
    else:
            l2b1.drawText('Name')
        
    click2 = l2b2.checkClicked(l22b)
    if click2:
        typeCheck['typel22'] = True
        textBools['getTextl21'] = False
        textBools['getTextl22'] = True
        textBools['getTextl23'] = False
    if typeCheck['typel22']:
        l2b2.drawText(textStrings['textl22'])
    else:
        l2b2.drawText('Email')
    click3 = l2b3.checkClicked(l23b)
    if click3:
        typeCheck['typel23'] = True
        textBools['getTextl21'] = False
        textBools['getTextl22'] = False
        textBools['getTextl23'] = True
    if typeCheck['typel23']:
        l2b3.drawText(textStrings['textl23'])
    else:
        l2b3.drawText('Gender')
    click4 = l2b4.checkClicked(l24b)
    if click4:
        typeCheck['typel24'] = True
        textBools['getTextl21'] = False
        textBools['getTextl22'] = False
        textBools['getTextl23'] = False
        textBools['getTextl24'] = True
        textBools['getTextl25'] = False
    if typeCheck['typel24']:
        l2b4.drawText(textStrings['textl24'])
    else:
        l2b4.drawText('Date of Birth')
    click5 = l2b5.checkClicked(l25b)
    if click5:
        typeCheck['typel25'] = True
        textBools['getTextl21'] = False
        textBools['getTextl22'] = False
        textBools['getTextl23'] = False
        textBools['getTextl24'] = False
        textBools['getTextl25'] = True
    if typeCheck['typel25']:
        l2b5.drawText(textStrings['textl25'])
    else:
        l2b5.drawText('Phone Number')
    studentB = buttonNextPage((119,73,248), (38,32,54), (52.5,527), 'JOIN A CLASSROOM', surface, pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18), (85,24,214), width, (318,42))
    sbs = studentB.drawShadow()
    sb = studentB.drawButton()
    studentB.drawText()
    teacherB = buttonNextPage((119,73,248), (38,32,54), (52.5,587), 'ARE YOU A TEACHER?', surface, pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18), (85,24,214), width, (318,42))
    tbs = teacherB.drawShadow()
    tb = teacherB.drawButton()
    teacherB.drawText()
    studentPage = studentB.checkClicked(sb,sbs)
    teacherPage = teacherB.checkClicked(tb,tbs)
    if teacherPage == False:
       popUps['teacher'] = True
    elif studentPage == False:
       popUps['student'] = True
    if popUps['teacher']:
       cursor.execute("""SELECT MAX(ClassroomCode) FROM profile WHERE Teacher = 1""") #where teacher = 1 can be removed when exceptions are handled
       codey = cursor.fetchone()
       if codey[0] == None:
          codeInt = 0
       else:
        codeInt = codey[0] +1
       code = str(codeInt)
       while len(code) < 4:
          code = '0' + code
       teacherCodePopUp = popUp(bgColour, surface, pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 24), (189,174,232), width, (343.875,266.25), (38,32,54), pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 96))
       teacherCodePopUp.drawPopUpOutline()
       teacherCodePopUp.drawPopUpBase()
       teacherCodePopUp.displayPopUpData("Find your classroom code below!", None)
       teacherCodePopUp.userInput(code)
       teachercB = buttonNextPage((119,73,248), (38,32,54), (52.5,495), 'CONTINUE', surface, pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18), (85,24,214), width, (318,42))
       tcbs = teachercB.drawShadow()
       tcb = teachercB.drawButton()
       teachercB.drawText()
       teacherSubmit = teachercB.checkClicked(tcb,tcbs)
       if not teacherSubmit:
          params = [str(textStrings['textl21']),str(textStrings['textl22']),str(textStrings['textl23']),str(textStrings['textl24']),int(textStrings['textl25']), int(1), int(code),str(textStrings['textl11'])]
          cursor.execute("""UPDATE profile
                                    SET Name = ?, Email = ?, Gender = ?, DateOfBirth = ?, Phone = ?, Teacher = ?, ClassroomCode = ?
                                    WHERE Username = ?;""",params)
          logo2 = False
          return logo2, teacherSubmit, True
       else:
          return True, True, True
    elif popUps['student']:
       studentCodePopUp = popUp(bgColour, surface, pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 22), (189,174,232), width, (343.875,266.25), (38,32,54), pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 96))
       studentCodePopUp.drawPopUpOutline()
       studentCodePopUp.drawPopUpBase()
       studentCodePopUp.displayPopUpData("Enter your classroom code below!", 1)
       studentCodePopUp.displayPopUpData("If you don't have a classroom", 2)
       studentCodePopUp.displayPopUpData("Enter 0000", 3)
       codeBox = textBox((38,32,54), (189,174,232), (62.0625,393.3125), surface, pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 80), (61,55,79), width, (298,80))
       codeBox.drawOutline()
       cb = codeBox.drawBox()
       clickC = codeBox.checkClicked(cb)
       if clickC:
          typeCheck['typeC'] = True
          textBools['getTextl21'] = False
          textBools['getTextl22'] = False
          textBools['getTextl23'] = False
          textBools['getTextl24'] = False
          textBools['getTextl25'] = False
          textBools['getCode'] = True
       if typeCheck['typeC']:
          codeBox.drawText(textStrings['ctext'])
       studentcB = buttonNextPage((119,73,248), (38,32,54), (52.5,495), 'CONTINUE', surface, pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18), (85,24,214), width, (318,42))
       scbs = studentcB.drawShadow()
       scb = studentcB.drawButton()
       studentcB.drawText()
       studentSubmit = studentcB.checkClicked(scb,scbs)
        #make student input pop up - timeline
       if not studentSubmit:
        params = [str(textStrings['textl21']),str(textStrings['textl22']),str(textStrings['textl23']),str(textStrings['textl24']),str(textStrings['textl25']), int(0), int(str(textStrings['ctext'])),str(textStrings['textl11'])]
        cursor.execute("""UPDATE profile
                                  SET Name = ?, Email = ?, Gender = ?, DateOfBirth = ?, Phone = ?, Teacher = ?, ClassroomCode = ?
                                  WHERE Username = ?;""",params)
        logo2 = False
        return logo2, True, studentSubmit
       else:
        return True, True, True
    else:
       return True, True, True

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
    if textBools['getTextl11']:
        textStrings['textl11'] = events(textStrings['textl11'])
    elif textBools['getTextl12']:
        textStrings['textl12'] = events(textStrings['textl12'])
    elif textBools['getTextl13']:
        textStrings['textl13'] = events(textStrings['textl13'])
    elif textBools['getTextl21']:
        textStrings['textl21'] = events(textStrings['textl21'])
    elif textBools['getTextl22']:
        textStrings['textl22'] = events(textStrings['textl22'])
    elif textBools['getTextl23']:
        textStrings['textl23'] = events(textStrings['textl23'])
    elif textBools['getTextl24']:
        textStrings['textl24'] = events(textStrings['textl24'])
    elif textBools['getTextl25']:
        textStrings['textl25'] = events(textStrings['textl25'])
    elif textBools['getCode']:
        textStrings['ctext'] = events(textStrings['ctext'])
    else:
        text = events(text)
    if pageBools['front']:
        pageBools['front'], pageBools['signup1'], pageBools['login'] = front()
    elif pageBools['signup1']:
        pageBools['signup1'], pageBools['signup2'] = signup1()
    elif pageBools['signup2']:
      pageBools['signup2'], pageBools['teacherPage'], pageBools['studentPage'] = signup2()
    pygame.display.flip()
    connection.commit()