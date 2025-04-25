import sqlite3

connection = sqlite3.connect('nea.db')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS profile")
table = """CREATE TABLE profile (
           Username VARCHAR(255) NOT NULL PRIMARY KEY,
           Email VARCHAR(255),
           Name CHAR(25),
           Gender CHAR(25),
           DateOfBirth DATETIME,
           Phone CHAR(255),
           Hash INT NOT NULL
        );"""
cursor.execute(table)
#cursor.execute("""ALTER TABLE classroom DROP COLUMN ClassroomCode;""")
#cursor.execute("""UPDATE options
 #              SET Option = "Tells the printer to print document x"
  #             WHERE OptionID = 2;""")
print(cursor.fetchall())
connection.commit()
