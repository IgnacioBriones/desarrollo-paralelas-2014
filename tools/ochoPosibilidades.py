# -*- coding: utf-8 -*-
import sys
import random
import commands
import re
import math
from posiciones import verificando
#funcion que recibe como parametros, la matriz de busqueda, las posiciones i,j, la palabra a buscar, el salto maximo y la pagina donde esta la palabra
def Ocho_posibilidades(matriz,i,j,palabra,salto,pagina):
            posibles={1:"hacia la derecha", 2:"hacia la izquierda", 
            3:"hacia arriba", 4:"hacia abajo", 5:"en forma Diagonal Superior Izquierda",
            6:"en forma Diagonal Inferior Izquierda", 7:"en forma Diagonal Superior Derecha", 
            8:"en forma Diagonal Inferior Derecha"}
            nueva=palabra[1:]       
            for n in range(1,salto):
					for x in range(1,9):
							veri=verificando(x,i,j,matriz,nueva,n)    
							if (veri==True):        #si es verdadero, signifia que se hallo la palabra
									print "La palabra {0} esta ubicada en la posicion ({1},{2}) {3} con salto {4} en la pagina {5}".format(palabra,i+1,j+1,posibles[x],n,pagina+1)    
									#return veri #retornamos que la encontramos, para evitar que se siga con las demas posibles formas de hallarla(descomentar para encontrar solo 1 vez la palabra)
