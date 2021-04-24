from abc import ABC, abstractmethod
from Movie import Movie

class MoviesData(ABC):

    #activar api para extraer los datos
    @abstractmethod
    def actualizador(self):
        pass

    @abstractmethod
    def saveMovie(self, nombre: str):
        pass

    @abstractmethod
    def getMovieByTitle(self, nombre: str) -> Movie:
        pass
