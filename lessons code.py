import sqlite3

connection = sqlite3.connect('lessons.db')
cursor = connection.cursor()
#cursor.execute("DROP TABLE IF EXISTS LESSONS")
table = """CREATE TABLE LESSONS (
           Question VARCHAR(255) NOT NULL,
           Answer VARCHAR(255) NOT NULL,
           Difficulty INT,
           Type VARCHAR(25),
           LessonPercentage REAL,
           Options VARCHAR(255),
           Example LONGTEXT
        );"""
#cursor.execute(table)
cursor.execute("""INSERT INTO LESSONS (Question, Answer, Difficulty, Type, LessonPercentage, Options, Example)
               VALUES ('What does the input(x) command do?', 'Outputs x and allows the user to input data', '1', 'What does this command do?', 0.05, 'Asks user to input x,Sets input to x,Outputs x', 'eg. input("What is your name?")');""")
cursor.execute("""SELECT * FROM LESSONS""")
print(cursor.fetchall())
connection.commit()
