# -*- coding: utf-8 -*-

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
