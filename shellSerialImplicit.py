# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: equipo de desarrollo
'''
from tools.serial import get_pattern
from tools.pdftolist import pdf2string
import json
import sys
from tools.diccionarios import lista_diccionario

path = sys.argv[1]
words = lista_diccionario()
sheets = pdf2string(path=path)

rank = 0

match = [[{'word':word, 'page':page, 'jump':rank + 1, 'position':get_pattern(text=sheet, rank=rank, word=word)}
      for page, sheet in enumerate(sheets)] for word in words ]
match = sum(match, [])
match = [m for m in match if m['position'] != set([])]

for m in match:
    m['position'] = list(m['position'])[0]
    
bible = {'sheets':sheets, 'match':match}
print json.dumps(bible)    

    
