# teacher.py = teacher statistics + import of csv files for accounts, Grade A skills: Cross-Table parameterised SQL
import pygame
import sys
import sqlite3
import math
import csv
import os

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
code = '0000'
headingFont = pygame.font.Font('Feather Bold.ttf', 30)
existingCSVFiles = ['hashes.csv', 'options.csv', 'questions unfinished.csv', 'questions.csv']

def events():
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        # updateTable = open('hashes.csv', 'w', newline='')
        # tableWriter = csv.writer(updateTable, delimiter = ',')
        # for i in range(len(table)-1):
        #   if table[i] != []:
        #     tableWriter.writerow(table[i])
        # updateTable.close()
        pygame.quit()
        sys.exit()
    #   elif event.type == pygame.KEYDOWN:
    #     if event.key == pygame.K_BACKSPACE:
    #         if len(text)>0:
    #             text = text[:-1]
    #     else:
    #         text += event.unicode
    # return text

class table: #display table design with each column etc.
    def __init__(self, values, columns, font, surface):
        self.values = values
        self.columns = columns
        self.font = font
        self.surface = surface
    def drawTable(self):
        columns = len(self.columns)
        splits = width / (columns)
        col = ['' for i in range(columns)]
        for j in range(len(col)):
            col[j] = pygame.Rect(splits*(j+1), 50, 1.5,700)
            pygame.draw.rect(self.surface, (255,255,255), col[j])
            if '\n' not in self.columns[j]:
                colText = self.font.render(str(self.columns[j]), False, (255,255,255))
                colRect = colText.get_rect()
                colRect.topleft = (splits*j + 2, 50)
                self.surface.blit(colText, colRect)
            else:
                split = self.columns[j].split('\n')
                colText1 = self.font.render(str(split[0]), False, (255,255,255))
                colRect1 = colText1.get_rect()
                colRect1.topleft = (splits*j + 2, 50)
                self.surface.blit(colText1, colRect1)
                colText2 = self.font.render(str(split[1]), False, (255,255,255))
                colRect2 = colText2.get_rect()
                colRect2.topleft = (splits*j + 2, 62)
                self.surface.blit(colText2, colRect2)
        firstRow = pygame.Rect(0, 78, width, 3)
        pygame.draw.rect(self.surface, (255,255,255), firstRow)
    def fillTable(self):
        rows = len(self.values) -1
        splits = width / len(self.columns)
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                valueText = self.font.render(str(self.values[i][j]), False, (255,255,255))
                valueRect = valueText.get_rect()
                valueRect.topleft = (splits*j + 2, 82 + 15*(i))
                self.surface.blit(valueText, valueRect)
        row = [''for i in range(rows)]
        for z in range(rows):
            row[z] = pygame.Rect(0, 82+14*(z+1), width, 1.5)
            pygame.draw.rect(self.surface, (255,255,255), row[z])
    def changeOrder(): #optional
        pass
def importData(importing): #import data from csv/txt
    #make button that on click runs display tables
    #look through files in upload folder
    #check name of file for table name and then insert values into tablename
    if not importing:
        displayBase = pygame.Rect(37.5, 755,318,42)
        pygame.draw.rect(surface,(255,0,255),displayBase, border_radius = 10)
        displayText = pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18).render(str('IMPORT EXTERNAL USERS'), False, (0,0,0))
        displayRect = displayText.get_rect()
        displayRect.topleft = (70, 760)
        surface.blit(displayText, displayRect)
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and displayBase.collidepoint(pos):
            importing = True
    elif importing:
        importing = displayTables(importing)
    return importing

