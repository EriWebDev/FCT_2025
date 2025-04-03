#importar base de datos de SQLite
import sqlite3

from WikiScraping import coso

info_countries = coso()

#conexión a la base de datos, si el archivo no existe, SQLite lo crea automáticamente
#la instrucción with (gestor de contexto) permite abrir y cerrar la conexión automáticamente
#así garantizamos que se cierre correctamente incluso si se produce un error
with sqlite3.connect("paises.db") as connection:
#crear un objeto cursor que permitirá ejecutar comandos SQL y consultar en la base de datos
    cursor = connection.cursor()
    print("Base de datos creada y conecxión abierta.")

#creación de tablas
#tipos de datos: TEXT, INTEGER, REAL
#tabla Países, cada país nos lleva a su propia tabla con sus datos
#cada país es un registro, que se guarda en una columna "Nombre"
#IF NOT EXISTS para garantizar que solo se cree si no existe; UNIQUE para que sea único

cursor.execute ("""CREATE TABLE IF NOT EXISTS countries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE 
                )""")

#insertar paises
for country in info_countries.keys():
     cursor.execute("INSERT OR IGNORE INTO countries (name) VALUES (?)", (country,))    


#crear tablas específicas de cada país
#la f antes de las """ es necesaria para que SQLite reconozca {country.lower()} como el nombre de la tabla de arriba
for country in info_countries.keys():
      cursor.execute(f"""
                     CREATE TABLE IF NOT EXISTS {country.lower()} (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     history TEXT,surface TEXT,
                     population TEXT,
                     pib TEXT)
                     """)


connection.commit()
#SQLite no puede entrar en listas, por lo que tengo que convertir los datos en cadenas de texto
#para lo que necesito un bucle for y entrar en cada país
for country, info in info_countries.items():
     history = " ".join(info["history"])
     surface = " ".join(info["surface"])
     population = " ".join(info["population"])
     pib = " ".join(info["pib"])

for country, info in info_countries.items():
     cursor.execute(f"""
                    INSERT INTO {country.lower()} (history, surface, population, pib)
                    VALUES (?, ?, ?, ?)
                    """, (history, surface, population, pib))

#guardado de los cambios
connection.commit()


#ahora tenemos que mostrar los datos

#la tabla de todos los países
cursor.execute("SELECT * FROM countries")
countries_names = cursor.fetchall()
for country_name in countries_names:
     print ("Países: \n")

#tabla de grecia
cursor.execute("SELECT * FROM Grecia")
greece_data = cursor.fetchall()
for rowsG in greece_data:
     print(rowsG)

#tabla de italia
cursor.execute("SELECT * FROM Italia")
italy_data = cursor.fetchall()
for rowsI in italy_data:
     print(rowsI)

connection.commit()
#para cerrar la base de datos una vez hayamos terminado todas las operaciones
#con la instrucción with, nos ahorramos llamar manualmente al cierre
# connection.close()