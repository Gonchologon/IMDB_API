from abc import ABC, abstractmethod


class DataBaseMovies(ABC):

    #Crea una tabla en la base de datos 
    @abstractmethod
    def createTable(self):
        pass
    
    #Guarda una pelicula en la base de datos
    @abstractmethod
    def saveMovie(self):
        pass
   
    #Borra una pelicula de la BDD conforme al ID
    @abstractmethod
    def deleteMovie(self, id_movie):
        pass

    #Muestra todas las peliculas de la base de datos
    @abstractmethod
    def showAllMovies(self):
        pass

    #Muestra todas las peliculas de la base de datos
    @abstractmethod
    def showMovie(self):
        pass
 
