# -*- coding: utf-8 -*-

import PyPDF2
import sys
import re


from PyPDF2 import PdfFileWriter, PdfFileReader

input1 = PdfFileReader(open(sys.argv[1], "rb"))

# imprime cuantas páginas tiene el pdf:
print  sys.argv[1] + " tiene %d paginas." % input1.getNumPages()
pagina = int(sys.argv[2])

# el contenido de la página "pagina" queda almacenado en string
salida = input1.getPage(pagina).extractText()

# imprime texto contenido en la página indicada y almacenado en string
print salida


# letras minusculas
salida2 = salida.lower()

# eliminación de otros caracteres
new_str = re.sub('[^a-zA-Z]', '', salida2)

# texto almacenado en string y modificado
print new_str
