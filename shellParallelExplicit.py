# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: leonardo jofre
'''
from mpi4py import MPI
from time import time
from tools.serial import get_pattern, clearMatch
from tools.parallelpdftolist import parallelpdf2string
from tools.stringamatriz import str2matrix
import time
import os
import commands
import json
import sys
from tools import removeInvalidChar

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
master = 0
size = comm.size
path, words = (sys.argv[1], sys.argv[2])
words = removeInvalidChar(words)
words = words.lower().split()
words = words + [w[::-1] for w in words]
ncol = 60
sheets = parallelpdf2string(comm=comm, path=path)
match = [[[{'word':w, 'page':page, 'jump':r + 1, 'position':get_pattern(text=sheet, rank=r, word=w)}
           for r in range(rank * len(sheet)/(size*len(w)), (rank + 1) * len(sheet)/(size*len(w)))] for w in words ] for page, sheet in enumerate(sheets)]
match = sum(match, [])
match = sum(match, [])
match = comm.gather(match, root=master)

if rank == master:
    bible = clearMatch(match, sheets,ncol,words)
    print json.dumps(bible)
