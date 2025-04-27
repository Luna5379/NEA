import sqlite3
import csv

options = 'options.csv'
connection = sqlite3.connect('nea.db')
cursor = connection.cursor()
#cursor.execute("DROP TABLE IF EXISTS profile")
table = """CREATE TABLE lessonQuestions (
           LessonID INT NOT NULL,
           QuestionID INT NOT NULL,
           DifficultyGroup INT NOT NULL,
           Correct BIT,
           PRIMARY KEY(LessonID, QuestionID),
           FOREIGN KEY(LessonID) REFERENCES lessons(LessonID),
           FOREIGN KEY(QuestionID) REFERENCES questions(QuestionID)
        );"""
#cursor.execute(table)
cursor.execute("""SELECT profile.Username, MAX(lessonsCompleted.DateCompleted) AS LastLessonTime, (SELECT questions.Topic FROM questions, lessonsCompleted, lessonQuestions WHERE lessonsCompleted.LessonID = lessonQuestions.LessonID AND lessonQuestions.QuestionID = questions.QuestionID ORDER BY lessonsCompleted.DateCompleted DESC LIMIT 1) AS CurrentTopic, SUM(lessonsCompleted.CorrectAnswers) AS TotalCorrectAnswers, (AVG(lessonsCompleted.Percentage)*100) AS TotalPercentage, SUM(lessonsCompleted.PointsGained) AS TotalPoints FROM (questions, lessonsCompleted, profile, lessonQuestions) WHERE profile.ClassroomCode = ? AND profile.Teacher = ? AND lessonsCompleted.Username = profile.Username GROUP BY profile.Username""", [0000, 0])
#cursor.execute("""ALTER TABLE classroom DROP COLUMN ClassroomCode;""")
# with open(options, "r") as file:
#     for index, row in enumerate(csv.reader(file)):
#         cursor.execute("""INSERT INTO options VALUES (?,?,?)""", [*row])
#cursor.execute("""DELETE FROM lessons""")
print(cursor.fetchall())
connection.commit()
