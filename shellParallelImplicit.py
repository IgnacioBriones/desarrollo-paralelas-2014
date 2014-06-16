# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: leonardo jofre
'''

from mpi4py import MPI
from time import time
import commands
import json
from tools.diccionarios import lista_diccionario
from tools.stringamatriz import str2matrix
import sys


try:
    from tools.serial import get_pattern
    from tools.pdftolist import pdf2string
except Exception:
    print "el nodo con ip " + commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:] + " y rank " + str(MPI.COMM_WORLD.rank) + "no reconoce las librerias" 

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

path = sys.argv[1]
words = lista_diccionario()
master = 0
sheets = None

if rank == master:
    #
    t = time()
    sheets = pdf2string(path=path)
# usamos las mismas hojas para cada uno de los procesadores
sheets = comm.bcast(sheets, root=master)

match = [[{'word':word, 'page':page, 'jump':rank + 1, 'position':get_pattern(text=sheet, rank=rank, word=word)}
          for page, sheet in enumerate(sheets)] for word in words ]

match = sum(match, [])
match = [m for m in match if m['position'] != set([])]
match = comm.gather(match, root=master)

if rank == master:
    match = [m for m in match if m != []]
    match = sum(match, [])
    
    for m in match:
        m['position'] = list(m['position'])[0]
    sheets = [str2matrix(text=sheet, ncol=60) for s in sheets]   
    bible = {'sheets':sheets, 'match':match}
    print json.dumps(bible)
    
    
