# -*- coding: utf-8 -*-
'''
Created on 13-05-2014

@author: leonardo jofre

Cada texto tiene n secuencias que separan los caracteres en n espacios

referencias: para poder encontrar varias veces una palabra
http://stackoverflow.com/questions/3519565/find-the-indexes-of-all-regex-matches-in-python
'''

import numpy as np
import re
from function_ordered_pair import ordered_pair
from vrcoords import vr

def get_pattern(text, rank, word):
    """toma un texto y un rank (que dice cuantos espacios se van a av"""
    # pasarlo a un array
    text = np.array(list(text))
    # buscamos la palabra casa
    p = re.compile(word)
    
    match = set()
    for i in range(rank + 1):
        textRank = text[np.arange(i, len(text), rank + 1)]
        textRank = "".join(textRank.tolist())
        m = [((rank + 1) * m.start(0) + i, (rank + 1) * (m.end(0) - 1) + i) for m in re.finditer(p, textRank)]
        m = set(m)
        # hacer la correccion del rank
         
        match = match | m
    # buscamos las coincidencias de la palabra word dentro de este string
    
    # buscamos las posiciones especificas de cada una de las letras
    match = list(match)
    try:
        match = [range(m[0], m[1] + 1, rank + 1) for m in match]
    except :
        pass
    
    # convertir todos los elementos de las listas a tuplas
    match = [[ordered_pair(n) for n in m] for m in match]
            
    # eliminar todos los conjuntos de tuplas que no esten sobre la misma recta
    if match != []:
        """si la lista no esta vacia tiene que tener elementos sobre la misma recta"""
        match = [m for m in match if vr(m)]
    
    return match

def clearMatch(match):
    """elimina elementos repetidos y agrega informacion adicional"""
    match = sum(match, [])
    match = [m for m in match if m['position'] != []]

    for m in match:
        m['position'] = list(m['position'])
    return match
    
    
    
    




