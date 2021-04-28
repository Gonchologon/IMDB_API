import sqlite3
from DB_Interface import DataBaseMovies
from Movie_Interface import MoviesData
from Movie import Movie

#CLASE PARA CREAR LA BASE DE DATOS

#implementa de la interface "DataBaseMovies"
class DataBase(DataBaseMovies):

    def __init__(self, db_name="moviesDB"):

        # Se crea la conexion a la base de datos
        self.conexion = sqlite3.connect(db_name)

    def createTable(self):
        # Se crea el cursor para manejar consultas
        cursor = self.conexion.cursor()
        #se crea la tabla de peliculas y la demas logica
        try:
            #sí no existe, se crea la tabla movies
            cursor.execute("""CREATE TABLE IF NOT EXIST movies (id  INTEGER PRIMARY KEY AUTOINCREMENT,
                                            title VARCHAR(80),
                                            yearr INTEGER,
                                            description TEXT,
                                            directors TEXT,
                                            stars TEXT,
                                            genres TEXT,
                                            image VARCHAR(250)
                                            )""")
            return ("Tabla _movie_ creada con exito")
            
        
        except sqlite3.Error as error:
            
            print("Error al conectar con sqlite", error)

            #Commit y se cierra la conexion
            self.conexion.commit()
            self.conexion.close()


    def saveMovie(self, movie):
        # Se crea el cursor para manejar consultas
        self.cursor = self.conexion.cursor()
        #Consulta para ver si existen datos 
        self.cursor.execute(f"""SELECT id_imdb FROM movies WHERE id_imdb = '{movie.id_imdb}' """)
        id_movie = self.cursor.fetchone() #guardamos la pelicula en una variable
        if id_movie != None:
            return "Mi loco, esa pelicula ya fue guardada en la DB"
        else:
            # (id_imdb, title, yearr, description, directors, stars, genres, image)
            #self.cursor.execute(f"""INSERT INTO movies VALUES ('{movie.id_imdb}','{movie.title}','{movie.yearr}',
            #                                '{movie.description}','{movie.description,}','{movie.directors}',   
            #                                        '{movie.stars}','{movie.genres}','{movie.image}')""") 
            #Se inserta en la tabla
            self.cursor.execute("INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (movie.id_imdb, movie.title, movie.yearr, movie.description, movie.directors, movie.stars, movie.genres, movie.image))
            self.conexion.commit()   
        return "¡¡¡ Datos guardados :D !!!"                                  
        

    def deleteMovie(self, movie):
        # Se crea el cursor para manejar consultas
        self.cursor = self.conexion.cursor()
        #Sí no existe la pelicula, manda error
        if movie == None:
            return "Esta pelicula no esta en la base de datos!!!"
        #Sí no, se procede a borrarla de la base de datos
        else:
            self.cursor.execute("DELETE FROM movies WHERE title = ?", (movie,)) #Borramos pelicula mediante el nombre
            self.conexion.commit()

        return "Pelicula borrada :O"

    def showAllMovies(self):                               #Falta este
        # Se crea el cursor para manejar consultas
        self.cursor = self.conexion.cursor()
        #Query para mostrar todas las peliculas en la DB
        self.cursor.execute("SELECT * FROM movies")
        rows = self.cursor.fetchall() #Tomamos todas las peliculas con "fetchall"
        movies_saved = [] #Lista para almacenar las peliculas
        if rows == None:
            return "No existe ésta pelicula en la DB"
        else:
            for row in movies_saved:
                print(row)
    
    def showMovie(self, movie):                            #Y este
        # Se crea el cursor para manejar consultas
        self.cursor = self.conexion.cursor()
        #Query para mostrar la pelicula solicitada de la DB
        self.cursor.execute("SELECT * FROM movies WHERE title = ?", (movie,))
        movie_saved = self.cursor.fetchone() #tomamos solo la pelicula solicitada con "fetchone"
        if movie_saved == None:
            return "No existe ésta pelicula en la DB"
        else:
            for row in movie_saved:
                print(row)

        pass

if __name__ == "__main__":
    pass