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


match = [[[{'word':word, 'page':page, 'jump':r + 1, 'position':get_pattern(text=sheet, rank=r, word=word)}
          for page, sheet in enumerate(sheets)] for word in words ]for r in range(rank*100,(rank+1)*100)]

match = sum(match, [])
match = sum(match, [])
match = comm.gather(match, root=master)

if rank == master:
    match = clearMatch(match)

    sheets = [str2matrix(text=sheet, ncol=ncol) for sheet in sheets]    
    nhojas = [len(s) for s in sheets]
    #creamos un diccionario con todas las series
    series = [{'name':w, 'data':[len([m for m in match if m['word']==w])]} for w in words]
    
    #buscamos todos los pares ordenados entre tiempo y largo de la palabra
    
    scatter = [(s['word_lengh'], s['time']) for s in match]
    
    bible = {'sheets':sheets, 'match':match, 'nhojas':nhojas, 'words':words, 'series':series, 'scatter':scatter}
    print json.dumps(bible)
    print json.dumps(bible)
    
