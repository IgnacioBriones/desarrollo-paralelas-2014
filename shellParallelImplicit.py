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
from tools.serial import get_pattern, clearMatch
from tools.parallelpdftolist import parallelpdf2string

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
master = 0

path = sys.argv[1]
words = lista_diccionario()
words = words + [w[::-1] for w in words]

sheets = parallelpdf2string(comm=comm, path=path)


match = [[{'word':word, 'page':page, 'jump':rank + 1, 'position':get_pattern(text=sheet, rank=rank, word=word)}
          for page, sheet in enumerate(sheets)] for word in words ]

match = sum(match, [])
match = comm.gather(match, root=master)

if rank == master:
<<<<<<< HEAD
    match = [m for m in match if m != []]
    match = sum(match, [])
    
    for m in match:
        m['position'] = list(m['position'])
    sheets = [str2matrix(text=sheet, ncol=60) for s in sheets]   
=======
    match = clearMatch(match)

    sheets = [str2matrix(text=sheet, ncol=60) for sheet in sheets]    
>>>>>>> 87d64d40942fdd1e78660b79538c3fd0805866a5
    bible = {'sheets':sheets, 'match':match}
    print json.dumps(match)
    
    
