# -*- coding: utf-8 -*-
#funcion que con la pagina y el salto, transforma el string a una matriz para busquedas, retornando la matriz. Es necesario el salto para armar la matriz
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
