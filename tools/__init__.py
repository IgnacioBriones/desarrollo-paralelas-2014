"""pasar los indices de inicio y fin a indices de una matriz de ancho 60 columnas"""

def indexConvertionListToArray(jump, tup):
    init, end = tup
    tup = range(init, end, jump + 1)
