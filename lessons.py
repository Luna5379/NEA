# lessons.py = lessons timeline + lessons, Grade A skills: Aggregate SQL functions, Complex user-defined algorithms
import pygame
import sqlite3
import sys
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
font = pygame.font.Font('Feather Bold.ttf', 32)

class options:
    def __init__(self, correct, option, surface, order,font):
        self.correct = correct
        self.option = option
        self.surface = surface
        self.order = order
        self.font = font

    def drawOption(self):
        coords = [0,0]
        if self.order % 2 == 0:
            coords[0] = 196.5
        if self.order > 2:
            coords[1] = 30
        optionBase = pygame.Rect(coords[0], coords[1],196.5,30)
        pygame.draw.rect(self.surface,(255,255,255),optionBase, border_radius = 10)
        buttonText = self.font.render(str(self.option), False, (0,0,0))
        buttonRect = buttonText.get_rect()
        buttonRect.topleft = (196.5/2 - self.font.size(self.option)[0]/2, coords[1]+(30+3.75-self.font.size(self.option)[1])/4)
        self.surface.blit(buttonText, buttonRect)
        #return optionBase

    def optionResult():
        pass


def events():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    #   elif event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_BACKSPACE:
    #         if len(text)>0:
    #             text = text[:-1]
    #     else:
    #         text += event.unicode
    # return text

def getQuestion(topic, percentage):
    params = (topic,percentage)
    cursor.execute("""SELECT QuestionID, Question FROM questions WHERE Topic = ? AND LessonPercentage = ?;""",params)
    questions = cursor.fetchone()
    connection.commit()
    return questions[0], questions[1]

def getAnswers(questionID):
    cursor.execute("""SELECT Answer FROM questions WHERE QuestionID = questionID;""")
    answer = cursor.fetchone()
    cursor.execute("""SELECT Option FROM options WHERE QuestionID = questionID""")
    options = cursor.fetchall()
    answerOptions = [options[0][0],options[1][0],options[2][0]]
    connection.commit()
    print(answer)
    print(options)
    return answer[0], answerOptions

def question():
    surface.fill(color=bgColour)
    hi = "hi"
    option1 = options(False, hi, surface, 1,font)
    option1.drawOption()
    option2 = options(False, hi, surface, 2,font)
    option2.drawOption()
    option3 = options(False, hi, surface, 3,font)
    option3.drawOption()
    option4 = options(False, hi, surface, 4,font)
    option4.drawOption()
    pygame.display.flip()
    #startB = buttonNextPage(fronty[1], fronty[2],(52.5,725),fronty[6], surface, fronty[5],fronty[3], width, fronty[4])
    #bbs = startB.drawShadow()
    #bb = startB.drawButton()
    #startB.drawText()
    #fronto = startB.checkClicked(bb,bbs)
    #logo1 = False
    #if fronto == False:
    #    logo1 = True


while True:
    events()
    #questionID, question = getQuestion("Simple Commands", 0.05)
    #answer, options = getAnswers(questionID)
    question()