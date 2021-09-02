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
def initCatalog():
    catalog = model.newCatalog()
    return catalog



# Funciones para la carga de datos
def loadData(catalog):
    loadNombres(catalog)
    loadFechaNacimiento(catalog)
    loadNacionalidad(catalog)
    loadGenero(catalog)
    loadIDs(catalog)


def loadNombres(catalog):
    nombresfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(nombresfile, encoding='utf-8'))
    for nombre in input_file:
        model.addNombre(catalog, nombre)

def loadFechaNacimiento(catalog):
    fechanacimientofile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(fechanacimientofile, encoding='utf-8'))
    for nacimiento in input_file:
        model.addFechaNacimiento(catalog, nacimiento)

def loadNacionalidad(catalog):
    Nacionalidadfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(Nacionalidadfile, encoding='utf-8'))
    for nacio in input_file:
        model.addNacionalidad(catalog, nacio)

def loadGenero(catalog):
    Generosfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(Generosfile, encoding='utf-8'))
    for genero in input_file:
        model.addGenero(catalog, genero)

def loadIDs(catalog):
    IDsfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(IDsfile, encoding='utf-8'))
    for id in input_file:
        model.addID(catalog, id)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
