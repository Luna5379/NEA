import sqlite3

connection = sqlite3.connect('nea.db')
cursor = connection.cursor()
#cursor.execute("DROP TABLE IF EXISTS LESSONS")
table = """CREATE TABLE lessonsCompleted (
           LessonID INT NOT NULL,
           DateCompleted DATETIME NOT NULL,
           PointsGained INT NOT NULL,
           Percentage REAL NOT NULL,
           CorrectAnswers INT NOT NULL,
           Username INT NOT NULL
        );"""
cursor.execute(table)
print(cursor.fetchall())
connection.commit()
