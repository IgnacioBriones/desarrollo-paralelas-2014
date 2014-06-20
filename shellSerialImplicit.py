# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: equipo de desarrollo
'''
from tools.serial import get_pattern, clearMatch
from tools.pdftolist import pdf2string
import json
import sys
from tools.diccionarios import lista_diccionario
from tools.stringamatriz import str2matrix

path = sys.argv[1]
words = lista_diccionario()
words = words + [w[::-1] for w in words]
sheets = pdf2string(path=path)

rank = 0

match = [[{'word':word, 'page':page, 'jump':rank + 1, 'position':get_pattern(text=sheet, rank=rank, word=word)}
      for page, sheet in enumerate(sheets)] for word in words ]
match = clearMatch(match)

for m in match:
    m['position'] = list(m['position'])
    
sheets = [str2matrix(text=sheet, ncol=60) for sheet in sheets]
nhojas = [len(s) for s in sheets]
bible = {'sheets':sheets, 'match':match, 'nhojas':nhojas}
print json.dumps(bible)   

    
