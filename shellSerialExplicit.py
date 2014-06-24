# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: equipo de desarrollo
'''
from tools.serial import get_pattern, clearMatch
from tools.pdftolist import pdf2string
from tools.stringamatriz import str2matrix
import json
import sys
from tools import removeInvalidChar
from numpy import mean


path, words = (sys.argv[1], sys.argv[2])
words = removeInvalidChar(words)
words = words.lower().split()
ncol = 60  # numero de columnas de la hoja

words = words + [w[::-1] for w in words]
sheets = pdf2string(path=path)

match = [[[{'word':word, 'page':page, 'jump':rank + 1, 'position':get_pattern(text=sheet, rank=rank, word=word)}
      for page, sheet in enumerate(sheets)] for word in words ] for rank in range(100)]

match = sum(match, [])

match = clearMatch(match)

sheets = [str2matrix(text=sheet, ncol=ncol) for sheet in sheets]
nhojas = [len(s) for s in sheets]

# creamos un diccionario con todas las series
series = [{'name':w, 'data':[len([m for m in match if m['word'] == w])]} for w in words]

# buscamos todos los pares ordenados entre tiempo y largo de la palabra
scatter = [(s['word_lengh'], s['time']) for s in match]

# luego de calcular el desempeño, dividimos por la cantidad de palabras encontradas antes de ese salto
performance = [(s['jump'], s['time']) for s in match]

#buscamos el tiempo promedio por cada rank
performance = [(q[0],mean([p[1] for p in performance if p[0]==q[0]]))for q in performance]

#performance = [(p[0],p[1]/len([q for q in performance if q[0]<=p[0]])) for p in performance]

bible = {'sheets':sheets,
         'match':match,
         'nhojas':nhojas,
         'words':words,
         'series':series,
         'scatter':scatter,
         'performance':performance}
         
print json.dumps(bible)   
# print match
