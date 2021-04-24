from abc import ABC, abstractmethod
from Api_Interface import ApiConnect
from Movie import Movie
import http.client
import json

conn = http.client.HTTPSConnection("movies-tvshows-data-imdb.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "cbcf05ab5fmsh24801d50619d037p1b4742jsn25a4dc832034",
    'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
    }

class APIMovie(ApiConnect):

    def searchMovie(self, nombre:str):
        #Concatenamos la peticion a la api con el parametro 
        #De la funcion, para obtener info de la pelicula
        conn.request("GET", "/?type=get-movies-by-title&title="+nombre, headers=headers) #Peticion a la api

        res = conn.getresponse()                     #Se guarda en una variable, y se obtiene un objeto de tipo HTTPResponse 
        data = res.read()                            #Convertimos a texto el objeto anterior en una variable nueva, ahora es de tipo "bytes"
        new_data_json = json.loads(data)             #Ahora convertimos a json el objeto anterior de tipo "bytes"
        if res.status == 200 and res.reason == "OK": #Se comprueba si el status es correcto, si no, mada un error
            if new_data_json is None:
                print("No info")
            pass 
        else: #Si no, Se prosigue a obtener los datos del request
            return "ERROR"


#print(json.dumps(new_data, indent=4, sort_keys=True)) #Esto sirve solo para formatear el print que muestra el json


"""
"movie_results"
"search_results"
"status"
"status_message"
"""
 