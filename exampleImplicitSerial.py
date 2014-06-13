# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: equipo de desarrollo
'''
from tools.serial import get_pattern
from tools.pdftolist import pdf2string
from tools.diccionarios import lista_diccionario
import json

"""
word=[]
for i in range(1,len(sys.argv)):
    word.append(sys.argv[i])
"""

path = "files/biblia.pdf"
sheets = pdf2string(path=path)

words = lista_diccionario()
print words
#print "\n",frase
rank = 0


for word in words:
    match = [[{'word':word, 'page':page, 'jump':rank + 1, 'position':get_pattern(text=sheet, rank=rank, word=word)}
          for page, sheet in enumerate(sheets)] for word in words ]
    match = sum(match,[])
    match = [m for m in match if m['position'] != set([])]

for m in match:
    m['position']=list(m['position'])[0]
print json.dumps(match)


# test: se automatiza la verificacion de los resultados

