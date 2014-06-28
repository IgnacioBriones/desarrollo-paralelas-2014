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
import re

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
master = 0

path = sys.argv[1]
words = lista_diccionario()
words = words + [w[::-1] for w in words]
regex = re.compile("|".join(words))
ncol = 60
size = comm.size

sheets = parallelpdf2string(comm=comm, path=path)

match = [[{'page':page, 'jump':r + 1, 'position':get_pattern(text=sheet, rank=r, regex=regex)}
           for r in range(rank * 200, (rank + 1) * 200)] for page, sheet in enumerate(sheets)]
match = sum(match,[])
match_temp = []
for m in match:
    
    for n in m['position']:
        u = {}
        u['position'] = n[1]
        u['jump'] = m['jump']
        u['word'] = n[0]
        u['time'] = n[2]
        u['page'] = m['page']
        match_temp.append(u)

match = match_temp
for m in match:
    m['position'] = [m['position']]
       
   
match = comm.gather(match, root=master)

if rank == master:
    bible = clearMatch(match, sheets, ncol, words) 
    print json.dumps(bible)
    
