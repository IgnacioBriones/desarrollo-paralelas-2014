# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: leonardo jofre
'''

from mpi4py import MPI
from time import time
from tools.stringamatriz import str2matrix
from tools.serial import get_pattern, clearMatch
from tools.parallelpdftolist import parallelpdf2string
from tools.diccionarios import lista_diccionario
import os
import commands
import json
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
master = 0

path = sys.argv[1]
words = lista_diccionario()
words = words + [w[::-1] for w in words]
ncol = 60

sheets = parallelpdf2string(comm=comm, path=path)


match = [[{'word':word, 'page':page, 'jump':rank + 1, 'position':get_pattern(text=sheet, rank=rank, word=word)}
          for page, sheet in enumerate(sheets)] for word in words ]

match = sum(match, [])
match = comm.gather(match, root=master)

if rank == master:
    match = clearMatch(match)

    sheets = [str2matrix(text=sheet, ncol=ncol) for sheet in sheets]    
    nhojas = [len(s) for s in sheets]
    bible = {'sheets':sheets, 'match':match, 'nhojas':nhojas}
    print json.dumps(bible)
    
