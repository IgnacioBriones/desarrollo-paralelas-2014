# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 00:22:26 2014

@author: marco
"""

import re
from PyPDF2 import PdfFileReader

def pdf2string(path, borrarCaracteresEspeciales, separadosPorHoja):
    # abrir pdf en modo lectura
    pdf = PdfFileReader(open(path, "rb"))

    # imprime cuantas páginas tiene el pdf:
    numero_paginas = pdf.getNumPages()
    
    # se inicia la cadena que almacenará el contenido de las páginas del pdf 
    contenido_libro = ""
    
    # instanciando lista a ocupar
    lista = list()

    """
    NOTA: Cuando se ejecuta el borrado de caracteres especiales, los acentos
    también son eliminados, aunque se incluyan en la sustitución; por lo que
    se intentará buscar una solución a este problema.
    """
    
    # caso 1: borrando caracteres especiales, separados por hoja
    # retorna una lista
    if borrarCaracteresEspeciales:
        if separadosPorHoja:
            for i in range(numero_paginas):
                contenido_pagina = pdf.getPage(i).extractText().lower()
                string_limpieza = re.sub('[^a-zA-Z]', '',contenido_pagina)
                lista.append(string_limpieza)
            return lista
        # caso 2: borrando caracteres especiales, sin separar hojas
        # retorna un string
        else:
            for i in range(numero_paginas):
                contenido_libro += pdf.getPage(i).extractText().lower()
            string_limpieza = re.sub('[^a-zA-Z]', '',contenido_libro)
            lista.append(string_limpieza)
            return lista
    else:
        # caso 3: sin borrar caracteres especiales, separados por hoja
        # retorna una lista
        if separadosPorHoja:
            lista = [pdf.getPage(i).extractText().lower() for i in range(numero_paginas)]
            return lista
        # caso 4: sin borrar caracteres especiales, sin separar hojas
        # retorna un string
        else:
            for i in range(numero_paginas):
                contenido_libro += pdf.getPage(i).extractText().lower()
            lista.append(contenido_libro)
            return lista