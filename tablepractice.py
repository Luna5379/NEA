import sqlite3

connection = sqlite3.connect('tablez.db')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS TABLEZ")
table = """CREATE TABLE TABLEZ (
           Email VARCHAR(255) NOT NULL,
           Name VARCHAR(255) NOT NULL,
           UserName VARCHAR(25),
           Gender CHAR(25),
           DateOfBirth DATETIME,
           PhoneNumber INt
        );"""
cursor.execute(table)
cursor.execute("""INSERT INTO TABLEZ (Email, Name, UserName, Gender, DateOfBirth, PhoneNumber)
               VALUES ('silviasantabuil@outlook.com', 'Silvia', 'Luna5379', 'F', date('2007-07-08'), 07898787635);""")
cursor.execute("""SELECT * FROM TABLEZ ORDER BY Name DESC""")
print(cursor.fetchall())
connection.commit()
print("heart")







connection.close()