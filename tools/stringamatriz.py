# -*- coding: utf-8 -*-
# funcion que con la pagina y el salto, transforma el string a una matriz para
# busquedas, retornando la matriz. Es necesario el salto para armar la matriz

import numpy as np

def matriz(pagina,salto):
	matriz=[]
	c=0
	for i in range (0,salto):      
		columna=[]              
		for j in range (0,int(len(pagina)/salto)):      
			columna.append(pagina[c])
			c = c+1
		matriz.append(columna)
	return matriz

def str2matrix(text, ncol):
	# pasamos el texto a un array cuya cantidad de elementos es el largo del texto
	text = list(text)
	
	# convertimos ese array en una matriz 60 columnas, no siempre la cantidad de datos es divisible por ncol
	# por lo que hay que hacer una correccion
	faltantes = ncol - len(text) % ncol
	cola = [" " for _ in range(faltantes)]
	text += cola
	text = np.array(text)
	text = np.reshape(text, (-1, ncol))
	text = text.tolist()
	return text
	
