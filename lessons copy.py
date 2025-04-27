# lessons.py = lessons timeline + lessons, Grade A skills: Aggregate SQL functions, Complex user-defined algorithms
import pygame
import sqlite3
import sys
import random
import datetime
import math
#def timeline(percentageCompleted):

connection = sqlite3.connect('nea.db')
cursor = connection.cursor()
width = 393
height = 852
bgColour = (22,19,36)
caption = 'lesson'
surface = screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
surface.fill(color=bgColour)
pygame.display.set_caption(caption)
pygame.font.init()
font = pygame.font.Font('Feather Bold.ttf', 16)
finished = False
returnTimeline = True

questionData = {
    "nextQ" : False,
    "selected" : [False,False,False,False],
    "submitted" : True,
    "firstRound" : True,
    "q" : 0,
    "order" : [0,0,0,0]
}

        # order = ['' for i in range(4)]
        # o = random.randint(1,4)
        # for i in range(4):
        #     while o in order:
        #         o = random.randint(1,4)
        #     order[i] = o

#re write with different questions as classes, get question ids outside for the whole lesson, then get the question + answers + all functions in each type of question in the classes
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

class q1: #first type, what does this command do?
    def __init__(self, surface, params, order):
        self.surface = surface
        self.params = params
        self.order = order
        #pass in colour so that it changes based on correct?
    def getQuestion(self):
        cursor.execute("""SELECT Question, Example FROM questions WHERE QuestionID = ?;""",self.params)
        question = cursor.fetchone()
        connection.commit()
        return question[0], question[1]
    def getOptions(self):
        cursor.execute("""SELECT Answer FROM questions WHERE QuestionID = ?;""",self.params)
        answer = cursor.fetchone()
        cursor.execute("""SELECT Option FROM options WHERE QuestionID = ?""",self.params)
        options = cursor.fetchall()
        answerOptions = [options[0][0],options[1][0],options[2][0]]
        connection.commit()
        return answer[0], answerOptions
    def drawQuestion(self, question, example): #print question onto page
        qText = font.render(question, False, (255,0,0))
        qRect = qText.get_rect()
        qRect.topleft = (10, 10)
        self.surface.blit(qText, qRect)
        eText = font.render("eg. " + str(example), False, (0,255,0))
        eRect = eText.get_rect()
        eRect.topleft = (10, 30)
        self.surface.blit(eText, eRect)
    def drawOptions(self, answer, options,selected): #print options onto page
        allOps = [answer, options[0], options[1], options[2]]
        allOpsOrdered = ['' for i in range(4)]
        coords = [[] for i in range(4)]
        for i in range(4):
            allOpsOrdered[i] = allOps[self.order[i]-1]
            coords[i] = [(0 + (i%2)*196.5), (300)]
            if i >1:
                coords[i][1] += 100
            optionBase = ['' for i in range(4)]
            optionText = ['' for i in range(4)]
            optionRect = ['' for i in range(4)]
        for i in range(4):
            if selected[i]:
                shadowBase = pygame.Rect(coords[i][0]-2.5,coords[i][1]-2.5, 201.5, 105)
                pygame.draw.rect(self.surface, (132,132,132), shadowBase, border_radius = 10) 
            optionBase[i] = pygame.Rect(coords[i][0],coords[i][1], 196.5, 100)
            pygame.draw.rect(self.surface, (255,255,255), optionBase[i], border_radius = 10)
            optionText[i] = font.render(str(allOpsOrdered[i]), False, (0,0,255))
            optionRect[i] = optionText[i].get_rect()
            optionRect[i].topleft = (196.5/2 + coords[i][0] - font.size(allOpsOrdered[i])[0]/2, coords[i][1] + (100+3.75-font.size(allOpsOrdered[i])[1])/4)
            self.surface.blit(optionText[i], optionRect[i])
        return optionBase, allOpsOrdered
    def selectOptions(self, optionBase, selected): #check if the user clicked the right answer, show result
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and (optionBase[0].collidepoint(pos) or optionBase[1].collidepoint(pos) or optionBase[2].collidepoint(pos) or optionBase[3].collidepoint(pos)):
            for i in range(len(optionBase)):
                if optionBase[i].collidepoint(pos):
                    selected[i] = True
                    for j in range(len(selected)):
                        if j!=i:
                            selected[j] = False
        return selected

    def resultPopUp(self, selected, optionText, answer):
        for i in range(len(selected)):
           if selected[i]:
              selectedIndex = i
        if optionText[selectedIndex] == answer:
            result = pygame.Rect(37.5,525, 318, 200)
            pygame.draw.rect(self.surface, (0,255,0), result, border_radius = 10)
            wellDone = font.render(str('Correct!'), False, (0,0,255))
            coRect = wellDone.get_rect()
            coRect.topleft = (196.5/2 + 52.5 - font.size('Correct!')[0]/2, 525 + (100+3.75-font.size('Correct!')[1])/4)
            self.surface.blit(wellDone, coRect)
            return True
        else:
            result = pygame.Rect(37.5,525, 318, 200)
            pygame.draw.rect(self.surface, (255,0,0), result, border_radius = 10)
            tough = font.render(str('Incorrect!'), False, (0,0,255))
            incoRect = tough.get_rect()
            incoRect.topleft = (196.5/2 + 52.5 - font.size('Incorrect!')[0]/2, 525 + (100+3.75-font.size('Incorrect!')[1])/4)
            self.surface.blit(tough, incoRect)
            return False
