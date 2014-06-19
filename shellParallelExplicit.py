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
from tools.stringamatriz import str2matrix
import sys

try:
    from tools.serial import get_pattern
    from tools.pdftolist import pdf2string
except Exception:
    print "el nodo con ip " + commands.getoutput("/sbin/ifconfig").split("\n")[1].split()[1][5:] + " y rank " + str(MPI.COMM_WORLD.rank) + "no reconoce las librerias" 

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
currentDir = os.path.dirname(os.path.abspath(__file__))

path, words = (sys.argv[1], sys.argv[2])
words = words.split()

master = 0
sheets = None

if rank == master:
    #
    t = time()
    # path = currentDir + "/../files/biblia.pdf"
    
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
        m['position'] = list(m['position'])

    sheets = [str2matrix(text=sheet, ncol=60) for sheet in sheets]    
    bible = {'sheets':sheets, 'match':match}
    json.dumps(bible)


    print json.dumps(bible)

    
