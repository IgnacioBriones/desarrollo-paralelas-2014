#Verificar si una lista de pares ordenados pertenece a una misma recta

def vr(coords):
    coords.sort()
    x=[]
    y=[]
    for i in range(len(coords)):
        x.append(coords[i][0])
        y.append(coords[i][1])

    if(len(coords)<=1):
        return True

    try:
        m = (y[1]-y[0])/(x[1]-x[0])
	q = y[1] - m*x[1]

	aux=0

        for i in range(0,len(coords)):
	    if((y[i]-m*x[i]-q)==0):
                aux=1
	    else:
		aux=0
	 	return False
		break

        if(aux==1):
            return True
   
    except ZeroDivisionError:
        aux=0
        suma=0
        c=0
        for i in range(len(coords)):
            if(x[i]==0):
                print x[i]
                c=1
            else:
                return False
                break
        
        if(c==1):
            for i in range(len(coords)):
                suma = suma + y[i]
            if (suma%len(coords)-1):
                return True
            else:
                return False
