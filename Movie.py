class Movie():

    #constructor
    def __init__(self, title: str,  descripcion: list(), stars: list(), year: int, directors: list(), image: int, genre: str):
        self.title = title              #1_Buscar_películas_ID_de_IMDB_por_título
        self.year = year                  #1_Buscar_películas_ID_de_IMDB_por_título
        self.directors = directors      #2_Obtener_detalles_de_la_película_por_IMDB 
        self.stars = stars              #2_Obtener_detalles_de_la_película_por_IMDB 
        self.genre = genre              #2_Obtener_detalles_de_la_película_por_IMDB 
        self.image = image              #3_Obtener_imágenes_de_películas_por_IMDB 

    #Representacion en "str" del objeto de tipo "Pelicula"
    def __str__(self):
         return f"""Titulo de la pelicula: {self.title}\nActores: {self.stars}\n
                    Año de emision: {self.year}\nDirectores: {self.directors}\n
                        Poster: {self.image}\nGenero: {self.genre}"""
