# -*- coding: utf-8 -*-

import commands
import re
import time

from PyPDF2 import PdfFileReader

def pdf2string(path):
	# abrir pdf en modo lectura
	t1 = time.time()
	pdf = PdfFileReader(open(path, "rb"))

	# imprime cuantas páginas tiene el pdf:
	numero_paginas = pdf.getNumPages()

	"""
	se inicia la cadena que almacenará el contenido de cada página
	del pdf
	""" 
	contenido_pagina = ""

	# instanciando lista a ocupar
	lista = list()
     # uso de la librería PyPDF2 para obtener la cantidad de hojas del pdf
	print "Transformando de pdf a txt... " + path
	pdf = PdfFileReader(open(path, "rb"))
	# imprime cuantas páginas tiene el pdf:
	numero_paginas = pdf.getNumPages()
	print "Numero de paginas del PDF: ", numero_paginas
	for i in range(numero_paginas+1):
		if i>=1:
			#convierte página i de pdf en txt
			commands.getoutput("pdftotext -f "+str(i)+" -l "+str(i)+" "+path)
			# reemplazo de .pdf a .txt en path
			txt= path.replace(".pdf", ".txt");
			# abrir fichero txt que trae el contenido de la página i del pdf + limpieza del string
			contenido_pagina = open(txt).read().lower()
			contenido_pagina = contenido_pagina.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u').replace('ñ','n')
			contenido_pagina = re.sub('[^a-z]', '', contenido_pagina)
			lista.append(contenido_pagina)
	print "Tiempo de ejecución: ", time.time() - t1, " segundos"
	commands.getoutput("rm -R "+txt)
	return lista
