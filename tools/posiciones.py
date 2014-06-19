# -*- coding: utf-8 -*-
import sys
import random
import commands
import re
import math
derecha = 1
izquierda = 2
arriba = 3
abajo = 4
diag_sup_izq = 5
diag_inf_izq = 6
diag_sup_der = 7
diag_inf_der = 8
#Funcion que verifica si existe la palabra dentro de la matriz[i][j] en distintas posiciones y ordenes
def verificando(op,i,j,matriz,palabra,n):
            if (len(palabra)==0):		#solo se detendra si todas las letras de la palabra estan contenidas
                    respuesta=True 
                    return respuesta        
            else:   
                    if (op==derecha):  		#busqueda hacia la derecha   
                            i=i
                            j=j+n
                    elif (op==izquierda):   	#busqueda hacia la izquierda
                            i=i
                            j=abs(j-n)
                    elif (op==arriba):   	#busqueda hacia arriba
                            i=abs(i-n)
                            j=j
                    elif (op==abajo):   	#busqueda hacia abajo
                            i=i+n
                            j=j
                    elif (op==diag_sup_izq):     	#busqueda diagonal superior izquierda
                            i=abs(i-n)
                            j=abs(j-n)
                    elif (op==diag_inf_izq):   	#busqueda diagonal inferior izquierda
                            i=i+n
                            j=abs(j-n)
                    elif (op==diag_sup_der):   	#busqueda diagonal superior derecha
                            i=abs(i-n)
                            j=j+n
                    elif (op==diag_inf_der):   	#busqueda diagonal inferior derecha
                            i=i+n
                            j=j+n
                    else:
                            print "ERROR [+]"
                   
                    try:
                            if matriz[i][j]==palabra[0]:			#verificamos que la nueva posicion (i,j) sea igual a la letra
                                    nueva=palabra[1:]       			#recortando la letra que ya verificamos de la palabra
                                    a=verificando(op,i,j,matriz,nueva,n)        #llamamos la recursion con los nuevos datos
                                    if a==True:     
                                            return a        
                            else:
                                    respuesta=False
                                    return respuesta        
                    except: 
                            respuesta=False
                            return respuesta 
