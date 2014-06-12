# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: equipo de desarrollo
'''
import sys
from tools.serial import get_pattern
from tools.pdftolist import pdf2string
from time import time
from tools.stringdiccionarios import fraseimplicita

"""
word=[]
for i in range(1,len(sys.argv)):
    word.append(sys.argv[i])
"""
print "leyendo la biblia..."

path = "./../files/biblia.pdf"
t = time()
sheets = pdf2string(path=path)
print "biblia leida en ", time() - t, " segundos"
pos = []

frase = fraseimplicita()
#print "\n",frase

for palabra in frase:
    print "\nPalabra: ",palabra
    for index, sheet in enumerate(sheets):
	pos.append((index, get_pattern(text=sheet, rank=0, word=palabra)))
    print pos
    del pos[:]

# test: se automatiza la verificacion de los resultados

