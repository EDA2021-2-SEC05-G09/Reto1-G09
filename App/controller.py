"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def initCatalog(lista):
    catalog = model.newCatalog(lista)
    return catalog



# Funciones para la carga de datos
def loadData(catalog):
    loadArtWorks(catalog)
    loadArtists(catalog)



def loadArtWorks(catalog):
    artworks = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworks, encoding='utf-8'))
    for Artworks in input_file:
        model.addArtWork(catalog, Artworks)

def loadArtists(catalog):
    artistfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)



# Funciones de ordenamiento
def sortdate(catalog, size, itera):
   
    return model.sortdate(catalog, size, itera)


# Funciones de consulta sobre el catálogo
def Ayear(catalog,y1,y2):
    
    return model.Ayear(catalog,y1,y2)

def Tecnicaartistas(catalog,nombre):

    return model.Tecnicaartistas(catalog,nombre)

