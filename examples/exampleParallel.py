# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: leonardo jofre
'''

from mpi4py import MPI
from tools.serial import get_pattern
from tools.pdftolist import pdf2string
from time import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

words = ["casa", "perro", "cielo"]
master = 0
if rank == master:
    #
    t = time()
    print "leyendo la biblia . . ."
    
    path = "./../files/biblia.pdf"
    sheets = pdf2string(path=path)
    
    print "biblia leida en ", time() - t, " segundos"
else:
    sheets = None
    
# usamos las mismas hojas para cada uno de los procesadores
comm.bcast(sheets, root=master)

  
match = [[(index, word, rank + 1, get_pattern(text=sheet, rank=rank, word=word)) 
          for index, sheet in enumerate(sheets)] for word in words ]
match = sum(match, [])
match = [m for m in match if m[3] != set([])]

# pasar cada resultado de cada uno de los nodos al maestro
print match
print len(match)
if rank == master:
    pass
    
    
