# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: equipo de desarrollo
'''

from tools.serial import get_pattern
from tools.pdftolist import pdf2string
import json
#

path = "files/biblia.pdf"
sheets = pdf2string(path=path)
<<<<<<< HEAD
rank = 0
=======
rank = 2
>>>>>>> cf5a84459b65b4899e4f156bfbda866fb9c49b71

words = ['casa']

for word in words:
    match = [[{'word':word, 'page':page, 'jump':rank + 1, 'position':get_pattern(text=sheet, rank=rank, word=word)}
          for page, sheet in enumerate(sheets)] for word in words ]
<<<<<<< HEAD
    match = sum(match,[])
    match = [m for m in match if m['position'] != set([])]

for m in match:
    m['position']=list(m['position'])[0]
print json.dumps(match)

# test: se automatiza la verificacion de los resultados

=======
    match = sum(match, [])
    match = [m for m in match if m['position'] != []]
    
for m in match:
    m['n'] = len(m['position'])

print json.dumps(match)

# test: se automatiza la verificacion de los resultados
>>>>>>> cf5a84459b65b4899e4f156bfbda866fb9c49b71
