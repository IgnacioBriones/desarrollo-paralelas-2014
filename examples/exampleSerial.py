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
'''
Lo anterior arroja: File "example.py", line 20, in <module>
                    match = get_pattern(text=sheet, rank=2, word="casa")
                    File "/home/cluster/Escritorio/pruebas/tools/serial.py", line 24, in get_pattern
                    text_rank1 = text[np.arange(0, len(text), rank + 1)]
                    TypeError: len() of unsized object
'''
