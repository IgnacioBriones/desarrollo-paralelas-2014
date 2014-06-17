# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: leonardo jofre
'''

from mpi4py import MPI
from time import time
import os
import commands
import json
from tools.diccionarios import lista_diccionario
import sys
from tools.stringamatriz import str2matrix

try:
    from tools.serial import get_pattern
    from tools.parallelpdftolist import parallelpdf2string
except Exception:
    print "el nodo con ip " + commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:] + " y rank " + str(MPI.COMM_WORLD.rank) + "no reconoce las librerias" 

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
currentDir = os.path.dirname(os.path.abspath(__file__))

words = ["perro", "casa"]
words = words + [w[::-1] for w in words]
path = currentDir + '/files/biblia.pdf'
sheets = parallelpdf2string(comm=comm, path=path)

master = 0
print len(sheets)
match = [[{'word':word, 'page':page, 'jump':rank + 1, 'position':get_pattern(text=sheet, rank=rank, word=word)}
          for page, sheet in enumerate(sheets)] for word in words ]

match = sum(match, [])
match = [m for m in match if m['position'] != set([])]
match = comm.gather(match, root=master)

if rank == master:
    match = [m for m in match if m != []]
    match = sum(match, [])
    
    for m in match:
        m['position'] = list(m['position'])
    
    sheets = [str2matrix(text=sheet, ncol=60) for s in sheets]    
    bible = {'sheets':sheets, 'match':match}
    print json.dumps(bible)
    
    
