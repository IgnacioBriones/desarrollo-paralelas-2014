# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: equipo de desarrollo
'''
from tools.serial import get_pattern, clearMatch
from tools.pdftolist import pdf2string
from tools.stringamatriz import str2matrix
from tools.diccionarios import lista_diccionario
import json
import sys

path = sys.argv[1]
words = lista_diccionario()
words = words + [w[::-1] for w in words]

ncol=60

sheets = pdf2string(path=path)

match = [[[{'word':word, 'page':page, 'jump':rank + 1, 'position':get_pattern(text=sheet, rank=rank, word=word)}
      for page, sheet in enumerate(sheets)] for word in words ] for rank in range(100)]
match = sum(match, [])

match = clearMatch(match)
    
sheets = [str2matrix(text=sheet, ncol=ncol) for sheet in sheets]
nhojas = [len(s) for s in sheets]
#creamos un diccionario con todas las series
series = [{'name':w, 'data':[len([m for m in match if m['word']==w])]} for w in words]

#buscamos todos los pares ordenados entre tiempo y largo de la palabra

scatter = [(s['word_lengh'], s['time']) for s in match]

bible = {'sheets':sheets, 'match':match, 'nhojas':nhojas, 'words':words, 'series':series, 'scatter':scatter}
print json.dumps(bible)
print json.dumps(bible)   
