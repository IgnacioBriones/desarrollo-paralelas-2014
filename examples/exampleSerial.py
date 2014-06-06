# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: equipo de desarrollo
'''

from tools.serial import get_pattern
from tools.pdfstring import pdf2string
from time import time

#
t = time()
print "leyendo la biblia . . ."

path =  "./../files/biblia.pdf"
sheets = pdf2string(path, borrarCaracteresEspeciales=True, separadosPorHoja=True)

print "biblia leida en ", time() - t, " segundos"

for sheet in sheets:
    pos = get_pattern(text=sheet, rank=2, word="casa")
    print pos
