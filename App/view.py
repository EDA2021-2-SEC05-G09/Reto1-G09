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


    else:
        sys.exit(0)
sys.exit(0)
