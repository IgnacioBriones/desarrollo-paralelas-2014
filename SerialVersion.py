# -*- coding: utf-8 -*-

import sys
import random
import commands
import re
import math


def verificando(op,i,j,matriz,palabra,n):
			
            if len(palabra)==int(sys.argv[3]):
                    respuesta=True 
                    return respuesta        
            else:   
                    if (op==1):  		#busqueda hacia la derecha   
                            i=i
                            j=j+n
                    elif (op==2):   	#busqueda hacia la izquierda
                            i=i
                            j=abs(j-n)
                    elif (op==3):   	#busqueda hacia arriba
                            i=abs(i-n)
                            j=j
                    elif (op==4):   	#busqueda hacia abajo
                            i=i+n
                            j=j
                    elif (op==5):     	#busqueda diagonal superior izquierda
                            i=abs(i-n)
                            j=abs(j-n)
                    elif (op==6):   	#busqueda diagonal inferior izquierda
                            i=i+n
                            j=abs(j-n)
                    elif (op==7):   	#busqueda diagonal superior derecha
                            i=abs(i-n)
                            j=j+n
                    elif (op==8):   	#busqueda diagonal inferior derecha
                            i=i+n
                            j=j+n
                    else:
                            print "ERROR [+]"
                   
                    try:
                            if matriz[i][j]==palabra[0]:
                                    nueva=palabra[1:]       
                                    a=verificando(op,i,j,matriz,nueva,n)      
                                    if a==True:     
                                            return a        
                            else:
                                    respuesta=False
                                    return respuesta        
                    except: 
                            respuesta=False
                            return respuesta        
                           
def Ocho_posibilidades(matriz,i,j,palabra,p):
            posibles={1:"hacia la derecha", 2:"hacia la izquierda", 
            3:"hacia arriba", 4:"hacia abajo", 5:"en forma Diagonal Superior Izquierda",
            6:"en forma Diagonal Inferior Izquierda", 7:"en forma Diagonal Superior Derecha", 
            8:"en forma Diagonal Inferior Derecha"}
            nueva=palabra[1:]       
            for n in range(1,int(sys.argv[2])):
					for x in range(1,9):
							veri=verificando(x,i,j,matriz,nueva,n)    
							if (veri==True):        
									print "La palabra '{0}' esta ubicada en la posicion ({1},{2}) {3} con salto {4} en la pagina {5}".format(palabra,(i+1)-60*(p[i+1]-1),j+1,posibles[x],n,p[i+1])    
									return veri	
						
								
                                   
def Posicion_inicial(buscando,matriz,M,N,p):
            for i in range(0,M):     
                    for j in range(0,N):    
                            if (buscando[0] == matriz[i][j]): 
                                    terminado=Ocho_posibilidades(matriz,i,j,buscando,p)
                                    if (terminado==True):   
                                            return terminado
                                                                         


print "Transformando de pdf a txt.
.. " + sys.argv[1]

comando = commands.getoutput("pdftotext "+sys.argv[1])
txt= sys.argv[1].replace(".pdf", ".txt");

string = open(txt).read().lower()
string = string.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n")
string = re.sub('[^a-zA-Z]', '', string)
open(txt, 'w').write(string)

L = list(string) 
tam_matriz = 60       
coincidencias = 0

largocol = float(float(len(L)) / float(tam_matriz*tam_matriz))
print "Largo Texto: " + str(len(L))
print "Largo Tamaño Lista Matrices: "+str(largocol)
print "Largo Tamaño Lista Matrices Redondeado: "+str(math.ceil(largocol))


cadena = ""
cadena2 = ""
contador = 1
cont2=1
open(txt, 'w').write(cadena)

for i in range(len(L)):
	if i == (tam_matriz * contador) - 1:
		cadena = cadena + " " + L[i]
		archi=open(txt,'a')
		archi.write(cadena+'\n')
		archi.close()
		contador = contador + 1
		cadena = ""
		"""
		if i == (tam_matriz*tam_matriz)*cont2-1:
			cont2= cont2 + 1
			archi=open(txt,'a')
			archi.write(cadena)
			archi.close()"""
	else:
		cadena = cadena + " " + L[i]

string = open(txt).read()
new_str = re.sub(' ', '', string)
open(txt, 'w').write(new_str)



archivo=open(txt,"r")
datos=archivo.readlines()       
N=M=tam_matriz


print len(L)
print str(int(M))

matriz=[]

            
for i in range (0,int(M)):      
		columna=[]              
		for j in range (0,int(N)):      
			   columna.append(datos[i][j])
			   #print "i= {0} , j= {1}".format(i,j)           
		matriz.append(columna)

#matrices = list()

c=1
p=[]
for i in range (0,int(M)):
		p.append(c)
		if(i==60*c):
			c = c+1
				
		
'''
linea = ""

for i in range(0, int(M)):
	for j in range(0, int(N)):
		linea += matriz[i][j] + " "
		if (j == N-1):
			linea += "\n"
print linea		
'''
palabras = list()

for i in range(len(sys.argv)):
	if i >= 4:
		palabras.append(sys.argv[i])
		
print palabras

for x in range (len(palabras)):      
		Posicion_inicial(palabras[x],matriz,int(M),int(N),p)  

                                   

			
			
