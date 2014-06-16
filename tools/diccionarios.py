# -*- coding: utf-8 -*-

import re
import random
import os

def lista_diccionario():
    
    # Abrir ficheros
    currentDir = os.path.dirname(os.path.abspath(__file__))
    path = currentDir + "/../files/"
    archivo_nombre=open(path+'diccionario-nombres.txt', 'r')
    archivo_paises=open(path+'diccionario-paises.txt', 'r')
    archivo_verbos=open(path+'diccionario-verbos.txt', 'r')
    archivo_cosas=open(path+'diccionario-cosas.txt', 'r')
    
    # Listas que almacenarán las palabras de los diccionarios
    lista=[]

    #Lectura de ficheros  
    """
    # Lista Nombres
    for linea in archivo_nombre:
        lista.append(re.sub("[^a-z]","",linea))
    # Lista Países
    for linea in archivo_paises:
        lista.append(re.sub("[^a-z]","",linea))
    # Lista Verbos
    for linea in archivo_verbos:
        lista.append(re.sub("[^a-z]","",linea))
    """
    # Lista Cosas
    for linea in archivo_cosas:
        lista.append(re.sub("[^a-z]","",linea))
    
    # Cierre de ficheros.
    archivo_nombre.close()
    archivo_paises.close()
    archivo_verbos.close()
    archivo_cosas.close()
    
    return lista
