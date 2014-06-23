# -*- coding: utf-8 -*-
"""pasar los indices de inicio y fin a indices de una matriz de ancho 60 columnas"""

from time import time

def indexConvertionListToArray(jump, tup):
    init, end = tup
    tup = range(init, end, jump + 1)
    
def removeInvalidChar(words):
    words = words.replace("Á","a")
    words = words.replace("É","e")
    words = words.replace("Í","i")
    words = words.replace("Ó","o")
    words = words.replace("Ú","u")
    words = words.replace("á","a")
    words = words.replace("é","e")
    words = words.replace("í","i")
    words = words.replace("ó","o")
    words = words.replace("ú","u")
    return words

    
