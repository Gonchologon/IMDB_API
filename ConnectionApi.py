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
conn.request("GET", "/?type=get-movie-details&imdb=tt7784604", headers=headers)
res = conn.getresponse() #Objeto de tipo HTTPResponse 

class APIMovie(ApiConnect):

    def searchMovie(self, nombre:str): #Funcion que busca los datos de la pelicula
        
        #res = conn.getresponse()                     #Se guarda en una variable, y se obtiene un objeto de tipo HTTPResponse 
        #data = res.read()                            #Convertimos a texto el objeto anterior en una variable nueva, ahora es de tipo "bytes"
        #new_data_json1 = json.loads(data)             #Ahora convertimos a json el objeto anterior de tipo "bytes"
        if res.status != 200: #Se comprueba si el status es correcto, si no, manda un error
            return "ERROR IN API CONNECTION"
        else:
            movies_list = [] #Lista para guardar datos obtenidos de la pelicula
            #Primer request que buscara la pelicula que se le ingrese en la funcion

            conn.request("GET", "/?type=get-movies-by-title&title="+nombre, headers=headers)
            res1 = conn.getresponse() #Objeto de tipo HTTPResponse 
            data1 = res1.read()  #Convertimos a texto el objeto anterior, ahora es de tipo "bytes"
            new_data_json1 = json.loads(data1) #Ahora convertimos a json el objeto de tipo "bytes"

            for movie in new_data_json1["movie_results"]: #Se extraen datos del primer request
                #Extraccion de datos de la API
                imdb_id = movie["imdb_id"]
                movies_list.append(imdb_id)
                title = movie["title"]
                movies_list.append(title)
                yearr = movie["year"]
                movies_list.append(yearr)

            conn.request("GET", "/?type=get-movie-details&imdb="+imdb_id, headers=headers)#tt7784604 hereditary ID
            res2 = conn.getresponse()           #Objeto de tipo HTTPResponse 
            data2 = res2.read()                 #Convertimos a texto el objeto anterior, ahora es de tipo "bytes"
            new_data_json2 = json.loads(data2)  #Ahora convertimos a json el objeto de tipo "bytes"
            #Extraccion de datos de la API del segundo request
            if "description" in new_data_json2:
                description = new_data_json2["description"]
                movies_list.append(description)
            if "directors" in new_data_json2:
                directors = new_data_json2["directors"]
                movies_list.append(directors)     
            if "stars" in new_data_json2:
                stars = new_data_json2["stars"]
                movies_list.append(stars)
            if "genres" in new_data_json2:
                genres = new_data_json2["genres"]
                movies_list.append(genres)

            #conn.request necesita el ID de la pelicula, este mismo se extrae del request anterior
            conn.request("GET", "/?type=get-movies-images-by-imdb&imdb="+imdb_id, headers=headers)
            res3 = conn.getresponse()           #Objeto de tipo HTTPResponse 
            data3 = res3.read()                 #Convertimos a texto el objeto anterior, ahora es de tipo "bytes"
            new_data_json3 = json.loads(data3)  #Ahora convertimos a json el objeto de tipo "bytes "
            #Extraccion de datos de la API del tercer request
            if "poster" in new_data_json3:
                image = new_data_json3["poster"]
                movies_list.append(image)

            #Si la info de la pelicula es diferente de vacio, creamos el Objeto de tipo Movie
            if imdb_id != "" and title != "" and yearr != "" and description != "" and directors != "" and stars != "" and genres != "" and image != "":
                movie_created = Movie(imdb_id, title, yearr, description, directors, stars, genres, image)
                #movies_list.append(movie_created)
            
            #for i in range(len(movies_list)):
                #print("".join(str(movies_list[i]))
            
        return movie_created
        
    