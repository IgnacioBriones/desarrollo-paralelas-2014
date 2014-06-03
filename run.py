'''
Created on 25-05-2014

@author: leonardo jofre
'''

from mpi4py import MPI
import webServer
import tools

comm = MPI.COMM_WORLD
rank = comm.rank
root = 0
if(rank == root):
    # levantar el servidor web
    webServer.run()
    
    Bibletext = tools.pdf
    


if rank == root:
    # recibir los resultados y desplegarlos
    


