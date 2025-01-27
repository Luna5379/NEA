import sqlite3

connection = sqlite3.connect('lessons.db')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS LESSONS")
table = """CREATE TABLE LESSONS (
           Question VARCHAR(255) NOT NULL,
           Answer VARCHAR(255) NOT NULL,
           Difficulty INT,
           Type VARCHAR(25),
           LessonPercentage REAL,
           Options LIST,
           Example LONGTEXT
        );"""
cursor.execute(table)