def displayTables(importing): #display the tables and values that the teacher can import
    surface.fill((0,255,255))
    rules = ['Please add your file with external users to the "upload" folder', 'Your file must be a .csv file that is comma delimited', 'You can add external users to "profile" and "classroomData" tables', 'the profile table consists of the following columns', 'Username VARCHAR(255) NOT NULL PRIMARY KEY', 'Email VARCHAR(255)', 'Name CHAR(25)', 'Gender CHAR(25)', 'DateOfBirth DATETIME', 'Phone CHAR(255)', 'Hash INT NOT NULL', 'Teacher BIT', 'ClassroomCode INT', 'the classroomData table consists of the following columns', 'Username VARCHAR(255) NOT NULL', 'CurrentTopic VARCHAR(25)', 'TotalCorrectAnswers INT', 'TotalPercentage REAL', 'LastLessonTime DATETIME', 'You must upload separate files for each table', 'You must include the table name in the file name']
    for i in range(len(rules)):
        ruleText = pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 13).render(str(rules[i]), False, (0,0,0))
        ruleRect = ruleText.get_rect()
        ruleRect.topleft = (2, 15*i)
        surface.blit(ruleText, ruleRect)
    cancelBase = pygame.Rect(37.5, 675,318,42)
    pygame.draw.rect(surface,(255,255,0),cancelBase, border_radius = 10)
    cancelText = pygame.font.Font('din-next-rounded-lt-pro-bold.ttf', 18).render(str('CANCEL'), False, (0,0,0))
    cancelRect = cancelText.get_rect()
    cancelRect.topleft = (39, 680)
    surface.blit(cancelText, cancelRect)
    uploadContents = []
    for root, dirs, files in os.walk('upload'):
            for file in files:
                if file[-4:] == '.csv' and (('classroomData' in file) ^ ('profile' in file)):
                    if 'classroomData' in file:
                        uploadContents.append([file, 'classroomData', False])
                    else:
                        uploadContents.append([file, 'profile', False])
    print(uploadContents)
    if len(uploadContents) == 0:
        errorText = pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 13).render(str('There are no valid files in the folder'), False, (255,0,0))
        errorRect = errorText.get_rect()
        errorRect.topleft = (2, 500)
        surface.blit(errorText, errorRect)
    else:
            for filey in uploadContents:
                if filey[2] == False:
                    fileo = 'upload\\' + str(filey[0])
                    with open(fileo, "r") as file:
                        for index, row in enumerate(csv.reader(file)):
                            cursor.execute("""INSERT INTO ? VALUES (?,?,?)""", [filey[1],*row])
                    filey[2] == True
    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] and cancelBase.collidepoint(pos):
        importing = False
        for file in uploadContents:
            os.remove('upload\\' + str(file[0]))
    return importing
def individual(): #click on name to get individual data
    pass
def overall(): #displays all users in classroom
    pass
def getCrossTable():
    cursor.execute("""SELECT profile.Username AS Username,
                    COALESCE(classroomData.LastLessonTime, MAX(lessonsCompleted.DateCompleted)) AS LastLessonTime,
                    COALESCE(classroomData.CurrentTopic,(SELECT questions.Topic
                    FROM lessonsCompleted
                    JOIN lessonQuestions ON lessonsCompleted.LessonID = lessonQuestions.LessonID
                    JOIN questions ON lessonQuestions.QuestionID = questions.QuestionID
                    WHERE lessonsCompleted.Username = profile.Username
                    ORDER BY lessonsCompleted.DateCompleted DESC
                    LIMIT 1)) AS CurrentTopic,
                    SUM(lessonsCompleted.CorrectAnswers) + COALESCE(classroomData.TotalCorrectAnswers, 0) AS TotalCorrectAnswers,
                    (COALESCE((AVG(lessonsCompleted.Percentage) + classroomData.TotalPercentage)/2, AVG(lessonsCompleted.Percentage)) * 100) AS TotalPercentage,
                    SUM(lessonsCompleted.PointsGained) + COALESCE(classroomData.TotalPoints, 0) AS TotalPoints
                    FROM profile
                    LEFT JOIN lessonsCompleted ON lessonsCompleted.Username = profile.Username
                    LEFT JOIN classroomData ON classroomData.Username = profile.Username
                    WHERE profile.ClassroomCode = ? AND profile.Teacher = ?
                    GROUP BY profile.Username
                    ORDER BY TotalPoints DESC;""", [code, 0])
    values = cursor.fetchall()
    print(values)
    value = []
    for i in range(len(values)):
        temp = []
        for j in range(len(values[i])):
            if type(values[i][j]) == float:
                temp.append(str(math.floor(values[i][j])) + '%')
            elif len(str(values[i][j])) == 10 and '-' in values[i][j]:
                tempo = ''
                for x in range(len(values[i][j])):
                    if values[i][j][x] == '-':
                        tempo += '.'
                    else:
                        tempo += values[i][j][x]
                temp.append(tempo)
            else:
                temp.append(values[i][j])
        value.append(temp)
    cols = ["Username", "Last \nLesson", "Topic", "Correct \nAnswers", "Percentage", "Points"]
    return value, cols
def teacherPage(values, columns, importing):
    surface.fill(color=bgColour)
    headingText = headingFont.render("Statistics for class: " + code, False, (255,255,255))
    headingRect = headingText.get_rect()
    headingRect.topleft = (5,10)
    surface.blit(headingText, headingRect)
    classTable = table(values, columns, pygame.font.Font('DIN Next Rounded LT W01 Regular.ttf', 13),surface)
    classTable.drawTable()
    classTable.fillTable()
    importing = importData(importing)
    return importing

values, columns = getCrossTable()
importing = False
while True:
    events()
    importing = teacherPage(values, columns, importing)
    pygame.display.flip()