class q2: #second type ...
    pass

def events():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def generateLesson(Topic, Section):
   lessonPercentage =  0
   qlist = []
   cursor.execute("""SELECT MAX(LessonID) FROM lessonQuestions""")
   lastLesson = cursor.fetchone()[0]
   if lastLesson == None:
      currentLesson = 1
   else:
      currentLesson = lastLesson + 1
   cursor.execute("""INSERT INTO lessons VALUES (?,?)""", [currentLesson, None])
   while lessonPercentage < 1:
    param1 = [random.randint(1,30),Topic, Section]
    cursor.execute("""SELECT QuestionID, LessonPercentage, Difficulty FROM questions WHERE QuestionID = ? AND Topic = ? AND Section = ? """, param1)
    qidp = cursor.fetchone()
    if qidp[1] <= (1-lessonPercentage) and qidp[0] not in qlist:
        lessonPercentage += qidp[1]
        qlist.append(qidp[0])
        param2 = [currentLesson, qidp[0], qidp[2], None]
        cursor.execute("""INSERT INTO lessonQuestions VALUES(?,?,?,?)""",param2)
        lessonPercentage = round(lessonPercentage,2)
   cursor.execute("""SELECT SUM(DifficultyGroup) FROM lessonQuestions WHERE LessonID = ?""", [currentLesson])
   totalDifficulty = cursor.fetchone()[0]
   cursor.execute("""UPDATE lessons SET MaxPoints = ? WHERE LessonID = ?""", [totalDifficulty*5, currentLesson])
   return currentLesson

def lesson(currentLesson, finished):
   cursor.execute("""SELECT QuestionID FROM lessonQuestions WHERE LessonID = ? ORDER BY DifficultyGroup""", [currentLesson])
   qlist = []
   for i in cursor.fetchall():
      qlist.append(i[0])
   currentQ = True
   if questionData["firstRound"] == True:
        questionData["nextQ"] = True
        questionData["selected"] = [False,False,False,False]
        questionData["submitted"] = True
        questionData["firstRound"] = False
        questionData["q"] = questionData["q"] + 1
        questionData["order"] = [0,0,0,0]
        i = 4
        positions = [1,2,3,4]
        for j in range(len(questionData["order"])):
            orderidx = random.choice(positions)
            questionData["order"][orderidx-1] = i
            i-=1
            positions.remove(orderidx)
   if questionData["q"] > len(qlist):
      finished = True
      currentQ = False
   if currentQ:
        questionData["selected"], questionData["submitted"], questionData["nextQ"], currentQ = question(questionData["selected"], questionData["submitted"], currentQ, questionData["nextQ"], qlist[questionData["q"]-1], questionData["order"])
   if questionData["nextQ"] == False:
      questionData["firstRound"] = True
   return finished
      

