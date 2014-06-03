# -*- coding: utf-8 -*-
'''
Created on 14-05-2014

@author: leonardojofre
'''

from mpi4py import MPI
from tools.serial import get_pattern
import random

comm = MPI.COMM_WORLD()
rank = comm.Get_rank()

if rank == 0:
    
    # a modo de ejemplo generamos un array de numeros aleatorios
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    
    # Generamos un vector aleatorio con esta informacion posible
    N = 1000000
    text = [random.choice(alfabeto) for _ in range(N)]
    print "codigo de la biblia en paralelo"
    word = "casa"
    comm.scatter(data=text)
    comm.scatter(data=word)
    
match = get_pattern(text, rank, word)


if rank == 0:
    
    
    
