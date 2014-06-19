# -*- coding: utf-8 -*-

import re
import random
import os

def fraseimplicita():
    
    # Abrir ficheros
    currentDir = os.path.dirname(os.path.abspath(__file__))
    path = currentDir + "/../files/"
    archivo_nombre=open(path+'diccionario-nombres.txt', 'r')
    archivo_paises=open(path+'diccionario-paises.txt', 'r')
    archivo_verbos=open(path+'diccionario-verbos.txt', 'r')
    archivo_cosas=open(path+'diccionario-cosas.txt', 'r')
    
    # Listas que almacenarán las palabras de los diccionarios
    nombres=[]
    paises=[]
    verbos=[]
    cosas=[]
    
    frase=[]
    #Lectura de ficheros
    
    # Lista Nombres
    for linea in archivo_nombre:
        nombres.append(re.sub("[^a-z]","",linea))
    # Lista Países
    for linea in archivo_paises:
        paises.append(re.sub("[^a-z]","",linea))
    # Lista Verbos
    for linea in archivo_verbos:
        verbos.append(re.sub("[^a-z]","",linea))
    # Lista Cosas
    for linea in archivo_cosas:
        cosas.append(re.sub("[^a-z]","",linea))
    
    # Cierre de ficheros.
    archivo_nombre.close()
    archivo_paises.close()
    archivo_verbos.close()
    archivo_cosas.close()
    
    # Generación de números aleatorios desde 0 hasta largo lista
    num1=random.randrange(0, len(nombres))
    num2=random.randrange(0, len(paises))
    num3=random.randrange(0, len(verbos))
    num4=random.randrange(0, len(cosas))
    
    # Cadena de retorno
    frase.append(nombres[num1])
    frase.append(verbos[num3])
    frase.append(cosas[num4])
    frase.append(paises[num2])
    return frase
