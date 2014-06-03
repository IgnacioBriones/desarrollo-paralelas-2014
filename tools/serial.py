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
    text = np.array(text)
    # buscamos la palabra casa
    p = re.compile(word)
    
    text_rank1 = text[np.arange(0, len(text), rank + 1)]
    text_rank1 = text_rank1.tolist()
    text_rank1 = "".join(text_rank1)
    
    # buscamos las coincidencias de la palabra casa dentro de este string
    return [(m.start(0), m.end(0)) for m in re.finditer(p, text_rank1)]
    
    
    
    




