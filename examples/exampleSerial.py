# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: equipo de desarrollo
'''

from tools.serial import get_pattern
from tools.pdftolist import pdf2string
from time import time

#

print "leyendo la biblia..."

path = "./../files/biblia.pdf"
t = time()
sheets = pdf2string(path=path)
print "biblia leida en ", time() - t, " segundos"
pos = []
for index, sheet in enumerate(sheets):
    pos.append((index, get_pattern(text=sheet, rank=61, word="casa")))
print pos

# test: se automatiza la verificacion de los resultados

