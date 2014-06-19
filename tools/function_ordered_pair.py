##Función que recibe posición de un elemento en una lista y retorna su posición
##en forma de par ordenado al transformar el vector a una matriz de 60 columnas.


#Recibe valor que es la posición del elemento en la lista.
def ordered_pair(position):
    #Se crea una tupla para representar (fila,columna)
    pair = (0,0)
    #Si la posición es menor que 60 esta si o si en la primera fila de la matriz
    #por lo que se retorna de inmediato la posición sin hacer calculos.
    if position < 60:
        pair = 0,position
        return pair
    else:
        #Se calcula la fila en la que estará alojado el elemento
        row = position // 60
        #Se calcula la columna donde estará alojado el elemento
        column = -(row * 60) + position
        #Se arma la tupla con la fila y la columna
        pair = (row,column)
        return pair
