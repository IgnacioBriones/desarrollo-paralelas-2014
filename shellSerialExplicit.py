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

path, words = (sys.argv[1], sys.argv[2])
words = words.split()
words = words + [w[::-1] for w in words]
sheets = pdf2string(path=path)

rank = 0
match = [[{'word':word, 'page':page + 1, 'jump':rank + 1, 'position':get_pattern(text=sheet, rank=rank, word=word)}
	  for page, sheet in enumerate(sheets)] for word in words ]

path, words = (sys.argv[1], sys.argv[2])
words = words.split()
sheets = pdf2string(path=path)

rank = 0

match = [[{'word':word, 'page':page, 'jump':rank + 1, 'position':get_pattern(text=sheet, rank=rank, word=word)}
      for page, sheet in enumerate(sheets)] for word in words ]

# el match tiene todas las coincidencias de la biblia, pero dentro viene con campos vacios e informacion
# incompleta que se debe deducir, como lo son por ejemplo, el numero de ocurrencias de una palabra en una hoja2

match = clearMatch(match)

sheets = [str2matrix(text=sheet, ncol=60) for s in sheets]
bible = {'sheets':sheets, 'match':match}
print json.dumps(match)

   


    
