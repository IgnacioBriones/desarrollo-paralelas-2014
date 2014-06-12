# -*- coding: utf-8 -*-
'''
Created on 13-05-2014

@author: leonardo jofre

Cada texto tiene n seuencias que separan los caracteres en n espacios

referencias
http://stackoverflow.com/questions/3519565/find-the-indexes-of-all-regex-matches-in-python
'''

import numpy as np
import re

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
    return match
    
    
    
    




