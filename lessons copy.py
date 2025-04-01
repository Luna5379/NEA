# lessons.py = lessons timeline + lessons, Grade A skills: Aggregate SQL functions, Complex user-defined algorithms
import pygame
import sqlite3
import sys
import random
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

        # order = ['' for i in range(4)]
        # o = random.randint(1,4)
        # for i in range(4):
        #     while o in order:
        #         o = random.randint(1,4)
        #     order[i] = o

#re write with different questions as classes, get question ids outside for the whole lesson, then get the question + answers + all functions in each type of question in the classes
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
    def drawOptions(self, answer, options): #print options onto page
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
            optionBase[i] = pygame.Rect(coords[i][0],coords[i][1], 196.5, 100)
            pygame.draw.rect(self.surface, (255,255,255), optionBase[i], border_radius = 10)
            optionText[i] = font.render(str(allOpsOrdered[i]), False, (0,0,255))
            optionRect[i] = optionText[i].get_rect()
            optionRect[i].topleft = (196.5/2 + coords[i][0] - font.size(allOpsOrdered[i])[0]/2, coords[i][1] + (100+3.75-font.size(allOpsOrdered[i])[1])/4)
            self.surface.blit(optionText[i], optionRect[i])
        return optionBase
    def checkCorrect(self, optionBase): #check if the user clicked the right answer, show result
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and (optionBase[0].collidepoint(pos) or optionBase[1].collidepoint(pos) or optionBase[2].collidepoint(pos) or optionBase[3].collidepoint(pos)):
            if optionBase[self.order[0]-1].collidepoint(pos):
                correctText = font.render("correct", False, (0,255,0))
            else:
                correctText = font.render("incorrect", False, (255,0,0))
            correctRect = correctText.get_rect()
            correctRect.topleft = (0, 700)
            self.surface.blit(correctText, correctRect)
            return True
        else:
            return False
class q2: #second type ...
    pass

def events():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def question():
    surface.fill(color=bgColour)
    while not qComplete: #add somewhere so that program works AFTER ADDING OTHER TYPES OF QUESTIONS
        quest1 = q1(surface, (1,), [3,2,1,4])
        q, ex = quest1.getQuestion()
        quest1.drawQuestion(q,ex)
        ans, ops = quest1.getOptions()
        optionBase = quest1.drawOptions(ans,ops)
        qComplete = quest1.checkCorrect(optionBase)
        pygame.display.flip()
while True:
    events()
    question()