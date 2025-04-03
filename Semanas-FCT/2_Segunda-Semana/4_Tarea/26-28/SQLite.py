import sqlite3
with sqlite3.connect("DB.db") as connection:
    cursor = connection.cursor()
    print("Base de datos creada y conexión abierta.")

cursor.execute(""" CREATE TABLE IF NOT EXISTS ayunts (
               idAyunt INTEGER PRIMARY KEY AUTOINCREMENT, 
               place TEXT UNIQUE,
               coor TEXT
               )
""")
cursor.execute(""" CREATE TABLE IF NOT EXISTS convocatorias
               idConv INTEGER PRIMARY KEY AUTOINCREMENT,
               place_Ayunts INTEGER,
               name TEXT,
               FOREIGN KEY (place_Ayunts)
""")


connection.commit
cursor.execute(""" INSERT INTO OR IGNORE 

               """)