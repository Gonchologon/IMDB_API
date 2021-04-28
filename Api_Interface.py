from abc import abstractmethod, ABC
from Movie import Movie

class ApiConnect(ABC):

    #Regresa una pelicula
    @abstractmethod
    def searchMovie(self, nombre:str) -> Movie:
        pass