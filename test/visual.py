L = list(str) #guardamos el string en una lista
salto = 500       #salto para encontrar los caracteres
L2 = list('casas')   #Palabra a buscar,(busqueda pendiente)
coincidencias = 0

largocol = len(L) / salto
cadena = ""
cadena2 = ""
contador = 1
open(txt, 'w').write(cadena)
for i in range(len(L)):
	if i == (salto * contador) - 1:
		cadena = cadena + " " + L[i]
		archi=open(txt,'a')
		archi.write(cadena+'\n')
		archi.close()
		contador = contador + 1
		cadena = ""
	elif i == len(L) - 1:
		cadena = cadena + " " + L[i]
		archi=open(txt,'a')
		archi.write(cadena+'\n')
		archi.close()
	else:
		cadena = cadena + " " + L[i]
	
string = open(txt).read()

new_str = re.sub(' ', '', string)
open(txt, 'w').write(new_str)	
