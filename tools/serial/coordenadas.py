# -*- coding: utf-8 -*-

import numpy as np

def misma_recta(var):
    es_igual = True   
    if len(var) <= 1:
        return True
    else:
        p0 = var[0]
        p1 = var[1]
        x0 = p0[1]
        x1 = p1[1]
        y0 = p0[0]
        y1 = p1[0]        
        try:
            # Pendiente Finita
            pendiente = (y1 - y0)/(x1 - x0)
            for i in range(2,len(var)):
                pendiente2 = float(var[i][0] - y0) / (var[i][1] - x0)
                if pendiente == pendiente2:
                    es_igual = True
                else:
                    es_igual = False
                    break
            return es_igual
        except ZeroDivisionError:
            # Pendiente Infinita
            for i in range(1,len(var)):
                if x0 == var[i][1]:
                    es_igual = True
                else:
                    es_igual = False
                    break
            return es_igual
        
def misma_recta_2(coor):
    c = np.array(coor)
