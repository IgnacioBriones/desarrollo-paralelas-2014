# -*- coding: utf-8 -*-
import sys
import random
import commands
import re
import math
from ochoPosibilidades import Ocho_posibilidades

def Posicion_inicial(buscando,matriz,salto,pagina):
            for i in range(0,salto):     
                    for j in range(0,int(len(pagina[i])/salto)):    
			                #verificamos si hay alguna letra en esas posicion (i,j) que sea igual a la primera letra de la palabra que buscamos
                            if (buscando[0] == matriz[i][j]): 
					                          #de haberla encontrado, llamamos a verificar las ocho posibles formas de terminar de hallar la palabra
                                    terminado=Ocho_posibilidades(matriz,i,j,buscando,salto,pagina)
					
                                    if (terminado==True):   
                                            return terminado
