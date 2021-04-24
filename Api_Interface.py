from abc import abstractmethod, ABC

class ApiConnect(ABC):

    #Regresa una pelicula
    @abstractmethod
    def searchMovie(self, nombre:str):
        pass