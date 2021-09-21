﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as iso
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as me
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf
from datetime import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(lista):
  
    catalog = {"Artworks": None,
               "Artists": None}

    catalog['Artworks'] = lt.newList(lista)
    catalog['Artists'] = lt.newList(lista)
    
 
 
    
    
    return catalog
   

# Funciones para agregar informacion al catalogo
def addArtWork(catalog, artWork):
    lt.addLast(catalog['Artworks'],artWork)

def addArtist(catalog, Artist):
    lt.addLast(catalog['Artists'], Artist)


# Funciones para creacion de datos

# Funciones de consulta
def Ayear(catalog,y1,y2):
    artists=catalog["Artists"] 
    final=lt.newList()
    for cont in range(lt.size(artists)):
        orden=lt.getElement(artists,cont)
        date=int(orden["BeginDate"])
        id=orden["ConstituentID"]
        n_artist=orden["DisplayName"]
        f_date=int(orden["EndDate"])
        nationality=orden["Nationality"]
        if orden["Gender"]=="":
                 gender="desconocido"
        else:
            gender=orden["Gender"]
        if orden["Nationality"]=="":
                nationality="desconocido"
        else:
            nationality=orden["Nationality"]
        if date!=0 and date!=None and date >=y1 and date<=y2:
           entonces={"nombre" : n_artist,"fecha":date, "fecha_final":f_date,"genero":gender,"nacionalidad":nationality,"id":id}
           lt.addLast(final, entonces)
    me.sort(final,cmpastistsBydate)
    return final

# Funciones utilizadas para comparar elementos dentro de una lista 
def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    if artwork1["DateAcquired"]==""  :
       artwork1["DateAcquired"]=("0001/01/01")
    if artwork2["DateAcquired"]==""  :
       artwork2["DateAcquired"]=("0001/01/01")
    f1=datetime.strptime(artwork1["DateAcquired"].replace("-","/"),"%Y/%m/%d" )
    f2=datetime.strptime(artwork2["DateAcquired"].replace("-","/"),"%Y/%m/%d" )
    ffinal=f1<f2
    return ffinal

def cmpastistsBydate(artist1, artist2):

    return artist1["fecha"] < artist2["fecha"]

# Funciones de ordenamiento
def sortdate(catalog, size, itera):
    sub_list = lt.subList(catalog['Artworks'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = itera.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
