# -*- coding: utf-8 -*-

from mpi4py import MPI
from PyPDF2 import PdfFileReader
import commands
import re
import time

def parallelpdf2string(comm, path):
    size = comm.Get_size()
    rank = comm.Get_rank()
    
    pdf = PdfFileReader(open(path, "rb"))
    total = pdf.getNumPages()
    auxtotal = total
    lista = []
    aux = []
    aux2 = []
    adicional = []
    master = 0
    es_multiplo = 0
    while(es_multiplo == 0):
	if total % size != 0:
            total = total + 1
        else:
            es_multiplo = 1
    pag_por_proc = total / size
    
    if rank == master:
        lista = [(i + 1) for i in range(total)]
        lista = [lista[i:i + pag_por_proc] for i in range(0, len(lista), pag_por_proc)]
      
    aux = comm.scatter(lista, root=master)
    for l in aux:
        if l <= auxtotal:
            commands.getoutput("pdftotext -f " + str(l) + " -l " + str(l) + " " + path + " " + str(l) + ".txt")
            txt = str(l) + ".txt"
            arch = open(txt, "r").read().lower()
            arch = arch.replace("á", "a")
            arch = arch.replace("é", "e")
            arch = arch.replace("í", "i")
            arch = arch.replace("ó", "o")
            arch = arch.replace("ú", "u")
            arch = arch.replace("ñ", "n")
            arch = re.sub("[^a-z]", "", arch)
            adicional.append(arch)
            commands.getoutput("rm -R " + txt)
    aux2 = comm.gather(adicional, root=master)
    if rank == master:
        lista2 = []
        for i in range(len(aux2)):
            lista2 += aux2[i]
    else:
        lista2 = None
        
    return comm.bcast(lista2, root=master)
