# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: leonardojofre
'''

from mpi4py import MPI
from tools.serial import get_pattern
from tools.pdfstring import pdf2string
from time import time

comm = MPI.COMM_WORLD()
rank = comm.Get_rank()

words = ["casa", "perro", "cielo"]
master = 0
if rank == master:
    #
    t = time()
    print "leyendo la biblia . . ."
    
    path =  "./../files/biblia.pdf"
    sheets = pdf2string(path, borrarCaracteresEspeciales=True, separadosPorHoja=True)
    
    print "biblia leida en ", time() - t, " segundos"
else:
    sheets = None
    
# usamos las mismas hojas para cada uno de los procesadores
comm.bcast(sheets, root=master)

match = {}
for word in words:   
    match[word] = [get_pattern(text=sheet, rank=rank, word=word) for sheet in sheets]

# pasar cada resultado de cada uno de los nodos al maestro

if rank == master:
    pass
    
    
