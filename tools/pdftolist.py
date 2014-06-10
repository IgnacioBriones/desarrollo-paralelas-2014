# -*- coding: utf-8 -*-

import commands
import re
import time

from PyPDF2 import PdfFileReader

def pdf2string(path):
    # tiempo inicial
    t1 = time.time()
    # se inicia la cadena que almacenará el contenido de cada página
    # del pdf
    contenido_pagina = ""
    # instanciando lista a ocupar
    lista = list()
    # abrir pdf en modo lectura
    pdf = PdfFileReader(open(path, "rb"))
    # imprime cuantas páginas tiene el pdf:
    numero_paginas = pdf.getNumPages()
    # uso de la librería PyPDF2 para obtener la cantidad de hojas del pdf
    print "Numero de paginas del PDF: ", numero_paginas
    print "Transformando de PDF a TXT... ", path
    for i in range(numero_paginas):
        #convierte página i de pdf en txt
        commands.getoutput("pdftotext -f "+str(i+1)+" -l "+str(i+1)+" "+path)
        # reemplazo de .pdf a .txt en path
        txt= path.replace(".pdf", ".txt");
        # abrir fichero txt que trae el contenido de la página i del pdf + limpieza del string
        contenido_pagina = open(txt).read().lower()
        contenido_pagina = contenido_pagina.replace('á','a')
        contenido_pagina = contenido_pagina.replace('é','e')
        contenido_pagina = contenido_pagina.replace('í','i')
        contenido_pagina = contenido_pagina.replace('ó','o')
        contenido_pagina = contenido_pagina.replace('ú','u')
        contenido_pagina = contenido_pagina.replace('ñ','n')
        contenido_pagina = re.sub('[^a-z]', '', contenido_pagina)
        lista.append(contenido_pagina)
        commands.getoutput("rm -R "+txt)
        
    print "Tiempo de transformación de PDF: ", time.time() - t1, " segundos"
    return lista
