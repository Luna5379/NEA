import sqlite3

connection = sqlite3.connect('tablez.db')
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS TABLEZ")
table = """CREATE TABLE TABLEZ (
           Email VARCHAR(255) NOT NULL,
           First_Name CHAR(25) NOT NULL,
           Last_Name CHAR(25),
           Score INT
        );"""
cursor.execute(table)
#data1 = """INSERT INTO TABLEZ(Email, First_Name, Last_Name, Score) VALUES ("pinkjolly333@gmail.com", 'Pia', 'Jolly', 0);"""
cursor.execute("""INSERT INTO TABLEZ(Email, First_Name, Last_Name, Score) VALUES ("pinkjolly333@gmail.com", 'Pia', 'Jolly', 0);""")
connection.commit()
print("heart")














connection.close()