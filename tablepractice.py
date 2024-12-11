import sqlite3

connection = sqlite3.connect('tablez.db')
cursor = connection.cursor()
#cursor.execute("DROP TABLE IF EXISTS TABLEZ")
table = """CREATE TABLE TABLEZ (
           Email VARCHAR(255) NOT NULL,
           First_Name CHAR(25) NOT NULL,
           Last_Name CHAR(25),
           Score INT
        );"""
#cursor.execute(table)
cursor.execute("""SELECT * FROM TABLEZ ORDER BY Score DESC""")
print(cursor.fetchall())
connection.commit()
print("heart")







connection.close()