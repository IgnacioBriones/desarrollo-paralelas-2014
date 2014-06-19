# -*- coding: utf-8 -*-

#python explicitapdf.py -frase-
import sys

from tools.pdftolist import pdf2string
from tools.stringamatriz import matriz
from tools.posicionInicial import Posicion_inicial

#creamos una lista llamada pagina, que almacenara las paginas
pagina = []

#pagslimpias es el string que aloja el pdf formateado por paginas como es el
#path se le puede poner la ruta en donde esta el pdf
pagslimpias = pdf2string('./../files/biblia.pdf') 

#almacenamos cuantas paginas quiere buscar en el pdf, en este caso buscaria en 4 paginas(desde la pagina 1 hasta la 4)
inicio = 3
fin = 6
numero_paginas= fin - inicio
for i in range(numero_paginas + 1):
	pagina.append(pagslimpias[i])   

#lista que contiene las palabras de nuestra frase
palabras = []
for i in range(len(sys.argv)):
	if i >= 1:
		palabras.append(sys.argv[i])

matriz1 = []
for i in range(numero_paginas + 1):
	salto = 10
	matriz1.append(matriz(pagina[i],salto))


# Funcion que revisa en cada pagina (ya en forma de matriz), cada palabra de la frase.
for i in range(numero_paginas + 1):
	for x in range (len(palabras)):      
		Posicion_inicial(palabras[x],matriz1[i],salto,int(len(pagina[i])/salto),salto,i)
		

