"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.Algorithms.Sorting import insertionsort as iso
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar Cronologicamente los Artistas")
    print("3- Listar Cronológicamente las Adquisiciones")
    print("4- Clasificar Obras de un Artista por Técnica")
    print("5- Clasificar Obras por la Nacionalidad de sus Creadores")
    print("6- Transportar Obras de un Departamento")
    print("7- Proponer una nueva exposición del museo")
    print("0- Salir")


def ListaTipos():
    print("elige el tipo de lista que se desea(a:ARRAY_LIST) O (l:LINKED_LIST): ")

def initCatalog(lista):
   
    return controller.initCatalog(lista)

def loadData(catalog):

    controller.loadData(catalog)

def printSortResults(ord_artWork, sample=5000):
    size = lt.size(ord_artWork)
    if size > sample:
        print("Las primeras ", sample, " obras ordenadas son:")
        i=1
        while i <= sample:
            artWork = lt.getElement(ord_artWork,i)
            print("Titulo: " + artWork["Title"] + "  ID: "   +
                    artWork["ConstituentID"]  + " fecha: " +  artWork["DateAcquired"])
            i+=1
catalog=None
def printAyear(catalog):
    size=lt.size(catalog)
                                                                                             
    artistas1 = lt.getElement(catalog, 1)
    print("id: "+ artistas1["id"]+", nombre: "+artistas1["nombre"] + " , fecha nacimiento: " + str(artistas1["fecha"]) + " , genero: "+  artistas1["genero"] + " , nacionalidad: "  +artistas1["nacionalidad"])
    artistas2 = lt.getElement(catalog, 2)
    print("id: "+ artistas2["id"]+", nombre: "+artistas2["nombre"] + " , fecha nacimiento: " + str(artistas2["fecha"]) + " , genero: "+  artistas2["genero"] + " , nacionalidad: "  +artistas2["nacionalidad"])
    artistas3 = lt.getElement(catalog, 3)
    print("id: "+ artistas3["id"]+", nombre: "+artistas3["nombre"] + " , fecha nacimiento: " + str(artistas3["fecha"]) + " , genero: "+  artistas3["genero"] + " , nacionalidad: "  +artistas3["nacionalidad"])

    artistas1a = lt.getElement(catalog, size - 1)
    print("id: "+ artistas1a["id"]+", nombre: "+artistas1a["nombre"] + " , fecha nacimiento: " + str(artistas1a["fecha"]) + " , genero: "+  artistas1a["genero"] + " , nacionalidad:"  +artistas1a["nacionalidad"])
    artistas2a = lt.getElement(catalog, size - 2)
    print("id: "+ artistas2a["id"]+", nombre: "+artistas2a["nombre"] + " , fecha nacimiento: " + str(artistas2a["fecha"]) + " , genero: "+  artistas2a["genero"] + " , nacionalidad:"  +artistas2a["nacionalidad"])
    artistas3a = lt.getElement(catalog, size - 3)
    print("id: "+ artistas3a["id"]+", nombre: "+artistas3a["nombre"] + " , fecha nacimiento: " + str(artistas3a["fecha"]) + " , genero: "+  artistas3a["genero"] + " , nacionalidad:"  +artistas3a["nacionalidad"])
                                                                                            
def printOyear(catalog):
    size=lt.size(catalog)
                                                                                             
    obras1 = lt.getElement(catalog, 1)
    print("nombre: "+obras1["nombre"] +" id: "+obras1["id"]  +" artista: "+obras1["artista"] + " , fecha: " + str(obras1["fecha"]) + ", fecha adquicision: "+ obras1["dateacquired"]+ ", medio: "+  obras1["medio"] + " , dimensiones: "  +obras1["dimensiones"])
    obras2 = lt.getElement(catalog, 2)
    print("nombre: "+obras2["nombre"] + " id: "+obras2["id"]  +" artista: "+obras2["artista"] +" , fecha: " + str(obras2["fecha"]) + ", fecha adquicision: "+obras2["dateacquired"]+" , medio: "+  obras2["medio"] + " , dimensiones: "  +obras2["dimensiones"])
    obras3 = lt.getElement(catalog, 3)
    print("nombre: "+obras3["nombre"] + " id: "+obras3["id"]  +" artista: "+obras3["artista"] +" , fecha: " + str(obras3["fecha"]) +", fecha adquicision: "+obras3["dateacquired"]+ " , medio: "+  obras3["medio"] + " , dimensiones: "  +obras3["dimensiones"])

    obras1a = lt.getElement(catalog, size - 1)
    print("nombre: "+obras1a["nombre"] + " id: "+obras1a["id"]  +" artista: "+obras1a["artista"] +" , fecha: " + str(obras1a["fecha"]) +", fecha adquicision: "+obras1a["dateacquired"]+ " , medio: "+  obras1a["medio"] + " , dimensiones:"  +obras1a["dimensiones"])
    obras2a = lt.getElement(catalog, size - 2)
    print("nombre: "+obras2a["nombre"] + " id: "+obras2a["id"]  +" artista: "+obras2a["artista"] +" , fecha: " + str(obras2a["fecha"]) +", fecha adquicision: "+obras2a["dateacquired"]+ " , medio: "+  obras2a["medio"] + " , dimensiones:"  +obras2a["dimensiones"])
    obras3a = lt.getElement(catalog, size - 3)
    print("nombre: "+obras3a["nombre"] + " id: "+obras3a["id"]  +" artista: "+obras3a["artista"] +" , fecha: " + str(obras3a["fecha"]) +", fecha adquicision: "+obras3a["dateacquired"]+ " , medio: "+  obras3a["medio"] + " , dimensiones:"  +obras3a["dimensiones"])

