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

ncol = 60

sheets = pdf2string(path=path)

match = [[[{'word':word, 'page':page, 'jump':rank + 1, 'position':get_pattern(text=sheet, rank=rank, word=word)}
      for page, sheet in enumerate(sheets)] for word in words ] for rank in range(100)]
match = sum(match, [])

bible = clearMatch(match, sheets,ncol,words)
print json.dumps(bible)  
