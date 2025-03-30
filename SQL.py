import sqlite3

connection = sqlite3.connect('nea.db')
cursor = connection.cursor()
#cursor.execute("DROP TABLE IF EXISTS Options")
table = """CREATE TABLE options (
           OptionID INT NOT NULL,
           QuestionID INT NOT NULL,
           Option VARCHAR(255) NOT NULL,
           PRIMARY KEY (OptionID)
        );"""
#cursor.execute(table)
#cursor.execute("""INSERT INTO options (OptionID, QuestionID, Option)
#VALUES (3, 1, "Tells the printer to print 'x'")""")
cursor.execute("""UPDATE options
               SET Option = "Tells the printer to print document x"
               WHERE OptionID = 2;""")
print(cursor.fetchall())
connection.commit()
