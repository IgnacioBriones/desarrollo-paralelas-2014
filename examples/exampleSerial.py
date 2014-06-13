# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: equipo de desarrollo
'''

from tools.serial import get_pattern
from tools.pdftolist import pdf2string
from time import time
import sys

#

print "leyendo la biblia..."

path = "./../files/biblia.pdf"
t = time()
sheets = pdf2string(path=path)
print "biblia leida en ", time() - t, " segundos"
pos = []
palabras = []

for i in range(len(sys.argv)):
    if i >= 1:
        palabras.append(sys.argv[i])
        
for index, sheet in enumerate(sheets):
    for x in range (len(palabras)):  
        pos.append((index, get_pattern(text=sheet, rank=0, word=palabras[x])))
print pos

# test: se automatiza la verificacion de los resultados

