import pygame
import sqlite3
import sys
import math

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
topicColours = [(0,0,255), (255,0,0), (0,255,0), (255,255,0), (0,255,255), (255,0,255)]


class header:
    def __init__(self, languages):
        self.languages = languages
    def drawHeader(self):
        pass
    def drawLanguages(self):
        pass
class section:
    def __init__(self, sectionName, sectionColour, font, surface):
        self.sectionName = sectionName
        self.sectionColour = sectionColour
        self.font = font
        self.surface = surface
    def drawSection(self):
        surface.fill(self.sectionColour)
    def drawHeading(self):
        sectionText = self.font.render(str(self.sectionName), False, (0,0,0))
        sectionRect = sectionText.get_rect()
        sectionRect.topleft = (52.5,142)
        self.surface.blit(sectionText, sectionRect)
    def changeSection(self): #circular queue for sections
        pygame.draw.circle(self.surface, (0,0,0),(340.5,725),10)
        arrowText = self.font.render(str('↓'), False, (255,255,255))
        arrowRect = arrowText.get_rect()
        arrowRect.center = (340.5,725)
        self.surface.blit(arrowText, arrowRect)
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and pos == (340.5,725):
            next = True
        else:
            next = False
        return next
class topic:
    def __init__(self, topicName, topicNumber, lessons, completed, coords, topicColour, surface, font1, font2):
        self.topicName = topicName
        self.topicNumber = topicNumber
        self.lessons = lessons
        self.completed = completed
        self.coords = coords
        self.topicColour = topicColour
        self.surface = surface
        self.font1 = font1
        self.font2 = font2
    def drawTopic(self):
        topicBase = pygame.Rect(self.coords[0], self.coords[1],150,150)
        pygame.draw.rect(self.surface,self.topicColour,topicBase, border_radius = 100)
        iconText = self.font1.render(str(self.topicNumber), False, (255,255,255))
        iconRect = iconText.get_rect()
        iconRect.center = (self.coords[0]+75, self.coords[1]+75)
        self.surface.blit(iconText, iconRect)
        return topicBase
    def topicPopUp(self, topicBase, selected, startLesson):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and topicBase.collidepoint(pos):
            selected = True
        if selected == True:
            tPop = pygame.Rect(self.coords[0]+155, self.coords[1], 180, 150)
            pygame.draw.rect(self.surface,self.topicColour,tPop, border_radius = 5)
            headText = self.font2.render(str(self.topicNumber) + ': ' + str(self.topicName), False, (0,0,0))
            headRect = headText.get_rect()
            headRect.topleft = (self.coords[0]+170, self.coords[1]+20)
            self.surface.blit(headText, headRect)
            subText = self.font2.render(str(self.completed) + '/' + str(self.lessons), False, (0,0,0))
            subRect = subText.get_rect()
            subRect.topleft = (self.coords[0]+170, self.coords[1]+40)
            self.surface.blit(subText, subRect)
            lessonBase = pygame.Rect(self.coords[0]+170, self.coords[1]+100,160,30)
            pygame.draw.rect(self.surface,(255,255,255),lessonBase, border_radius = 10)
            lessonText = self.font2.render(str('START LESSON'), False, (0,0,0))
            lessonRect = lessonText.get_rect()
            lessonRect.topleft = (self.coords[0]+190, self.coords[1]+110)
            self.surface.blit(lessonText, lessonRect)
            pos2 = pygame.mouse.get_pos()
            click = True
            if pygame.mouse.get_pressed()[0] and (lessonBase.collidepoint(pos2)):
                startLesson = True
        return selected, startLesson

    def fillTopic(self): #draw bigger circle below topic circle, fill with sector 
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
def getTopics():
    cursor.execute("""SELECT Topic FROM topics""")
    topics = []
    for i in cursor.fetchall():
        topics.append([i[0],False])
    return topics


def displayTopic(topicName, selected, startLesson):
    cursor.execute("""SELECT Position FROM topics WHERE Topic = ?""", [topicName])
    index = cursor.fetchone()[0]
    cursor.execute("""SELECT COUNT(Question) FROM questions WHERE Topic = ?""", [topicName])
    lessonNumber = math.floor(cursor.fetchone()[0]/10)
    cursor.execute("""SELECT COUNT(lessons.LessonID) FROM lessons, lessonQuestions, questions WHERE lessons.LessonID = lessonQuestions.LessonID AND lessonQuestions.QuestionID = questions.QuestionID AND questions.Topic = ?""", [topicName])
    completed = cursor.fetchone()[0]
    indexMod = index % len(topicColours)
    currentTopic = topic(topicName, index, lessonNumber, completed, (20, index*102 + (index-1)*70), topicColours[indexMod], surface, pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 64), pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 14))
    currentBase = currentTopic.drawTopic()
    selected, startLesson = currentTopic.topicPopUp(currentBase, selected, startLesson)
    return selected, startLesson
def displayTimeline(topicList, startLesson):
    surface.fill(color=bgColour)
    for i in range(len(topicList)):
        topicList[i][1], startLesson = displayTopic(topicList[i][0], topicList[i][1], startLesson)
    return topicList, startLesson
topicList = getTopics()
startLesson = False
while True:
    events()
    if not startLesson:
        topicList, startLesson = displayTimeline(topicList, startLesson)
    else:
        print("yay") #START LESSON
    pygame.display.flip()
