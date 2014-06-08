# -*- coding: utf-8 -*-

import sys
import random
import commands
import re
import time
import numpy as np
import re

from tools.pdftolist import pdf2string
from tools.stringamatriz import matriz
from tools.posicionInicial import Posicion_inicial

#creamos una lista llamada pagina, que almacenara las paginas
pagina = list()

#pagslimpias es el string que aloja el pdf formateado por paginas
pagslimpias = pdf2string('c.pdf') #como es el path se le puede poner la ruta en donde esta el pdf

#almacenamos cuantas paginas quiere buscar en el pdf, en este caso buscaria en 4 paginas(desde la pagina 1 hasta la 4)
inicio = 3
fin = 6
numero_paginas= fin - inicio
for i in range(numero_paginas + 1):
	pagina.append(pagslimpias[i])   

#lista que contiene las palabras de nuestra frase
palabras = list()
for i in range (len(sys.argv)):
	if i >= 1:
		palabras.append(sys.argv[i])

matriz1 = list()
for i in range(numero_paginas + 1):
	salto = 10
	matriz1.append(matriz(pagina[i],salto))


# Funcion que revisa en cada pagina (ya en forma de matriz), cada palabra de la frase.
for i in range(numero_paginas + 1):
	for x in range (len(palabras)):      
		Posicion_inicial(palabras[x],matriz1[i],salto,int(len(pagina[i])/salto),salto,i)

#python explicitapdf.py laboratorio paralela 
