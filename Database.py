import sqlite3
from DB_Interface import DataBaseMovies
from Movie import Movie

#implementa de la interface "DataBaseMovies"
class DataBase(DataBaseMovies):

    def __init__(self, db_name="moviesDB"):

        # Se crea la conexion a la base de datos
        self.conexion = sqlite3.connect(db_name)

    def createTable(self):
        # Se crea el cursor para manejar consultas
        cursor = self.conexion.cursor()
        #se crea la tabla de peliculas y la demas logia
        try:
            #sí no existe, se crea la tabla movies
            cursor.execute("""CREATE TABLE IF NOT EXIST movies (id  INTEGER PRIMARY KEY AUTOINCREMENT,
                                            title VARCHAR(80),
                                            year INTEGER,
                                            directors TEXT,
                                            stars TEXT,
                                            genre TEXT,
                                            image VARCHAR(250)
                                            )""")
            return ("Tabla _movie_ creada con exito")
            
        
        except sqlite3.Error as error:
            
            print("Error al conectar con sqlite", error)

            #Commit y se cierra la conexion
            self.conexion.commit()
            self.conexion.close()


    def saveMovie(self):
        # Se crea el cursor para manejar consultas
        self.cursor = self.conexion.cursor()
        #se crea la tabla de peliculas y la demas logia
        #
        #
        #

        pass

    def deleteMovie(self):
        # Se crea el cursor para manejar consultas
        self.cursor = self.conexion.cursor()
        #se crea la tabla de peliculas y la demas logia
        #
        #
        #
        pass

    def showAllMovies(self):
        # Se crea el cursor para manejar consultas
        self.cursor = self.conexion.cursor()
        #se crea la tabla de peliculas y la demas logia
        #
        #
        #
        pass

    def showMovie(self):
        # Se crea el cursor para manejar consultas
        self.cursor = self.conexion.cursor()
        #se crea la tabla de peliculas y la demas logia
        #
        #
        #
        pass

if __name__ == "__main__":
    pass