def ObrasTecnica(valor,tamaño,maximo,tecnicamas):
    print("el artista tiene: "+str(valor) + " obras en el museo")
    print("el artista cuenta con: "+str(tamaño)+ " tecnicas diferentes")
    print("su tecnica mas usada es: "+str(maximo))
    for e in lt.iterator(tecnicamas):
        print("id: " +e["constituentid"]+" obra: "+e['name']+" medio: "+e['medium']+" Fecha: "+e['date']+" dimensiones: "+e['dimensions'])
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        lista= " "
        ListaTipos()
        Tipo=input("ingrese a o l: ")
        if Tipo=="a":
            lista="ARRAY_LIST"
        elif Tipo=="b":
            lista="LINKED_LIST"
        print("Cargando información de los archivos ....")
        catalog = initCatalog(lista)
        loadData(catalog)
        print('Obras cargadas: ' + str(lt.size(catalog['Artworks'])))
        print('Autores cargados: ' + str(lt.size(catalog['Artists'])))


    elif int(inputs[0]) == 2:

     
        y1 = int(input("Ingrese primer año:  "))
        y2 = int(input("Ingrese segundo año:  "))
        
        
        cantidadArtistas = controller.Ayear(catalog,y1,y2)
        print("                                                                                            ")
        print("============================================================================================")
        print("                                                                                            ")
        printAyear(cantidadArtistas)
        print("                                                                                            ")
        print("============================================================================================")
        print("                                                                                            ")
                                                                                            

    elif int(inputs[0]) == 3:
         itera=""
         clase=input("ingrese tipo de ordenamiento iterativo: I:(insertion sort),M:(Merge sort),Q:(Quick Sort),S:(Shell sort): ")
         if clase=="I":
             itera=iso
         elif clase=="M":
             itera=ms
         elif clase=="Q":
             itera=qs
         elif clase=="S":
             itera=ss
         size = input("Indique tamaño de la muestra: ")
         result = controller.sortdate(catalog, int(size),itera)
         if itera==iso:
             algoritmo="insertion"
         elif itera==ms:
             algoritmo="Merge"
         elif itera==qs:
             algoritmo="Quick"
         elif itera==ss:
             algoritmo="Shell"
            
         printSortResults(result[1])
         print("Para la muestra de", size, " elementos, con el arreglo de "+ algoritmo +  " el tiempo (mseg) es: ",
         str(result[0]))
         y1 = str(input("Ingrese primer año(AAAA-MM-DD):  "))
         y2 = str(input("Ingrese segundo año(AAAA-MM-DD):  "))
         cantidadObras = controller.Oyear(catalog,y1,y2)
         print("                                                                                            ")
         print("============================================================================================")
         print("                                                                                            ")
         printOyear(cantidadObras)
         print("                                                                                            ")
         print("============================================================================================")
         print("                                                                                            ")
    
    elif int(inputs[0]) == 4:
        nombre=input("ingrese nombre del artista: ")
        valor,tamaño,maximo,tecnicamas=controller.Tecnicaartistas(catalog,nombre)
        print("                                                                                            ")
        print("============================================================================================")
        print("                                                                                            ")
        ObrasTecnica(valor,tamaño,maximo,tecnicamas)
        print("                                                                                            ")
        print("============================================================================================")
        print("                                                                                            ")


    else:
        sys.exit(0)
sys.exit(0)