def question(selected,submitted, currentQ, nextQ, questionID, order):
    surface.fill(color=bgColour)
    #while not qComplete: #add somewhere so that program works AFTER ADDING OTHER TYPES OF QUESTIONS
    quest1 = q1(surface, [questionID], order)
    q, ex = quest1.getQuestion()
    quest1.drawQuestion(q,ex)
    ans, ops = quest1.getOptions()
    optionBase, optionText = quest1.drawOptions(ans,ops,selected)
    selected = quest1.selectOptions(optionBase, selected)
    submitButton = buttonNextPage((0,255,0), (0,0,0), (52.5,725), 'SUBMIT', surface, pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18), (120,120,120), width, (318,42))
    sbs = submitButton.drawShadow()
    sb = submitButton.drawButton()
    submitButton.drawText()
    if submitted:
        submitted = submitButton.checkClicked(sb,sbs)
    elif not submitted:
       if True in selected:
        correct = quest1.resultPopUp(selected, optionText, ans)
        if correct:
          buttoncol = (0,255,0)
          params = [1, questionID]
        else:
          buttoncol = (255,0,0)
          params = [0, questionID]
        nextButton = buttonNextPage(buttoncol, (0,0,0), (52.5,725), 'NEXT', surface, pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18), (120,120,120), width, (318,42))
        nbs = nextButton.drawShadow()
        nb = nextButton.drawButton()
        nextButton.drawText()
        nextQ = nextButton.checkClicked(nb,nbs)
        if not nextQ:
          currentQ = False
          cursor.execute("""UPDATE lessonQuestions SET CORRECT = ? WHERE questionID = ?""",params)
    pygame.display.flip()
    return selected, submitted, nextQ, currentQ
def results(lessonID, Username, uploaded):
   dateCompleted = datetime.date.today()
   cursor.execute("""SELECT AVG(Correct) FROM lessonQuestions WHERE LessonID = ?""", [lessonID])
   percentage = round(cursor.fetchone()[0], 2)
   cursor.execute("""SELECT MaxPoints FROM lessons WHERE LessonID = ?""", [lessonID])
   totalPoints = math.floor((percentage)*cursor.fetchone()[0])
   cursor.execute("""SELECT SUM(Correct) FROM lessonQuestions WHERE LessonID = ?""", [lessonID])
   totalCorrect = cursor.fetchone()[0]
   if not uploaded:
    cursor.execute("""INSERT INTO lessonsCompleted VALUES(?,?,?,?,?,?)""", [lessonID, dateCompleted, totalPoints, percentage, totalCorrect, Username])
    uploaded = True
   resultText = ['percentage achieved = ' + str(100*percentage), 'points gained = ' + str(totalPoints)]
   surface.fill(color=bgColour)
   rText1 = font.render(str(resultText[0]), False, (0,0,255))
   rRect1 = rText1.get_rect()
   rRect1.topleft = (10,10)
   surface.blit(rText1, rRect1)
   rText2 = font.render(str(resultText[1]), False, (0,0,255))
   rRect2 = rText2.get_rect()
   rRect2.topleft = (10,30)
   surface.blit(rText2, rRect2)
   timelineButton = buttonNextPage((255,255,0), (0,0,0), (52.5,725), 'RETURN TO TIMELINE', surface, pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18), (140,120,60), width, (318,42))
   tbs = timelineButton.drawShadow()
   tb = timelineButton.drawButton()
   timelineButton.drawText()
   returnTimeline = timelineButton.checkClicked(tb,tbs)
   if not returnTimeline:
    return uploaded, returnTimeline
   else:
      return uploaded, True

Username = 'IBM'
lessonID = generateLesson('Basics', 'Simple Commands')
uploaded = False
while True:
    events()
    if not finished:
       finished = lesson(lessonID, finished)
       connection.commit()
    elif finished and returnTimeline:
       uploaded, returnTimeline = results(lessonID, Username, uploaded)
       pygame.display.flip()
       connection.commit()
    elif not returnTimeline:
       sys.exit()