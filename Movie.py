class Movie():

    #constructor
    def __init__(self, id_imdb: int, title: str, yearr: int, description: list(), directors: list(), stars: list(), genres: list(), image: str):
        self.id_imdb = id_imdb                      #1_Buscar_películas_ID_de_IMDB_por_título
        self.title = title                #1_Buscar_películas_ID_de_IMDB_por_título
        self.yearr = yearr                 #1_Buscar_películas_ID_de_IMDB_por_título
        self.description = description    #2_Obtener_detalles_de_la_película_por_IMDB 
        self.directors = directors        #2_Obtener_detalles_de_la_película_por_IMDB 
        self.stars = stars                #2_Obtener_detalles_de_la_película_por_IMDB 
        self.genres = genres              #2_Obtener_detalles_de_la_película_por_IMDB 
        self.image = image                #3_Obtener_imágenes_de_películas_por_IMDB 

    #Representacion en "str" del objeto de tipo "Pelicula"
    def __str__(self):
         return f"""ID: {self.id_imdb}\nTitulo de la pelicula: {self.title}\nAño de emision: {self.yearr}
                    \nDescripción: {self.description}\nDirectores: {self.directors}\nActores: {self.stars}
                            \nGeneros: {self.genres}\nPoster: {self.image}"""
