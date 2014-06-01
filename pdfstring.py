# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 00:22:26 2014

@author: marco
"""

import re
import sys
import os

def pdf2string(path, borrarCaracteresEspeciales, separadosPorHoja):
    # herramientas a usar    
    from PyPDF2 import PdfFileReader
    
    # abrir pdf en modo lectura
    pdf = PdfFileReader(open(path, "rb"))

    # imprime cuantas páginas tiene el pdf:
    paginas = pdf.getNumPages()
    
    # se inicia la cadena que contendrá las páginas 
    contenido_pagina = ""
    
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
            for i in range(0, paginas):
                contenido_pagina = pdf.getPage(i).extractText().lower()
                string_limpieza = re.sub('[^a-zA-Z]', '',contenido_pagina)
                lista.append(string_limpieza)
                content = ""
            return lista
        # caso 2: borrando caracteres especiales, sin separar hojas
        # retorna un string
        else:
            for i in range(0, paginas):
                contenido_pagina += pdf.getPage(i).extractText().lower()
            string_limpieza = re.sub('[^a-zA-Z]', '',contenido_pagina)
            return string_limpieza
    else:
        # caso 3: sin borrar caracteres especiales, separados por hoja
        # retorna una lista
        if separadosPorHoja:
            for i in range(0, paginas):
                lista.append(pdf.getPage(i).extractText().lower())
            return lista
        # caso 4: sin borrar caracteres especiales, sin separar hojas
        # retorna un string
        else:
            for i in range(0, paginas):
                contenido_pagina += pdf.getPage(i).extractText().lower()
            return contenido_pagina
